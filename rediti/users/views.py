from django.shortcuts import render
from django.views import generic
from .models import User
from django.contrib.auth import views
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

class ProfileView(generic.DetailView):
    template_name = "users/profile.html"
    model = User

class LogoutView(views.LogoutView):
    next_page = 'common:home'


class LoginView(views.LoginView):
    template_name = "users/login.html"
    success_url = reverse_lazy('common:home')
    redirect_authenticated_user = True 

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('common:home'))
        return super(LoginView, self).get(request)