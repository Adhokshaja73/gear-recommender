from django.shortcuts import render
from django.http import JsonResponse
from .recommender import *
from .models import *
# Create your views here.
# a function to return homepage
def homePage(request):
    # get the video from the database
    video = Videos.objects.all()
    # add the video to the context
    context = {'video': video}
    # render the homepage
    return render(request, 'home.html', context)

# this function takes post request with parameters
# 1 : image
# and returns a response with the recommended gear in JSON format

def getGear(request):
    image = request.POST['image']
    # convert the image to opencv image
    print(image)
    print(image.shape)
    # crop the image to get the speedometer from 75% bottom and 80% right of the image
    # cropped = image[int(image.shape[0]*0.75):, int(image.shape[1]*0.8):]
    # # use aws rekognition to get the 
    # recommended_gear = recommendGear(image)

    return JsonResponse({'gear': 2})