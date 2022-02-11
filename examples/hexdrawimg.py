from machine import Pin, SoftSPI
import max7219
from heximg import drawimg
spi = SoftSPI(baudrate=800000, polarity=1, phase=0, sck=Pin(2), mosi=Pin(3), miso=Pin(10))
screen = max7219.Matrix8x8(spi, Pin(7), 4)
drawimg(screen.pixel,0,0,3,3,[0x02,0x05,0x02])