from machine import Pin, SoftSPI
from st7735 import TFT

def TFTColor(r,g,b) :
  '''Create a 16 bit rgb value from the given R,G,B from 0-255.
     This assumes rgb 565 layout and will be incorrect for bgr.'''
  return ((b & 0xF8) << 8) | ((g & 0xFC) << 3) | (r >> 3)

def FixPos(pos):
    x,y=pos
    return x,y+24

spi = SoftSPI(baudrate=800000, polarity=1, phase=0, sck=Pin(2), mosi=Pin(3), miso=Pin(10))
tft=TFT(spi,6,10,7) #DC, Reset, CS
tft.initr()
tft.rgb(True)
tft.rotation(1)

# tft.pixel((10,10),RED)
b=TFTColor(89,170,250)
tft.fill(b)

#hero = Hero(FixPos((10,0)),(20,20),TFTColor(0,255,0),tft)    

#hero.draw()
# color 0-65535 gen:TFTColor

y=TFTColor(255,255,0)
o=TFTColor(255,128,0)
w=TFTColor(255,255,255)
r=TFTColor(255,0,0)
g=TFTColor(244,244,244)
img = [
    [0,0,0,0,0,0,9,9,9,9,9,9,0,0,0,0,0],
    [0,0,0,0,9,9,w,w,w,9,w,w,9,0,0,0,0],
    [0,0,0,9,w,w,y,y,9,w,w,w,w,9,0,0,0],
    [0,0,9,w,y,y,y,y,9,g,w,w,9,w,9,0,0],
    [0,9,y,y,y,y,y,y,9,g,w,w,9,w,9,0,0],
    [0,9,9,9,9,9,y,y,y,9,g,w,w,w,9,0,0],
    [9,w,w,w,w,w,9,y,y,y,9,9,9,9,9,9,0],
    [9,y,w,w,w,y,9,y,y,9,r,r,r,r,r,r,9],
    [0,9,9,9,9,9,o,o,9,r,9,9,9,9,9,9,0],
    [0,0,9,o,o,o,o,o,o,9,9,r,r,r,r,9,0],
    [0,0,0,9,9,o,o,o,o,o,9,9,9,9,9,0,0],
    [0,0,0,0,0,9,9,9,9,9,0,0,0,0,0,0,0],
]

def draw_img(img,pos,scale=1):
    start_x,start_y=FixPos(pos)
    for line in img:
        x=0
        for pixel in line:
            #tft.pixel((start_x+x,start_y),pixel)
            if pixel > 0:
                tft.fillrect((start_x+x,start_y),(scale,scale),pixel)
            x+=1*scale
        start_y+=1*scale

draw_img(img,(10,10),5)
