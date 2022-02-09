from machine import Pin, SPI
from lib import max7219
from time import sleep
spi = SPI(1, baudrate=10000000)
screen = max7219.Matrix8x8(spi, Pin(15), 1)

screen.brightness(0)
#screen.text('0',0,0,1)
#screen.scroll(-4,0)

class Sprite:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def update(self):
        if self.x < 7:
            self.x=self.x+1
            
    def draw(self):
        screen.pixel(self.x,self.y,1)

sprite = Sprite(0,0)

def update():
    sprite.update()

def draw():
    sprite.draw()

while True:
    sleep(1)
    screen.fill(0)
    update()
    draw()
    screen.show()
    