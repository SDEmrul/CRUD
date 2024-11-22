from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from todo.models import Student



def home(request):


    data=Student.objects.all()
    if request.method=="POST":
        sname=request.POST.get("n")
        sage=request.POST.get("a")
        semail=request.POST.get("e")
        obj=Student()
        obj.name=sname
        obj.age=sage
        obj.email=semail
        obj.save()
  
    return render(request,"home.html",{"e":data})

def signup(request):

    if request.method=="POST":
        uname=request.POST.get("n")
        uemail=request.POST.get("e")
        uusername=request.POST.get("u")
        upassword=request.POST.get("p")
        obj=User()
        obj.first_name=uname
        obj.username=uusername
        obj.email=uemail
        obj.set_password (upassword)
        obj.save()
        return redirect('l')
  
    return render(request,"signup.html")

def login(request):

    if request.method=="POST":
        username=request.POST.get("u")
        upassword=request.POST.get("p")
        user = authenticate(username=username, password=upassword)
        
        if user is None:
            print("not found")
            # Display an error message if authentication fails (invalid password)

            return redirect('l')
        else:
            print("found")
            # Log in the user and redirect to the home page upon successful login
            login(request,user)
            return redirect('h')
    
    # Render the login page template (GET request)
    return render(request, 'login.html')  
 
def d(request,pk):
    data=Student.objects.get(id=pk)
    data.delete()
    return redirect('h')

def update(request,pk):


    data=Student.objects.get(id=pk)
    if request.method=="POST":
        sname=request.POST.get("n")
        sage=request.POST.get("a")
        semail=request.POST.get("e")
        obj=Student()
        obj.id=pk
        obj.name=sname
        obj.age=sage
        obj.email=semail
        obj.save()
        return redirect('h')
  
    return render(request,"update.html",{"e":data})
