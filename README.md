# soyarf_horizon_s4
Pygame application that allows users to draw and erase last drawn circles . The size of the circle increases as long as the left mouse button is held down, and lines connect consecutive circles.
created a screen named win and fill that with white backgroud
pos1 - read previous position,left_held - check whether key is held on,set rad.
store radam colours in color by importing random.randint function.
get the mouse cursor point 
if mousebuttondown is 1, left_held become true and draw the circle.if previous circle present, it display line to consecutive circle.
mousebuttomup is 1, left_held =falseand radius change to initial value.
if left_held ,increase radius and draw the circle.

if moudebuttondown is 3 , draw a white circle above tha last drawn circle to remove.

 if space fill with white screen to clear.

if s, save as image using function.

running :  py pygamecircle.py

features 
Draw Circle	-Left Click
Increase Circle Size-	Hold Left Click
Erase Last Circle -	Right Click
Clear Screen-	Press SPACE
Save Drawing-	Press S

Author 
Soya 

2nd question
Motor control with encoder
This code is designed to control a DC motor using an encoder for precise rotation. The user inputs a target degree, and the motor rotates to that position. The encoder tracks the motor's rotation and ensures accurate positioning.
Circuit Setup
Motor Connections:
Connect motorA to pin 5 of the Arduino.
Connect motorB to pin 6 of the Arduino.
 the motor driver output pins to the motor terminals.
Connect the motor driver power pins to the power supply and ground.
Encoder Connections:
Connect encoderPin1 to pin 2 of the Arduino.
Connect encoderPin2 to pin 3 of the Arduino.
Connect the encoder power to 5V and ground to GND.
Arduino Connections:
Connect the motor driver input pins to the Arduino pins motorA and motorB.
Ensure the encoder pins are connected to interrupt-capable pins.
motorA, motorB: Pins connected to the motor driver.
key variables:
encoderPin1, encoderPin2: Pins connected to the encoder.
encoderValue: Tracks the encoder pulses.
pulsePerRevolution: Number of encoder pulses per full motor rotation (set to 360).
degree: Target degree input by the user.
total_degree: Target position in degrees.
start_degree: Current position in degrees.
working:
The user inputs a target degree via the Serial Monitor.
The motor rotates to the target position.
The encoder tracks the motor's rotation and updates the position.
The motor stops when the target position is reached.
##error##
serial monitor works and read the input
motor is not rotating .
error in getting output.

author 
Soya
