from django.shortcuts import render, redirect ,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib.auth.models import User 
from django.contrib.auth import logout, authenticate, login

# Create your views here.

def index(request):
    context = {
        'variable': 'boy',
    }
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        return render(request, "index.html", context)
    # return HttpResponse('This is my page')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    # Handling Form data and pull it on database 
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        
    return render(request, 'contact.html')

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get("password")
        #check if user entered correct credintial
        user = authenticate(username=username, password=password)
        # normal user 
            # username -> user
            # password -> Sushant@@@123***
        # super user 
            # username -> sushant
            # password -> Sushant
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    # Redirect to a success page.
    return redirect("/login")