#!/usr/bin/env python

class SplashScreen:
    def __init__(self, g, width = 32, height = 32):
        self.gui = g
        self.width = width
        self.height = height

    def draw(self):
        self.gui.set_pixel(             0,               0, (255, 255, 255))
        self.gui.set_pixel(             0, self.height - 1, (  0,   0, 255))
        self.gui.set_pixel(self.width - 1,               0, (255,   0,   0))
        self.gui.set_pixel(self.width - 1, self.height - 1, (  0, 255,   0))

        for i in range(0, int(min(self.width, self.height) / 3)):
            self.gui.set_pixel((self.width / 2) - 1 + i, (self.height / 2) - 1 + i, (255, 255, 255))
            self.gui.set_pixel((self.width / 2) - 1 - i, (self.height / 2) - 1 - i, (255, 255, 255))
            self.gui.set_pixel((self.width / 2) - 1 + i, (self.height / 2) - 1 - i, (255, 255, 255))
            self.gui.set_pixel((self.width / 2) - 1 - i, (self.height / 2) - 1 + i, (255, 255, 255))

    def finished(self):
        return True

    def restart(self):
        pass

if __name__ == "__main__":
    from test import TestGUI
    t = TestGUI()
    s = SplashScreen(t)
    s.draw()
    t.debug_loop(s.draw)
