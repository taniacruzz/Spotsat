from django.urls import path # a função path() é usada para mapear URLs para views no Django
from . import views

urlpatterns = [
    path('v1/', views.returnMessage),
    path('v1/auth/', views.authenticateUser),
    path('v2/places/', views.returnPlaces),
    path('v2/places/:id', views.returnPlacesById)
]