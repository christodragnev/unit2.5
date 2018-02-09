#Christo Dragnev
#2/9/18
#germany.py

from ggame import *

red = Color(0xFF0000,1)
yellow = Color(0xFFFF00,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black)
redOutline = LineStyle(1,red)
yellowOutline = LineStyle(1,yellow)

blackRectangle = RectangleAsset(200,50,blackOutline,black) #width, height, outline, fill
redRectangle = RectangleAsset(200,50,redOutline,red) #width, height, outline, fill
yellowRectangle = RectangleAsset(200,50,yellowOutline,yellow) #width, height, outline, fill

Sprite(blackRectangle)
Sprite(redRectangle,(0,50))
Sprite(yellowRectangle,(0,100))

App().run()
