from typing import Any, Optional
from django.db import models
from django.shortcuts import render

from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .form import RegistrasionForm
from BlogArticle.models import Profile


# Create your views here.
class UserRegistrationView(generic.CreateView):
    form_class = RegistrasionForm
    template_name ='registration/register.html'
    success_url = reverse_lazy('login')
    
class UserEditeProfile(generic.UpdateView):
    form_class = RegistrasionForm
    template_name ='registration/register.html'
    success_url = reverse_lazy('my-post')
    
    def get_object(self):
        return self.request.user
    
class UpdateProfile(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile.html'
    fields = ['bio','profile_pic']
    success_url = reverse_lazy('my-post')