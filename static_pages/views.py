from django.shortcuts import HttpResponse

# Create your views here.

def home(request):
   return HttpResponse ("Pagina Home")

def help(request):
   return HttpResponse ("Pagina Help")

def about(request):
   return HttpResponse ("Pagina About")


