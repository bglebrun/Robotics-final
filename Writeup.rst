****************************************************************
Introduction To Robotics Final Projcet
****************************************************************
--------------------------------------------------------------
Cameron Parette & Ben LeBrun
--------------------------------------------------------------

********
Abstract
********
The goal of this project is to create a simple path following robot using OpenCV and methods outlined in the Introduction To Robotics course at SDSMT.
The initial challenge involved the robot navigating a pre-defined course, turning at intersections in a direction mapped to the robot.
Due to constraints in the course, the challenge was later modified to remove the mapping and instead focus on lane keeping.
With the modified approach the goal was to have the robot stay on the sidewalk and drive straight down without crossing over onto the terrain.

************
Robot Design
************

----------
Frame
----------
Our frame consists of two primary components. The first component is a plastic frame re-purposed from an Arduino "car kit".
This portion houses the four gear motors along with an L298n H-bridge for driving the motors.
This portion of the frame can be seen below in Figure ####.

The second part of the frame is a simple round baking sheet used to hold all digital components of the robot.
We chose this for the frame due to its rigidity, durability, and low cost.
Since the sheet is made of metal it will provide enough shielding between the noisy motors and the digital logic preventing interference.

We first test fitted the two sections of the frame together with tape, revealing that the upper portion would contact the wheels.
To address this issue we placed a small piece of Masonite panel in between the two portions of the frame, giving the clearance needed for the the wheels.
All portions were bonded together using JB Weld brand adhesive and were allowed to set for 12 hours before continuing.
The fully assembled frame is shown below in Figure ####.

-------------------
Motors and H-Bridge
-------------------
The motors used for the robot are common DC geared motors that can be found easily on Amazon and often include wheels.
The motors run off of 3 to 6 Volts and provide enough torque to drive the robot due to the gearing.
The wheels included with the motors should provide adequate traction for the purpose of the robot.
Figure #### below shows the motors and H-bridge circuit.

----------
Main board
----------
The main board chosen for this project was the Atomic Pi single board computer.
We chose this board due to the low $40 price and compelling hardware specifications.
The Atomic Pi uses a quad core Intel Atom X5-Z8350 paired with 2GB DDR3L RAM and 16GB eMMC storage.
The Atomic Pi also includes integrated GPIO, a 9 axis navigation sensor, and a plethora of standard PC connectivity options.

Included with the Atomic Pi is a small breakout board that makes powering the SBC and accessing GPIO much easier.
The connector on the breakout board makes it possible to easily remove the SBC without removing the wiring for the GPIO and power, allowing us to work on the chassis of the robot without fear of damaging the hardware.
An image of the breakout board is shown below in Figure ####.

The board requires a 5 volt power supply that is capable of sourcing up to 3 milliamps of current.
This makes the board usable with many commercially available power supplies and USB battery banks, reducing overall development complexity.

We mounted the SBC to the frame of the robot using brass standoffs and glue to prevent shorting out the board, while allowing it to be easily removable.
The SBC mounted to the frame is shown below in Figure ####.

-------------
Camera
-------------
Initially we used the camera included with the Atomic Pi as our sensor, however we had many issues accessing the camera within Python; this made image processing difficult and unpredictable.
Further testing revealed that the camera would power on and off without reason leading us to conclude it was faulty.

To remedy this, we used an off the shelf USB webcam with a 720p 30 FPS sensor.
We removed the shell of the camera in order to more easily attach it to the robot.
It is important to note that nearly any USB based camera will be acceptable for this application. Increased resolution and framerates will lead to more processing overhead which could cause a performance decrease, in this application we are sampling the image at 800 by 600 pixels.

Mounting the camera to the frame of the robot was accomplished using a large copper wire with a thick rubber insulation, glue and zip ties.
The copper was flexible enough to allow us to position the camera as needed while being strong enough to not move when not intended.
The camera and its mounting can be seen below in Figure ####.

----------
Batteries
----------
The mainboard is powered by a 10400 mAh battery pack that outputs 5 volts at up to 3 amps of current.
This component was chosen due to its features and low cost.
The battery pack charges via a micro USB cable and has USB A ports for plugging into the mainboard.

The H-bridge is powered by 2 LiPo batteries included with the Arduino "smart car" kit.
These batteries output roughly 8 volts and supply ample current to the H-bridge.
The batteries are also re-chargeable via an included charger.

----------------
Power Generator
----------------
An attempt to provide a "proof of concept" power generator was attempted on this robot.
The goal was to use a small internal combustion engine to turn a small DC generator providing power for the electric drive line.
Below we will outline our attempt at this concept and attempt to provide a foundation for future development of this concept.
Figure #### below shows the assembled system.

