from django.shortcuts import render

# Create your views here.


'''
   form ----> data[submit] ----> create account[not active]
   --> (1) send activation code
   --> (2) redirect-> form[activation code]
   ----> [activate user] ----> redirect-> profile
'''
def signup(request):
   pass

