#Christo Dragnev
#3/7/18
#olympics.py

red = Color(0xFF0000,1) #this is the color red
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)
yellow = Color(0xFFFF00,1)

blueCircle = CircleAsset(50,blackOutline,blue) #radius, outline, full
blackCircle = CircleAsset(50,blackOutline,black) #radius, outline, full
redCircle = CircleAsset(50,blackOutline,red) #radius, outline, full
yellowCircle = CircleAsset(50,blackOutline,yellow) #radius, outline, full
greenCircle = CircleAsset(50,blackOutline,green) #radius, outline, full

Sprite(blueCircle,(50,50))
Sprite(blackCircle,(100,50))
Sprite(redCircle,(150,50))
Sprite(yellowCircle,(75,75))
Sprite(greenCircle,(125,75))

App().run()

