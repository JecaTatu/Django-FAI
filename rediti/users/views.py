from django.shortcuts import render
from django.views import generic
from .models import User
from django.contrib import auth
from django.contrib.auth import views, get_user_model, authenticate
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from .forms import UserForm
from .models import User

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

class SignupView(generic.FormView):
    template_name = "users/signup.html"
    form_class = UserForm
    redirect_authenticated_user = True 
    model = get_user_model()

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('common:home'))
        return super(SignupView, self).get(request)

    def form_valide(self, form):
        self.object = form.save()
        user = authenticate(username=self.object.email, password=form.cleaned_data['password'])
        auth.login(self.request, user)

        return redirect('common:home')