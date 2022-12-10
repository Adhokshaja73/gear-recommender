from django.shortcuts import render
from django.http import JsonResponse
from .recommender import *
import cv2
import numpy as np
from base64 import b64decode

# Create your views here.
# a function to return homepage
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
    # crop the image to get the speedometer from 75% bottom and 80% right of the image
    # cropped = image[int(image.shape[0]*0.75):, int(image.shape[1]*0.8):]
    # # use aws rekognition to get the 
    # recommended_gear = recommendGear(image)

    return JsonResponse({'gear': 2})