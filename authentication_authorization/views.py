from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def home(request): 
    return HttpResponse("This is auth system !!")
def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("account create done")
    else:
        form = UserCreationForm()
        print("user came to form")
    return render(request, 'signup.html', {'form': form})