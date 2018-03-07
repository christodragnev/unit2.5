#Christo Dragnev
#3/7/18
#yield.py

from ggame import *

yellow = Color(0xFFFF00,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black)
text = TextAsset('YIELD',fill=black, style='bold 21pt Times')

yellowTriangle = PolygonAsset([(50,50), (200,50), (125,175)], blackOutline, yellow)

Sprite(yellowTriangle)
Sprite(text,(30,25))

App().run()


