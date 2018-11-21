/*  Persistence of Vision Image Manipulator

This is code to turn an image into code that my POV arduino code can read and output

The input file will be a jpg or some other type of photo.
The output will be a chunk of text that will be read by my Arduino code for displaying a photo.*/

// Declare some variables

const int divisions = 60;  //divisions
const int LEDnum = 10;  //number of RGB LEDs
int ID = 2; // Internal Dimension percentage
int angle;
int radius;

int i;
int j;

array data[divisions,LEDnum*3];  //3 LEDs per RGB LED
 
string inputfile = "helloworld.jpg";
int width; 
int height;
int OD;  //Outer Dimension


// Main Loop
void loop() {

//find size of inputfile
//[width, height] = size(inputfile);
OD = min(width,height);


for (i = 0; i <= divisions; i += 1) {
  for (j = 0; j <= LEDnum; j += 1){

    angle = i * 360/divisons;  
    radius = ID*OD/100 + j*OD*(100-ID)/200/LEDnum;

    data[i][j*3+0] = Just the RED function;
    data[i][j*3+1] = Just the Green function;
    data[i][j*3+2] = Just the Blue function;

  }
}
