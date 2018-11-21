#  This is python program to create images for a POV display

#  This program will load in an image, convert it to a usable format,
#  dice it up into smaller regions, and average the RGB values.  The
#  output will be a file that can be read in by an Arduino

#  The dicing will dice the image into a radius, theta based divisions.
#  The format will be 5bits per R, G, and B, per LED per division.  

#  Setup
import Image
import math

def average(rad,polar,im):
   maxImage = 6.75  #The LED image will have a rad of 6.750"  The first LED is at .625"
   minImage = .625  #Each LED is 5/16"
   LEDsize = .075  #How much to average over to get the right color
   numPixels = min(im.size)
   averagewindow = int(math.ceil(LEDsize*numPixels/maxImage))
   
   GammaRed = 1;      
   GammaGreen = 1;  #These are the gamma correction values for the LEDs
   GammaBlue = 1;

   red = 0
   blue = 0
   green = 0  
   midx = math.floor(im.size[0]/2 + ((-1)**rad)*(.625+rad*5.0/16.0)*numPixels/maxImage/2*math.cos(2*math.pi*polar/numDivisions))
   midy = math.floor(im.size[1]/2 + ((-1)**rad)*(.625+rad*5.0/16.0)*numPixels/maxImage/2*math.sin(2*math.pi*polar/numDivisions))
   for x in range(-averagewindow, averagewindow):
      for y in range(-averagewindow, averagewindow):
         red = red + pix[midx+x,midy+y][0]
         green = green + pix[midx+x,midy+y][1]
         blue = blue + pix[midx+x,midy+y][2]
 
   #This will be where we do gamma correction


   red = int(math.floor((red+16)/(averagewindow*averagewindow*4*8)))  # dividing the window into 32nds so we can add them all together.
   green = int(math.floor((green+16)/(averagewindow*averagewindow*4*8)))   
   blue = int(math.floor((blue+16)/(averagewindow*averagewindow*4*8)))
   return ((red << 10) + (green << 5) + blue)   # All the colors are now in the same 2 byte package

startImage = "./fortsailboat.jpg"
outputfile = "./outputtest.txt"
numDivisions = 45
numLED = 20

outfile = open(outputfile,"w");
outfyle = open('./arduinoready.txt',"w");

#  Load the image.
im = Image.open(startImage)

#  How big is it?
(height, width) = im.size

#min(height, width)

pix = im.load()

for polar in range(0, numDivisions):
   for rad in range(0, numLED):

      outfyle.write('0x')
      
      #converted = '%(num)d' % {"num": average(rad,polar,im)}    #For Arduino output
      converted2 = '%(num)04X' % {"num": average(rad,polar,im)}    #For Arduino output   
      converted = '%(num)05d' % {"num": average(rad,polar,im)} #Only for POV_gluing_5bit.py    
         
      outfile.write(converted)
      outfyle.write(converted2)
      #outfile.write(',')

      outfile.write('\n')  #Only for an outputfile that needs to be tested with POV_gluing_5bit.py   
      #outfyle.write('L')  #No longer "long"
      outfyle.write(',')


