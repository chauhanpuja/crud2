
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from crudapp.forms import StudentRegistration
from .models import User_Data
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout



# Create your views here.
def addandshow(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            ps=fm.cleaned_data['password']
            reg=User_Data(name=nm,email=em,password=ps)
            fm.save()
            messages.info(request,'Successfully registered a Student')
            fm=StudentRegistration()
    else:
        fm=StudentRegistration()
    stu=User_Data.objects.all()

    return render(request,'addandshow.html',{'form':fm,'stu':stu})
   
    # return render(request,'addandshow.html')

def update_data(request,id):
    if request.method=='POST':
        pi=User_Data.objects.get(pk=id)
        fm=StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=User_Data.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)
        messages.info(request,'Updated Sucessfully')

    return render(request,'updatestudent.html',{'form':fm})  

def delete_data(request,id):
    if request.method=='POST':
        pi=User_Data.objects.get(pk=id)
        pi.delete()
        messages.info(request,'Successfully deleted')
    return HttpResponseRedirect('/')




def signup(request):
   
    if request.method=="POST":
        username=request.POST.get('username')
        name=request.POST.get('name')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')

        if User.objects.filter(username=username).exists():
            messages.info(request,"Username already taken")
            return redirect("signup")
        
        if User.objects.filter(email=email).exists():
            messages.info(request,"Email already taken")
            return redirect("signup")


        if len(username)>10:
            messages.error(request,"Username must be under 10 character")
            return redirect("signup")

        if not username.isalnum():
            messages.error(request,"Username should only contain letters and numbers")
            return redirect("signup")
        
        if pass1 != pass2:
            messages.error(request,"Password do not matched")
            return redirect("signup")

        # create user
        myuser=User.objects.create_user(username,email,pass1)
        myuser.name=name
        myuser.save()

      
        messages.success(request,"User Created")
        return redirect("/")
        
    else:

       
        return render(request,'signup.html')
    

def userlogin(request):
    
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        

        user=authenticate(username=username,password=password)
        
        if user is not None:
            login(request, user)
            
            messages.success(request,'Successfully logged In')
            return redirect('/')

        else:
            messages.error(request,'User not Signup')
            return redirect('/') 
    return render(request,'userlogin.html')


def userlogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')