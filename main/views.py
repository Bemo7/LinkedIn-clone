from django.shortcuts import render
# from models import
from django.http import HttpResponse, HttpResponseRedirect, Http404

# Create your views here.

def home(request):
  return render(request,'index.html')