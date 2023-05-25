#Face Recognition Project - Android Things Individual Project by Serafim Socaciu

Project Description:
In this project, I have created a face recognition system using a Raspberry Pi, a camera module, and a LED. The system utilizes the Raspberry Pi's GPIO pins, LED bulb, and various software libraries such as OpenCV and face_recognition. The goal is to develop a system that can recognize faces captured by the camera and perform specific actions, such as lighting up an LED when a known face is detected.

Schematics:
The project involves the following components:
Raspberry Pi 3 (Model B v1.2) specification 
Raspberry Pi Camera Module or compatible USB webcam specification 
LED bulb
Jumper wires

Pre-requisites:
Hardware components:
Raspberry Pi 3 (Model B v1.2) - Specification
Raspberry Pi Camera Module - Specification
LED bulb
Jumper wires

Software components:
Python programming language -Python
OpenCV library -OpenCV
face_recognition library -face_recognition
RPi.GPIO library for Python -RPi.GPIO

Building Steps:
Set up the Raspberry Pi and camera module:
Install the Raspberry Pi OS on an SD card and insert it into the Raspberry Pi.
Connect the camera module to the Raspberry Pi's camera connector (or connect a USB webcam).
Enable the camera interface in the Raspberry Pi Configuration settings (Preferences > Raspberry Pi Configuration > Interfaces > Camera).
Wire the LED to the breadboard:
Connect the positive (longer) leg of the LED to a GPIO pin on the Raspberry Pi (e.g., GPIO 18) using a jumper wire.
Connect the other end of the resistor to a GND pin on the Raspberry Pi using another jumper wire.

Running Steps:
Ensure that all the hardware components are connected as per the schematics and all the software components are installed.
Run the script using the provided train or test program arguments.
To train the face recognition system, execute the script with the "train" argument. This step involves capturing and storing faces for future recognition.
To test the face recognition system, execute the script with the "test" argument followed by either a filename or “camera” as to either test an already existing image or capture a new image using the camera. This step involves capturing faces, comparing them with the trained faces, and performing actions (e.g., lighting up the LED) based on recognition results.
Most important function: we load the known faces obtained in the training faze and now we test the given frame’s encodings against the known faces encodings. I there is a match, then we output a high signal using GPIO library on the specified led pin, else, we output a low signal, meaning that the LED connected will not light up, indicating there is no known face detected.
At the end, we save the image with the face having a bounding box around it, coloured in either green, if the face is known, or red, if the face is unknown.
