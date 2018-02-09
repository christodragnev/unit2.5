#Christo Dragnev
#2/8/18
#graphicDemo.py

from ggame import *

color = input('Enter Color Code: ')

red = Color(0xFF0000,1) #this is the color red
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black)
redOutline = LineStyle(1,red)

redRectangle = RectangleAsset(1000,600,redOutline,red) #width, height, outline, fill

Sprite(redRectangle)

App().run()