from django.shortcuts import render
from django.http import JsonResponse
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
    # convert the image to opencv image
    header, encoded = data_uri.split(",", 1)
    data = b64decode(encoded)
    nparr = np.fromstring(data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    print(img.shape)
    
    speed = getSpeed(img)
    rpm = getRpm(img)

    recommendedGear = recommender.getGear(img, speed, rpm)
    return JsonResponse({'gear': recommendedGear})


def getSpeed(image):
    # crop the image where the speed is
    # get the number in it from aws 
    # return the number
    pass

def getRpm(img):
    # crop the image where the speed is
    # get the number in it from aws 
    # return the number
    pass