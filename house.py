#Christo Dragnev
#2/8/18
#house.py

from ggame import *

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black)

redRectangle = RectangleAsset(300,200,blackOutline,red)

Sprite(redRectangle)

App().run()

