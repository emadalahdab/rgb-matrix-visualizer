#!/usr/bin/env python3

# Uses the Python bindings for the Raspberry Pi RGB LED Matrix library:
# https://github.com/hzeller/rpi-rgb-led-matrix
#
# And the pillow Python Imaging Library:
# https://github.com/python-pillow/Pillow
#
# For the wiring of multiple panels, check out:
# https://github.com/hzeller/rpi-rgb-led-matrix/blob/master/wiring.md#chains
#
# Basically each chain only stretches in the X-direction.
# For the Y-direction, multiple parallel chains are used.
# Up to 3 are theoretically possible with the Pi, but my hardware only supports
# one.
#
# The physical layout of the chained panels can be different of course.
# For four panels, you could do 64x64 or 32x128.
# But this PiMatrix object will always present it as 128x32,
# chained in the X-direction.
#
# Use the objects from mapper.py to adjust this.
#
# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# <xythobuz@xythobuz.de> wrote this file.  As long as you retain this notice
# you can do whatever you want with this stuff. If we meet some day, and you
# think this stuff is worth it, you can buy me a beer in return.   Thomas Buck
# ----------------------------------------------------------------------------

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image

class PiMatrix:
    def __init__(self, w = 64 * 1, h = 32* 2, panelW = 64, panelH = 32):
        self.width = w # x-axis
        self.height = h # y-axis

        self.panelW = panelW # x-axis
        self.panelH = panelH # y-axis

        # compatibility to TestGUI
        self.multiplier = 1.0

        options = RGBMatrixOptions()

        options.cols = 64  #self.panelW # x-axis
        options.rows = 32 #self.panelH # y-axis

        options.chain_length = 1 #int(self.width / options.cols) # x-axis
        options.parallel = 2 #int(self.height / options.rows) # y-axis

        #options.row_address_type = 0
        #options.multiplexing = 0
        #options.pwm_bits = 11
        options.brightness = 100
        #options.pwm_lsb_nanoseconds = 130
        #options.led_rgb_sequence = 'RGB'
        options.hardware_mapping = 'regular'  # If you have an Adafruit HAT: 'adafruit-hat'
        options.gpio_slowdown = 2
        #options.pixel_mapper_config = "Rotate:270"

        # newer Pimoroni 32x32 panels require this setting for additional
        # initialization of the shift-registers on there.
        # fortunately this also works for the older type of panels.
        #options.panel_type = "FM6126A"

        self.matrix = RGBMatrix(options = options)

        self.loop_start() # initialize with blank image for ScrollText constructor

    def exit(self):
        pass

    def loop_start(self):
        self.image = Image.new('RGB', (self.width, self.height))
        return False # no input, never quit on our own

    def loop_end(self):
        self.matrix.SetImage(self.image.convert('RGB'))

    def set_pixel(self, x, y, color):
        if (x < 0) or (y < 0) or (x >= self.width) or (y >= self.height):
            return

        self.image.putpixel((int(x), int(y)), color)

if __name__ == "__main__":
    import util

    t = PiMatrix()
    util.loop(t, lambda: t.set_pixel(15, 15, (255, 255, 255)))
