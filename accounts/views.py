from django.shortcuts import render, redirect
from .forms import SignUpForm, UserActivateForm
from .models import Profile
from django.core.mail import send_mail

# Create your views here.


'''
   form ----> data[submit] ----> create account[not active]
   --> (1) send activation code
   --> (2) redirect-> form[activation code]
   ----> [activate user] ----> redirect-> profile
'''
def signup(request):
   
   if request.method == 'POST':
      form = SignUpForm(request.POST)
      if form.is_valid():
         username = form.cleaned_data['username'] # get username from 'form-data'
         email = form.cleaned_data['email']
         myform = form.save(commit = False)  # not saved in db
         myform.active = False
         myform.save()
         profile = Profile.objects.get(user__username = username)
         print(profile)
         print(profile.code)
         send_mail(
            subject = 'Activate Your Account',
            message = f'use this code {profile.code} to activate your account.',
            from_email = 'mshehab6@smail.ucas.edu.ps',
            recipient_list = [email],
            fail_silently = False,
         )
         return redirect(f'/accounts/{username}/activate')
   else:
      form = SignUpForm()
   
   return render(request, 'registration/signup.html', {'form':form})


def user_activate(request, username):
   profile = Profile.objects.get(user__username= username)
   if request.method == 'POST':
      form = UserActivateForm(request.POST)
      if form.is_valid():
         code = form.cleaned_data['code']    # get the input code from the form
         if profile.code == code:
            profile.code_used = True
            profile.save()
            return redirect('/accounts/login')

   else:
      form = UserActivateForm()

   return render(request, 'registration/activate.html', {'form':form})
