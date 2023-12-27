from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail

from .forms import SignupForm,ActivationForm
from .models import Profile

from django.conf import settings



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']

           # to prevent the user from logining to page without the code 
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            profile = Profile.objects.get(user__username=username)
            send_mail(
                "Activate Your Email",
                f"Welcome {username} \nuse this code {profile.code} to activate your email ",
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )

            return redirect(f'/accounts/{username}/activate')

    else:
        form = SignupForm()
    
    return render(request,'registration/register.html',{'form':form})

def activate(request,username):
    profile = Profile.objects.get(user__username=username)
    if request.method == 'POST':
        form = ActivationForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            if code == profile.code:
                profile.code = ''
                
                # to make the user login to page after useing code
                user = User.objects.get(username=profile.user.username)
                user.is_active = True
                user.save()

                profile.save()

                return redirect('/accounts/login') 
    else:
        form = ActivationForm()

    return render(request,'registration/activate.html',{'form':form})
