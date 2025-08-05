from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.
def home(request): 
    return HttpResponse("This is auth system !!")
def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return HttpResponse("account create done!!!!")
    else:
        form = UserCreationForm()
        print("user came to form")
    return render(request, 'signup.html', {'form': form})
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password= password)
            django_login(request, user)
            return HttpResponse("account login done!!!!")
    else:
        form = AuthenticationForm()
        print("user came to form")
    return render(request, 'login.html', {'form': form})

@login_required #login lagbei 😊
def logout(request): 
    django_logout(request)
    return HttpResponse("user logged out !!!")