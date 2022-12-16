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
    
    speed = getSpeed(time)
    rpm = getRpm(index)
    recommendedGear = recommender.getGear(img, speed, rpm)
    return JsonResponse({'gear': recommendedGear})

def getSpeed(time):
    speeds = [49,24,2,25,60,84,68,75, 76, 85, 80,72, 88,85,98,99,113, 115,102,]
    index = time % len(speeds)
    return speeds[index]

def getRpm(time):
    rpms = [2000, 1000, 300, 1000, 2000,2500, 2200, 2000, 2500, 3000, 3500, 3300, 3500, 4000, 4500, 5000, 6000, 6500]
    index = time % len(rpms)
    return rpms[index]