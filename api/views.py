from rest_framework.response import Response # retorna dados convertidos em uma resposta HTTP adequada
from rest_framework.decorators import api_view
from rest_framework import status #  constantes usadas para retornar respostas adequadas a diferentes situações em sua API
from rest_framework import generics
from api.models import User, Place
from api.serializers import UserSerializer, PlaceSerializer
from django.views.decorators.csrf import csrf_exempt


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
def returnPlacesById(request):
    places = Place.objects.filter(id=1)
    serializer = PlaceSerializer(places, many=True)
    return Response(serializer.data)

   

