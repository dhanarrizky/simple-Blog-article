from django.urls import path
from . import views as v

urlpatterns = [
    #path('Login/', v.LoginView, name='login'),
    path('Register/', v.UserRegistrationView.as_view(), name='register'),
    path('edit_profile/', v.UserEditeProfile.as_view(), name='edit-profile'),
    path('<int:pk>/update_profile/', v.UpdateProfile.as_view(), name='update-profile'),
] 
