#Morgan Baughman
#9/27/18
#Yield Sign.py

from ggame import *

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)
white = Color(0xFFFFFF, 1)

blackOutline = LineStyle(1,black) #pixels, color

whiteTriangle = PolygonAsset([(500,0),(200,500),(800,500)],blackOutline, red) #List of endpoints, outline, fill
redTriangle = PolygonAsset([(500,100),(300,450),(700,450)],blackOutline, white) #List of endpoints, outline, fill
text = TextAsset('Yield' ,fill=red, style='bold 40pt Times')

Sprite(whiteTriangle)
Sprite(redTriangle)
Sprite(text, (450,300))
App().run()


