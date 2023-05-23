from django.urls import path # a função path() é usada para mapear URLs para views no Django
from . import views

urlpatterns = [
    path('v1/', views.returnMessage),
    path('v1/auth/', views.authenticateUser),
    path('v2/places/', views.returnPlacesBD), # rota refeita, agora com persistência dos dados
    path('v2/places/:<int:id>', views.returnPlacesByIdBD), #rota refeita, agora com persistência dos dados
    path('v3/places/', views.newPlace),
    path('v3/places/update/:<int:id>', views.updatePlace),
    path('v3/places/delete/:<int:id>', views.deletePlace),
    path('v4/places/:<int:id1>/distancia/:<int:id2>', views.distance),
    # path('v4/search/latitude={latitude}&longitude={longitude}&radius={raio}', views.placesInRatio),
    path('v4/search/', views.placesInRatio),
    # path('v4/search?latitude:<str:latitude>&longitude:<str:longitude>&radius:<str:radius>', views.placesInRatio)
]