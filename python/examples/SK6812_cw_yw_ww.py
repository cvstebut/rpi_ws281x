# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import signal
import sys
import time

from neopixel import *

# LED strip configuration:
LED_COUNT      = 30      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 5     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0
LED_STRIP      = ws.WS2811_STRIP_RGB
#LED_STRIP      = ws.SK6812_STRIP_RGBW
#LED_STRIP      = ws.SK6812W_STRIP


# graceful handling of ctrl-c
def signal_handler(sig, frame):
	print ('You pressed Ctrl-C')
	sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/1000.0)


# Main program logic follows:
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	# Intialize the library (must be called once before other functions).
	strip.begin()

	displaypause = 4.000

	print ('Press Ctrl-C to quit.')

	try:

		while True:
			# Color wipe animations.
			print('yellow white')
			colorWipe(strip, Color(0, 255, 0), 0)  # yellow white
			time.sleep(displaypause)
			print('cold white')
			colorWipe(strip, Color(255, 0, 0), 0)  # cold white
			time.sleep(displaypause)
			print('warm white')
			colorWipe(strip, Color(0, 0, 255), 0)  # warm white
			time.sleep(displaypause)

			print('test white - 2')
			colorWipe(strip, Color(0, 0, 255), 255)  # Red wipe
			time.sleep(displaypause)



	finally:
		print ("done - black- cvs")
		colorWipe(strip, Color(0, 0, 0), 0)  # turn off strip
		