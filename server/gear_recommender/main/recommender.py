
import numpy as np
import os
import pickle
# save the model to disk

# convert the code below into a class
class GearRecommender:
    def __init__(self):
      filePath = os.path.join( os.getcwd(), 'model.sav')
      self.loaded_model = pickle.load(open(filePath, 'rb'))

    
    def getGear(self, image, speed, rpm, ):
      slope = int(self.countPixels(image) > 75)
      y_pred = self.loaded_model.predict([[speed,rpm, slope]])
      return(y_pred)

    def countPixels(self, image):
      avgColorMap = self.getRoadColor()
      # TODO adjust these parameters based on shape of the image
      areaMinX = 150
      areaMaxX = 400
      areaMinY = 50
      areaMaxY = 400
      count = 0
      pixelCount = 0
      for i in range(areaMinX, areaMaxX):
        for j in range(areaMinY,areaMaxY):
          currentPixel = image[j][i]
          if(self.colorInRange(currentPixel, avgColorMap)):
            pixelCount += 1
          count += 1
      return (pixelCount/count * 100)

    def colorInRange(self , pixel, avgColorMap):
      avgColor = avgColorMap["avgColor"]
      diff = avgColorMap["diff"]
      r = pixel[0]
      g = pixel[1]
      b = pixel[2]
      if(r > avgColor[0] - diff[0] and r < avgColor[0] + diff[0]):
          if(g > avgColor[1] - diff[1] and g < avgColor[1] + diff[1]):
            if(b > avgColor[2] - diff[2] and b < avgColor[2] + diff[2]):
              return True
      return False

    def getRoadColor(self, image):
      roadColor = {"avgColor" : [], "diff" : []}
      avgColor = [0,0,0]
      diff = [0,0,0]
      # TODO adjust these xys based on shape of the input image
      sampleMinX = 220
      sampleMaxX = 350
      sampleY = 350

      for i in range(sampleMinX, sampleMaxX):
        currentPixel = image[sampleY][i]
        avgColor[0] = (avgColor[0] + currentPixel[0]) // 2

        avgColor[1] = (avgColor[1] + currentPixel[1]) // 2

        avgColor[2] = (avgColor[2] + currentPixel[2]) // 2

      count = 0
      for i in range(sampleMinX, sampleMaxX):
        currentPixel = image[sampleY][i]
        diff[0] = (diff[0] + (currentPixel[0] - avgColor[0])**2)
        diff[1] = (diff[1] + (currentPixel[1] - avgColor[1])**2)
        diff[2] = (diff[2] + (currentPixel[2] - avgColor[2])**2)
        count += 1
        
      diff = [int(np.sqrt(i/count)) for i in diff]
      roadColor["avgColor"] = avgColor
      roadColor["diff"]  = diff
      return(roadColor)
  
