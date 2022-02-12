from machine import Pin, SoftSPI
import max7219
from heximg import drawimg
spi = SoftSPI(baudrate=800000, polarity=1, phase=0, sck=Pin(2), mosi=Pin(3), miso=Pin(10))
screen = max7219.Matrix8x8(spi, Pin(7), 4)
screen.fill(0)
drawimg(screen.pixel,0,0,8,8,[
    0x3c,0x42,0x95,0x95,
    0xa1,0x9d,0x42,0x3c])
screen.show()