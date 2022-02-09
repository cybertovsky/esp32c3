from machine import Pin, SoftSPI
from st7789 import ST7789,color565

def TFTColor(r,g,b) :
  '''Create a 16 bit rgb value from the given R,G,B from 0-255.
     This assumes rgb 565 layout and will be incorrect for bgr.'''
  return ((b & 0xF8) << 8) | ((g & 0xFC) << 3) | (r >> 3)

def FixPos(pos):
    x,y=pos
    return x,y+24

spi = SoftSPI(baudrate=800000, polarity=1, phase=0, sck=Pin(2), mosi=Pin(3), miso=Pin(10))
spi.write(b"12345678")
print(spi.read(8, 0x42))
tft=ST7789(spi,320,240,reset=Pin(11),dc=Pin(5),cs=Pin(7)) #DC, Reset, CS
#tft=ST7789(spi,320,240,reset=Pin(11),dc=Pin(6)) 
tft.fill(color565(255,255,255))