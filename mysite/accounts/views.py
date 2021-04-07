from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import models, login, authenticate, logout
from .forms import SignupForm, LoginForm

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST) # UserForm -> 사용가자 입력한 form을 받음
        if form.is_valid(): # form이 유효하면 새로운 유저 생성하고 index페이지로 redirect
            new_user = models.User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
        return redirect('/accounts/')
    else: # 비어 있는 form으로 반환해야 한다.
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form':form,}) # 틀리면

def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        userName = request.POST['username']
        userPassword = request.POST['password']
        user = authenticate(username=userName, password=userPassword)
        if user is not None:
            login(request, user)
            return redirect('blog')
        else: return HttpResponse('Login failed. Try again.')
    else: # 비어 있는 form으로 반환해야 한다.
        form = LoginForm()
    return render(request, 'accounts/index.html', {'form':form,}) # 틀리면

def signout(request):
    logout(request)
    return redirect('/accounts/')

