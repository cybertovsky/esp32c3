from machine import Pin,I2C
from ssd1306 import SSD1306_I2C
print("hello")
i2c = I2C(sda=Pin(4), scl=Pin(5))
display = SSD1306_I2C(128, 32, i2c)

#display.text('Hello, World!', 0, 0, 1)
display.contrast(1)  # bright


text='''
000000011000000000001100011000000001100001100000000000001111000000000000000000000,
001111111111110000001100011000000001100001100000001111111111100000000000000000000,
001111111111110011111111111111100001101111111100001111100000000000000000000000000,
000000011000000011111111111111100001101111111100001100000000000000000000000000000,
000111111111100000001100011000000101110001101100001100011000000000000000000000000,
000000110000000000000000000000000101110001101100011000011000000000000000000000000,
011111111111111001111111111111001101100001101100011111111111100000000000000000000,
011111111111111001111111111111001001101111111110011111111111100000000000000000000,
000110000011000000000110000011000001101111111110000000011000000000000000000000000,
011111111111110000000110000011000001100001100000000010011010000000000000000000000,
011011000011011000000110000011000001100011110000000110011011000000110000000000000,
000011111111000000000110001111000001100110011000001100011001100000110000000000000,
000011000011000000000110001110000001101100001100011000011000110000010000000000000,
000011111111000000000110000000000001111000000110000001111000010000100000000000000,
000011111111000000000110000000000001100000000000000000110000000000000000000000000,
000000000000000000000000000000000000000000000000000000000000000000000000000000000,
000000000000000000000000000000000000000000000000000000000000000000000000000000000,
000000110000000000000011000000000000000110000000000000000110110000000000000000000,
000000111111100000000011111110000011000110000000000000000110010000000000000000000,
000000110000000000000011000000000011000110000000011111111111111000011000000000000,
011111111111110001111111111111000011000110000000011111111111111000011000000000000,
011111111111110001111111111111000111111111111000011000000110000000011000000000000,
011000110000110001100011000011000111111111111000011011110110110000011000000000000,
011011111110000001101111111000001100000110000000011011110110110000011000000000000,
011000110001100001100011000110000000000110000000011001000110110000011000000000000,
011000111111100001100011111110000001111111110000011111111110110000011000000000000,
011000000000000001100000000000000001111111110000011010011011100000000000000000000,
011001111110000001100111111000000000000110000000011011110011000000000000000000000,
011001111110000001100111111000000000000110000000011001100011000000011000000000000,
011001100110011001100110011001100000000110000000010011110111101000011000000000000,
110001100111111011000110011111101111111111111110110110001100111000000000000000000,
010111000011110001011100001111001111111111111110100000011000011000000000000000000
'''

def FixPos(pos):
    x,y=pos
    return x,y

def draw_img(img,pos,scale=1):
    start_x,start_y=FixPos(pos)
    lines = img.split(',')
    for line in lines:
        x=0
        for pixel in line:
            if pixel == '1':
                display.rect(start_x+x,start_y,scale,scale,1)
            x+=1*scale
        start_y+=1*scale

draw_img(text,(0,0),1)

display.show()