from django.http import HttpResponse
from django.shortcuts import render

def home(request):
   # return HttpResponse('HOME PAGE')
   return render(request, 'index.html')
def about(request):
   return render(request, 'about.html')
   # return HttpResponse('ABOUT PAGE')
def contact(request):
   # return HttpResponse('CONTACT PAGE')
   return render(request, 'contact.html')
