from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import SignupForm, LoginForm
from .service.create_user import create_user,create_user_role
# Create your views here.
# Home page
def index(request):
    return render(request, 'index.html')

# signup page
def user_signup(request):
    err = ""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Process the form data
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            nama = form.cleaned_data['nama']
            gender = form.cleaned_data['gender']
            tempat_lahir = form.cleaned_data['tempat_lahir']
            tanggal_lahir = form.cleaned_data['tanggal_lahir']
            kota_asal = form.cleaned_data['kota_asal']
            roles = form.cleaned_data['roles']
            err = create_user(email, password, nama, gender, tempat_lahir, tanggal_lahir, kota_asal)            
            if err != "":
                render(request, 'signup.html', {'form': form,"error_message":err})
            err = create_user_role(roles,email)
            if err != "":
                render(request, 'signup.html', {'form': form,"error_message":err})
            # Do somethng with the form data
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form,"error_message":err})

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user:
                login(request, user)    
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')