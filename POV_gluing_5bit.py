#  This is python program to create images for a POV display

#  This program will load in an image, convert it to a usable format,
#  dice it up into smaller regions, and average the RGB values.  The
#  output will be a file that can be read in by an Arduino

#  The dicing will dice the image into a radius, theta based divisions.
#  The format will be one byte per R, G, and B, per LED per division.  

#  Setup
import Image
import math

def paint(rad,polar,hue,im):
   maxImage = 6.75  #The LED image will have a rad of 6.750"  The first LED is at .625"
   minImage = .625  #Each LED is 5/16"
   LEDsize = .075  #How much to average over to get the right color
   numPixels = min(im.size)
   averagewindow = int(math.ceil(LEDsize*numPixels/maxImage))
    
   midx = math.floor(im.size[0]/2 + ((-1)**rad)*(.625+rad*5.0/16.0)*numPixels/maxImage/2*math.cos(2*math.pi*polar/numDivisions))
   midy = math.floor(im.size[1]/2 + ((-1)**rad)*(.625+rad*5.0/16.0)*numPixels/maxImage/2*math.sin(2*math.pi*polar/numDivisions))
      

   for x in range(-averagewindow, averagewindow):
      for y in range(-averagewindow, averagewindow):
         pix[midx+x,midy+y] = hue
   return 

startImage = "./BlankTest.jpg"
inputfile = "./outputtest.txt"
numDivisions = 45
numLED = 20

infile = open(inputfile,'r');

#  Load the image.
im = Image.open(startImage)

#  How big is it?
(height, width) = im.size

#min(height, width)

pix = im.load()

for polar in range(0, numDivisions):
   for rad in range(0, numLED):
         RGBtext = infile.readline().strip()
         hue = (((int(RGBtext) & 31744) >> 10) * 8,((int(RGBtext) & 992) >> 5) * 8,(int(RGBtext) & 31) * 8)    
         paint(rad,polar,hue,im)
         
im.save("./5bitfortsailboat.jpg","JPEG")      




