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
Our frame consists of two primary components. The first component is a plastic frame re-purposed from an Elegoo Arduino Robot Car Kit V3.0 (no longer being sold, any chassis with room for 4 DC motors will do).
This portion houses the four gear motors along with an L298n H-bridge for driving the motors.
This portion of the frame can be seen below in Figure ####.

The second part of the frame is a simple round baking sheet used to hold all digital components of the robot.
We chose this for the frame due to its rigidity, durability, and low cost.
Since the sheet is made of metal it will provide enough shielding between the noisy motors and the digital logic preventing interference.
Figure #### below showes the

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
It is important to note that nearly any USB based camera will be acceptable for this application. Increased resolution and framerates will lead to more processing overhead which could cause a performance decrease, in this application we are using internal OpenCV libraries to downsample the image at 800 by 600 pixels.

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

----------
Software
----------
================
Basic Algorithm
================
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


