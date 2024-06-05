from time import sleep
import board
import neopixel

pixel_pin = board.D10
num_pixels = 4
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.8, auto_write=False, pixel_order=neopixel.GRB)

pixels.fill((255, 0, 0))
pixels.show()
sleep(10)

pixels[0] = (255, 0, 0)
pixels[1] = (0, 255, 0)
pixels[2] = (0, 0, 255)
pixels[3] = (255, 255, 255)

pixels.show()
sleep(10)