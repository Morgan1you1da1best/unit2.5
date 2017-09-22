#Morgan Baughman
#9/22/17
#name.py

name= input('Enter your name: ')
color_input = input('Enter a hex code: ')

from ggame import *

color = Color(color_input, 1)
black = Color(0x000000,1)


blackOutline = LineStyle(1,black) #pixels, color

redRectangle = RectangleAsset(100000,100000,blackOutline,color) #Width, height, outline, fill.

text = TextAsset(name,fill=black, style='bold 40pt Times')

Sprite(redRectangle)
Sprite(text, (300,300))
App().run()




