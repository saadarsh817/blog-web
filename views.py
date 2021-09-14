# import geekymini
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .forms import SignUpForm, LoginForm,postform,img_form
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import newpost
from django.contrib.auth.models import Group
# Create your views here.


#def new_photo(request):
    #picture=img_form(request.FILES)
    #return render(request,'geekymini/dashbaord.html',{'picture':picture})

def newhome(request):
    posts=newpost.objects.all()
    return render(request, 'geekymini/home.html',{'posts':posts})


def newabout(request):
    return render(request, 'geekymini/nabout.html')


def newcontact(request):
    return render(request, 'geekymini/contact.html')


def newsignup(request):
    if request.method == "POST":

        form = SignUpForm(request.POST)
        if form.is_valid():

            messages.success(
                request, 'congratulations !! Your signup is successfull')


            user=form.save()
            group=Group.objects.get(name='Author')
            user.groups.add(group)
    else:
        form = SignUpForm()
    return render(request, 'geekymini/signup.html', {'form': form})


def newdashboard(request):
    if request.user.is_authenticated:
        pic=img_form(request.FILES)
        posts=newpost.objects.all()
        user=request.user
        full_name=user.get_full_name()
        gps=user.groups.all()
        if pic.is_valid():
            pic.save()
        
        
        return render(request, 'geekymini/dashboard.html',{'posts':posts,'full_name':full_name,'groups':gps,'pic':pic})
    
    else:
        return HttpResponseRedirect('/login/')


def user_login(request):
    if not request.user.is_authenticated:

        if request.method == "POST":
            form = LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'login successfull')
                    return HttpResponseRedirect('/dashboard/')

        else:
            form = LoginForm()
        return render(request, 'geekymini/login.html', {'form': form})
    else:
        return HttpResponseRedirect('/dashboard/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/")

def add_post(request):
    if request.user.is_authenticated:
        if request.method =='POST':
            form=postform(request.POST)
            if form.is_valid():
                title=form.cleaned_data['title']
                desc=form.cleaned_data['description']
                pst=newpost(title=title, description=desc)
                pst.save()
                form=postform()
        else:
            form=postform()
        return render(request,"geekymini/add.html",{'form':form})
    else:
        return HttpResponseRedirect("/login/")

def update_post(request,id):
    if request.user.is_authenticated:
        if request.method== "POST":
            pi=newpost.objects.get(pk=id)
            form=postform(request.POST,instance=pi)
            if form.is_valid():
                form.save()
        else:
            pi=newpost.objects.get(pk=id)
            form=postform(instance=pi)
        return render(request,"geekymini/update.html",{'form':form})
    else:
        return HttpResponseRedirect("/login/")

def delete_post(request,id):
    if request.user.is_authenticated:
        if request.user.is_authenticated:
            pi=newpost.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')


def view_img(request):
    
    if request.method== "POST":
        img=img_form.objects.all()
        