============
Nitro Motor
============
We initially chose to use a Toki 0.05 Nitro motor from an RC car to generate power for the robot.
We felt its small size would work well for our applications, however we ran into issues using this motors.
The motor was very difficult to start and would not run for any meaningful period of time.
We discovered this was due to the engine needing an exhaust system that would assist with pumping fuel from the fuel tank as the engine ran.
Attempting to find a muffler that would fit the Toki proved to be difficult and we eventually abandoned this option.

We then sourced a Cox Sure Start .049 model plane motor.
The Cox requires no exhaust to run and is smaller and easier to place than the Toki.
Starting the Cox proved difficult; conventional model planes use a spring attached to the propeller to start.
Our motor did not include a propeller or spring, and all attempts to manual start the engine failed.
We believe the engine is functional and able to generate power if a method to reliably start the engine is implemented.

=============
DC Generator
=============
In order to generate DC power we used a simple DC motor wired in reverse.
Applying a voltage across the terminals of a DC motor causes it to rotate, however the reverse also occurs.
By spinning the DC motor we can generate a voltage across its terminals, allowing us to power devices on the robot by.
Spinning the the DC motor using a Nitro motor would allow us to convert chemical energy to electrical energy.
This can be useful due to the higher energy density and no recharge time of combustion engines.

We used a simple DC motor sourced from a broken printer.
To verify that the motor would work for our applications we wired a DMM to it while spinning it with an electric drill spinning at 2000 RPM.
Measuring the output gave 7.8 volts meaning we would be able to power the drive line of the robot if proper measures were taken to smooth the output of the generator.

====================================
Coupling The Engine To The DC Motor
====================================
To couple the DC generator to the Nitro engine we attempted to fashion a belt driven pulley system similar to a car.
We first attempted to use a rubber band as a belt, but had issues with the belt creeping up and then off the pulleys.
Secondly we used a nylon hair tie that worked well when spun using the drill mentioned above.

==============================
Fuel Cell Design
==============================
In order to supply the Nitro motor with fuel we needed to develop a fuel tank and fuel line to the motor.
The small size of the motor meant that we did not need an overly large fuel tank for the robot.
We fashioned a small tank out of a 50 milliliter beverage bottle that includes a resealable lid.
We tapped a small hole into the container and inserted 3/32 fuel line into it.
We then ran this line to the fuel inlet on the Cox Sure Start.

==============================
Regulating The Output Voltage
==============================
Stable output voltage is required for predictable operation of the robot.
In order to smooth the output of the DC generator we used a DC to DC buck converter.
The converter allows us to adjust the output voltage of the system and set a current limit to protect anything we attach to it.
These units are pre-manufactured and are of low cost making it ideal for this application.

-----------
Parts List
-----------
Below is a list of parts that are specific to this robot.
Many of the components used could easily be replaced with something similar such as our baking sheet used in the frame.
We have decided to only include the critical components in this list, anyone wishing to replicate this project should be able to find solutions to the remaining components using a little imagination.

Critical Parts:

- `Atomic Pi SBC kit with mini breakout board and camera as shown here <https://www.amazon.com/DLI-Atomic-Pi-Peripheral-Camera/dp/B07DVYDDV8/ref=sr_1_3?keywords=atomic+pi&qid=1576714701&sr=8-3>`_.
- `Geared motors with wheels similar to these <https://www.amazon.com/Electric-Magnetic-Gearbox-Plastic-Yeeco/dp/B07DQGX369/ref=sr_1_5?keywords=geared+motor&qid=1576715104&sr=8-5>`_.
- `L298N motor controller like similar to this <https://www.amazon.com/PChero-Controller-Module-Stepper-Arduino/dp/B07GTCWN9Z/ref=sr_1_18?keywords=l298n&qid=1576715419&sr=8-18>`_.
- `USB battery pack similar to this one <https://www.amazon.com/Omars-10000mAh-Slimline-Portable-Compatible/dp/B07G26S5V8/ref=sr_1_6?keywords=battery+pack&qid=1576715552&sr=8-6>`_.
- `Generic robot car frame like this one <https://www.amazon.com/wheel-layer-Chassis-Encoder-Arduino/dp/B06VTP8XBQ/ref=sr_1_7?keywords=arduino+car&qid=1576715694&sr=8-7>`_.
  Note this one also includes motors and wheels.
