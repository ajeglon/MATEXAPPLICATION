from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.contrib.auth import authenticate, login

from .forms import UserRegistrationForm


class Index(TemplateView):
    template_name = 'matex_app/index.html'


class Dashboard(View):
    def get(self, request):
        return render(request, 'matex_app/dashboard.html')


class SignUpView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'matex_app/signup.html', {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )

            login(request, user)
            return redirect('index')

        return render(request, 'matex_app/signup.html', {'form': form})
