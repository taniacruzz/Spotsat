from django.urls import path # a função path() é usada para mapear URLs para views no Django
from . import views

urlpatterns = [
    path('v1/', views.returnMessage),
    path('v1/auth/', views.authenticateUser),
    path('v2/places/', views.returnPlacesBD), # rota refeita, agora com persistência dos dados
    path('v2/places/:<int:id>', views.returnPlacesByIdBD), #rota refeita, agora com persistência dos dados
    path('v3/places/', views.newPlace),
    path('v3/places/update/:<int:id>', views.updatePlace),
    path('v3/places/delete/:<int:id>', views.deletePlace)
]