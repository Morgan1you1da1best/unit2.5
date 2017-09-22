#Morgan Baughman
#9/22/17
#Germany.py
 
from ggame import *

red = Color(0xFF0000,1)
yellow = Color(0xFFCC33,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black) #pixels, color

redRectangle = RectangleAsset(200,50,blackOutline,red) #Width, height, outline, fill.
blackRectangle = RectangleAsset(200,50,blackOutline,black) #Width, height, outline, fill.
yellowRectangle = RectangleAsset(200,50,blackOutline,yellow) #Width, height, outline, fill.

Sprite(blackRectangle, (200,50))
Sprite(yellowRectangle, (200,150))
Sprite(redRectangle, (200,100))
App().run()

