from django.urls import path
from .views import *

urlpatterns = [
    path('login/', UserAuthenticationView.as_view()),
    path('sign_in/', UserRegistrationView.as_view()),
    path('create_transport/', CreateTransport.as_view()),
    path('create_driver_profile/', CreateDriverProfile.as_view()),
    path('create_user_profile/', CreateUserProfile.as_view()),
    path('create_cargo/', CreateCargo.as_view()),
    path('get_all_profile_driver/', ProfileTransport.as_view()),
    path('get_all_profile_user/', CargoProfile.as_view()),
    path('update_profile_driver/', UpdateProfileDriver.as_view()),
    path('get_all_cargoes/', AllCargoes.as_view()),

]