- A battery of roughly 9 volts to power the motors. A simple 9 volt battery will work or a more robust solution `like this <https://www.amazon.com/Tenergy-Capacity-Rechargeable-Standard-Connector/dp/B001BA292A/ref=sr_1_2?keywords=robot+car+battery&qid=1576716030&sr=8-2>`_. Will also work.

DC Generator Parts:

- Any DC motor capable of producing the required voltage will do such as `this one <https://www.amazon.com/RS-550s-18v-Electronic-Controlled-Replacement/dp/B00TE42PME/ref=sr_1_26?keywords=12+dc+motor&qid=1576716922&sr=8-26?>`_.
- `A DC to DC voltage regulator such similar to this <https://www.amazon.com/gp/product/B011G0BNCG/ref=ppx_yo_dt_b_asin_title_o07_s00?ie=UTF8&psc=1>`_.
- `Cox sure start nitro motor <https://www.ebay.com/itm/Surestart-Cox-049-model-airplane-engine-New/223476877248?epid=907509424&hash=item34084287c0:g:-pkAAOSwZW5aPUmP>`_.
- `Fuel line <https://www.amazon.com/gp/product/B0006MZKJ8/ref=ppx_yo_dt_b_asin_title_o04_s00?ie=UTF8&psc=1>`_.
- `Nitro fuel <https://www.amazon.com/gp/product/B00D253TAS/ref=ppx_yo_dt_b_asin_title_o06_s00?ie=UTF8&psc=1>`_.

-----------------
Assembly
-----------------
With the exception of the frame, all components were attached using high strength hot glue, or nuts and bolts.
In order for the hot glue to stick to the frame we needed to sand off the non-stick material coating the baking sheet.
After sanding and cleaning applying a liberal amount of glue results in a strong hold after a proper set time.
Images of the fully assembled robot are shown below in Figure ####.

**********
Software
**********
----------------
Basic Algorithm
----------------
In order to more easily comprehend the methods discussed in future sections, we will outline the basic algorithm used for navigation.
No code or specific methods will be discussed in this section, and some details will be left intentionally vague to not cloud the concept with details.

We begin by capturing an image of the path currently in front of the robot, while this image is incredibly useful it contains a large amount of information we do not need.
Cropping the horizon off of the image helps us isolate the path in front of us.
Sometimes it may also be useful to crop some of the bottom of the image off as well.
This cropped image we will refer to as the "Region Of Interest" or ROI.

Now that we have our ROI isolated we need to do some modifications to make finding the path within the ROI easier.
Our current image has a wide array of color values making isolation difficult, even grayscale images have a wide array of values that complicate the process.
To get past this hurdle we use a process known as binary thresholding.
This method converts an image with many color values to one that simply has two, black and white.
We simply need to pick a color value to pivot about and every color below that value will be converted to white, while every color equal to or above will be converted to black.
If we select a pivot near the color of our path it will become black while the surrounding environment will become white.

Now that we have our ROI converted to a binary image we can split it in half vertically in the center of the image.
This will give us an image for the left hand side LHS and the right hand side RHS of the robot.
We can then count the number of white pixels in each image and compare the LHS to the RHS.
If there are more white pixels on the LHS we are turned to far in that direction and must turn right to compensate; likewise if there are more white pixels on the RHS we know we will need to turn left to compensate.
In practical applications there may also be a "dead zone" in the middle.
This value will allow the robot to drive straight on if it is only slightly off path, eventually it will become far enough off the path to overcome the dead zone and will then turn to correct its course.
If not using a dead zone the robots motion may appear jagged and unstable, while having a dead zone that is too large will cause it to not respond well.
A balance can be struck and the robot can move smoothly and respond rapidly.

This process is repeated for each frame the robot takes, in our case up to 30 per second, adjusting as needed for each updated position.
Now that we have a basic understanding of the process we can dive into further details using Python code shown in the sections below.

==========================
Python Path Following Code
==========================
Below is the code we used to have the robot attempt to stay on its path using the method described in the section above.


===============================
GUI Tools For Tuning The Robot
===============================
We included a number of GUI based tools enabling the user to adjust certain parameters in real time while using the robot.
While not needed for operation, these tools help with getting the desired performance out of the robot in various conditions.

We have sliders for the following:

- Threshold values - Threshold for binary threshold processing
- Normal and Inverted - Switch between normal and inverted binary processing for different lighting/path conditions
- Region of Interest - Set the top limit of the images to be processed, should be set as close to the horizon as possible
- Deadzone - Tune to avoid "bouncing" or the robot excessively turning left or right

