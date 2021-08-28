from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from colorthief import ColorThief
from .forms import UploadFileForm
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def index(request):
    if request.method == 'POST':
        print("hello")
        form = UploadFileForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            tuples = ','.join([str(value) for value in handle_uploaded_file(request.FILES['file'])])
            print(tuples)
            return HttpResponse(tuples)
    else:
        form = UploadFileForm()
    return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.

def handle_uploaded_file(file):
   
    color_thief = ColorThief(file)
# get the dominant color
    return color_thief.get_color(quality=5)