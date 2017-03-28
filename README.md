# Infrared-Breakbeam
A project to measure and compare objects moving through known routes
This project uses a raspberry pi, and 2 infrared breakbeam sensors.
This project was originally intended to track "cars" moving through a marked location on two roads.
The traffic data from both roads would be compared and the raspberry pi would tweet
the fastest route based on the number of cars. In practical use, this project can be
made portable and set up anywhere a user needs to know how many of something is crossing
a path. Alerts can be modified and type of traffic can be changed as well. I wrote the 
whole program and tested the sensors using only a raspberry pi. 

Software Requirements:
Raspbian
Text Editor
Terminal

Hardware Requirements: 
Raspberry pi (with raspbian)
Monitor
HDMI cable
Mouse
Keyboard
IR Breakbeam sensors (adafruit #2167)

Notes: The sensors can wired into either 3.3v or 5v power. They have 3 wires:
Red: Power
Black: Ground
White: Analogue
