#Christo Dragnev
#2/8/18
#graphicDemo.py

from ggame import *

red = Color(0xFF0000,1) #this is the color red
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black)

redRectangle = RectangleAsset(200,100,blackOutline,red) #width, height, outline, fill
blueCircle = CircleAsset(50,blackOutline,blue) #radius, outline, full
greenEllipse = EllipseAsset(100,50,blackOutline,green) #wdth, height, outline, fill
blackLine = LineAsset(50,160,blackOutline) #x_endpoint, y_endpoint, lineStyle
redTriangle = PolygonAsset([(0,0), (120,180), (60,300)], blackOutline, red) #endpoints,
text = TextAsset('Smeds',fill=black, style='bold 40pt Times') #test, other options

Sprite(redRectangle)
Sprite(blueCircle,(50,50))
Sprite(greenEllipse,(200,200))
Sprite(blackLine)
Sprite(redTriangle)
Sprite(text,(300,200))
App().run()
