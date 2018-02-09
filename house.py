#Christo Dragnev
#2/8/18
#house.py

from ggame import *

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black)


blueTriangle = PolygonAsset([(0,100), (75,0), (150,100)], blackOutline, blue) #endpoints,
redRectangle = RectangleAsset(150,100,blackOutline,red)
redRectangle1 = RectangleAsset(25,50,blackOutline,red)

Sprite(redRectangle,(100,100))
Sprite(blueTriangle,(100,0))
Sprite(redRectangle1,(160,150))
App().run()

