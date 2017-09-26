#Morgan Baughman
#9/26/17
#warmUp5.py - Yellow Diamond with name inside

name = input('Enter a name:')
from ggame import *

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)
yellow = Color(0xFFFF00,1)

blackOutline = LineStyle(1,black) #pixels, color

blackLine = LineAsset(50, 160, blackOutline) #x_endpoint, y_endpoint, LineStyle
yellowTriangle = PolygonAsset([(500,0),(200,300),(800,300)],blackOutline, yellow) #List of endpoints, outline, fill
yellowTriangle2 = PolygonAsset([(500,600),(200,300),(800,300)],blackOutline, yellow)
text = TextAsset(name ,fill=black, style='bold 40pt Times')

Sprite(yellowTriangle2)
Sprite(yellowTriangle)
Sprite(text, (410,260))
App().run()

