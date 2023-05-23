from psycopg2 import IntegrityError
from rest_framework.response import Response # retorna dados convertidos em uma resposta HTTP adequada
from rest_framework.decorators import api_view
from rest_framework import status #  constantes usadas para retornar respostas adequadas a diferentes situações em sua API
from api.models import User, Place
from api.serializers import UserSerializer, PlaceSerializer
from api.objects import createPlaces
from django.db.models import Max
import pyproj 

# retornar mensagem padrão
@api_view(['GET'])
def returnMessage(request):
    message = "Bem Vindo a API GeoPoly!"
    return Response({"message": message})

# simulação de sistema de autenticação
@api_view(['POST'])
def authenticateUser(request):
    serializer = UserSerializer(data=request.data)
    try:
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']    
        if email == 'admin@exemplo.com.br' and password == 'abcd1234':
            return Response({'message': 'Autenticado com sucesso!'}, status=200)
        else:
            return Response({'message': 'Falha ao autenticar!'}, status=401)
    except serializer.ValidationError as e:
        return Response({'message': 'Formato da requisição inválido!'}, status=400)
    
# retornar places
@api_view(['GET'])
def returnPlaces(request):
    places = Place.objects.all()
    serializer = PlaceSerializer(places, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def returnPlacesById(request, id):
    obj = Place.objects.get(id=id)
    # places = Place.objects.filter(id=id)
    serializer = PlaceSerializer(obj, many=True)
    return Response(serializer.data)

# retornar places, com persistência
@api_view(['GET'])
def returnPlacesBD(request):
    places = createPlaces()
    serializer = PlaceSerializer(places, many=True)
    return Response(serializer.data)

# retorna objetos do tipo place com id=1, com persistência
@api_view(['GET'])
def returnPlacesByIdBD(request, id):
    places = createPlaces()
    # lista que só receberá objetos com id=1
    filtered_places = []
    for place in places:
        if place.id == id:
            filtered_places.append(place)
    serializer = PlaceSerializer(filtered_places, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def newPlace(request):
    serializer = PlaceSerializer(data=request.data)
    if serializer.is_valid():
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # essa exceção ocorre quando há Id(PK) duplicado
        except KeyError as exc:
            # vejo qual o maior id da tabela, para pegar o valor seguinte
            max_key = Place.objects.aggregate(max_key=Max('pk'))['max_key']
            next_pk = max_key + 1
            serializer.validated_data['id'] = next_pk
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400)

@api_view(['PUT'])
def updatePlace(request, id):
    try:
        obj = Place.objects.get(id=id)
    except Place.DoesNotExist:
        return Response({'message': 'Objeto não encontrado'}, status=400)
    serializer = PlaceSerializer(obj, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_200_OK)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deletePlace(request, id):
    try:
        obj = Place.objects.get(id=id)
    except Place.DoesNotExist:
        return Response({'message': 'not found'}, status=404)
    obj.delete()
    return Response({'message': 'Lugar removido com sucesso!'}, status=200)
    
@api_view(['GET'])
def distance(request, id1, id2):
    # transforma datum, de coord. geográficas, para UTM na zona 23s.
    transformer = pyproj.Transformer.from_crs('EPSG:4326', 'EPSG:31983', always_xy=True)
    # pego a latitude e longitude dos objetos com ids especificados
    obj1 = Place.objects.get(id=id1) 
    lat1 = obj1.latitude
    lon1 = obj1.longitude
    obj2 = Place.objects.get(id=id2) 
    lat2 = obj2.latitude
    lon2 = obj2.longitude

    # converter coordenadas geográficas decimais em utm
    utm1_east, utm1_north = transformer.transform(lon1, lat1)
    utm2_east, utm2_north = transformer.transform(lon2, lat2)

    distance = (((utm1_east-utm2_east)**2 + (utm1_north-utm2_north)**2)**0.5)
    # distance = round(distance, 2)
    return Response((f"distance in meters: %.2f" %distance), status = status.HTTP_200_OK)

@api_view(['GET'])
def placesInRatio(request):
    latitude = float(request.GET.get('latitude'))
    longitude = float(request.GET.get('longitude'))
    radius = float(request.GET.get('radius'))
    
    # inicio lista na qual serão incluosos os lugares dentro do radius
    places_insideRatio = []
    transformer = pyproj.Transformer.from_crs('EPSG:4326', 'EPSG:31983', always_xy=True)
    utm_east, utm_north = transformer.transform(longitude, latitude)
    objs = Place.objects.all()
    for obj in objs:
        lat_obj = obj.latitude
        lon_obj = obj.longitude
        utm_east_obj, utm_north_obj = transformer.transform(lon_obj, lat_obj)
        distance = (((utm_east-utm_east_obj)**2 + (utm_north-utm_north_obj)**2)**0.5)
        if distance <= radius:
            serializer_obj = PlaceSerializer(obj)
            serialized_data = serializer_obj.data
            serialized_data['distance'] = distance
            places_insideRatio.append(serialized_data)
    return Response(places_insideRatio)





    





    
    