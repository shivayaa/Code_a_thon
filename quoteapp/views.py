from django.shortcuts import render

# Create your views here.
def home(request):

    return render(request,'quote/home.html')

def About(request):

    return render(request,'quote/about.html')

def Contact(request):

    return render(request,'quote/contact.html')

def Dashboard(request):


    return render(request,'quote/dashboard.html')

def user_logout(request):

    
    return redirect("/")

def Singup(request):

    
    return render(request,'quote/singup.html')

def Login(request):

    return render(request,'quote/login.html') 
