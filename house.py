#Morgan Baughman
#9/20/17
#graphicsDemo.py - Learning how to use graphics! Intro to ggame.

from ggame import *

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black) #pixels, color

redRectangle = RectangleAsset(400,400,blackOutline,red) #Width, height, outline, fill.
blackTriangle = PolygonAsset([(0,0),(300,300),(-300,300)],blackOutline, black) #List of endpoints, outline, fill

Sprite(redRectangle, (400,200))
Sprite(blackTriangle,(600,00))
App().run()

