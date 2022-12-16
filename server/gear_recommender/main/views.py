from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import cv2
import numpy as np
from base64 import b64decode
from .recommender import *


# Create your views here.
# a function to return homepage
recommender = GearRecommender()


def homePage(request):
    return render(request, 'home.html')

# this function takes post request with parameters
# 1 : image
# and returns a response with the recommended gear in JSON format

def getGear(request):   
    data_uri = request.POST['image']
    index = int(request.POST["index"])
    # convert the image to opencv image
    encoded = data_uri.split(",", 1)    
    data = b64decode(encoded[1])
    nparr = np.fromstring(data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    speed = getSpeed(index)
    rpm = getRpm(index)
    recommendedGear = recommender.getGear(img, speed, rpm)
    return JsonResponse({'gear': recommendedGear})

def getSpeed(index):
    speeds = [45]
    return speeds[index]
    pass

def getRpm(index):
    rpms = [4500]
    return rpms[index]