===============================
Image Processing considerations
===============================
In our code, as discussed above, we count the amount of white pixels that appear on screen from two halves of the same 
image. Initially this was done using a raw feed from a 720p camera at 30fps. While the framerate has not become an issue 
for either the speed of processing or saturating our ability to process, one should take careful consideration into the 
size of the image you are processing. In our code we took the 960 x 544 sized frame and downscaled it to 800 x 600. This is 
vital, as in our initial testing with whitespace counting, we encountered integer overflow very often especially in normal 
operating conditions which severely skewed our results and even produced incorrect instructions for the motor control. 
Therefore, for our method, one should consider using a downscaled sample of your camera's actual resolution. 

One more consideration we encountered is our adjustable ROI frame, among other tweakable tools for image processing. In our project 
we displayed the fully processed, greyscaled and binary thresholded image. To then display to the user where the region of 
interest lies, we used OpenCV's line drawing tools to both show the centerline of the image to display where the slice was happening, and
the horizontal cut where we were sampling only the bottom half of the image. To effectively show this back onto the processed image though, 
one should be careful to make sure to convert the image back to color, as greyscale images in OpenCV discard all color information 
even after processing which may leave helpful indication lines black and white if not properly returned to OpenCV's color space.

----------------
H Bridge control
----------------
For our L298n H-bridge, we are lucky to have a set of GPIO pins directly accessible to the Atomic Pi's operating system. 
This allows us to simply program in the pin commands to our main script without having to run through serial communication, 
networked communication, or other means of motor control communication. However, there are a few challenges that the Atomic Pi
presents us with the GPIO interface.

First, that the program will need to be run as super user (invoking sudo before python, use with care), as the Atomic Pi's GPIO pins are 
only controllable by the root usergroup. No attempt was made to attempt to change or remove these permissions for the sake 
of stability of the controller board. Second, the Atomic Pi unfortunately does not have any sort of PWM or adjustable voltage 
output. This would normally allow us to change the speed of the motors and allowing more sophisticated movement. While not a 
project ending setback, requires us to consider the limitations of the current design as a whole. One proposal we might add 
to improve this project would be to use something like a 74HC595 shit register and timing to emulate PWM to the motors.

Therefore, our code was a simple on/off statement with the motors only set to forward. During our initialization of the robot
we immediately set the H bridge to turn the wheels forward, and with our turning functions we simply turn one set of wheels off
or the other. For our purpose of following a hallway or a sidewalk, this worked fine, but could be improved for more complicated 
path following in the future.

------------------------------
Optional: Spotify integration
------------------------------
As a morale boosting endeavor and in the famous words of George Leigh Mallory who probably did not have as easy access to python 
libraries for spotify control and integration as we did; we integrated Spotify "Because it is there"; the robot with an attached 
speaker can also activate music during its line following duties.

We chose Spotify for two reasons, one is that it runs on a separate program and the libraries simply make network calls to 
command Spotify, not to be decoding or playing music while vital computer vision processing is occuring. The other is to 
avoid any legal issues with including music in projects. Therefore, this section does require the developer to have a paid
Spotify premium subscription.

`The library can be found here <https://github.com/plamere/spotipy>`_ and must be installed with pip using 
:code:`pip install git+https://github.com/plamere/spotipy`. For simplicity, we used a yaml file and the pyyaml package to 
read in the Client ID and Client Secret which can be `generated from Spotify's developer dashboard <https://developer.spotify.com/>`_.
Under no circumstance should you reveal this Client ID or Client Secret token to either an open git repo or otherwise and avoid hard coding 
the tokens in. For this project, we generated a makefile that given the proper parameters will generate this file, and the .gitignore 
will ignore any references to this generated file, preventing it from being added or committed to a repo.

Finally, feeding Spotipy the correct user credentials and a URI to a playlist of songs prepared by the developer, the robot 
will make a request to Spotify to play on any open web or phone player the selected playlist. Ideally, on a player set up on 
the Atomic Pi.

Note one issue is that where the program may need to run once without root access for the GPIO pins, as neither Chrome or Firefox 
will run as a root user for security reasons; but is necessary to login to Spotify to activate Spotipy. Simply put the block of code 
for Spotipy in your initialization stages, follow the prompted instructions to login to Spotify, and let the program give you the 
13 Access Denied error for the GPIO pins once. After that, no web browser should need to be opened and the program should be safe to 
run as root user for access to the GPIO pins. A cache file will be generated in your working directory with a token for the program to 
return to. Make sure this also does not get committed to a git repo for security reasons.