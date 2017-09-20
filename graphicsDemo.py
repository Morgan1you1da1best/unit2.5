#Morgan Baughman
#9/20/17
#graphicsDemo.py - Learning how to use graphics! Intro to ggame.

from ggame import *

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black) #pixels, color

redRectangle = RectangleAsset(200,100,blackOutline,red) #Width, height, outline, fill.
blueCircle = CircleAsset(50,blackOutline,blue) #Radius, outline, fill.
greenEllipse = EllipseAsset(100,50,blackOutline,green) #horizontal radius, verticle radius, outline, fill
blackLine = LineAsset(50, 160, blackOutline) #x_endpoint, y_endpoint, LineStyle
redTriangle = PolygonAsset([(0,0),(120,180),(60,300)],blackOutline, red) #List of endpoints, outline, fill
text = TextAsset('Fellas, is it gay?' ,fill=red, style='bold 40pt Times')

Sprite(redRectangle)
Sprite(blueCircle,(50,50))
Sprite(greenEllipse, (200,400))
Sprite(blackLine)
Sprite(redTriangle)
Sprite(text, (200,200))
App().run()


