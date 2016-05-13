#!/usr/bin/python


from p_thermal.Adafruit_Thermal import *


def printer_test():
    printer = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)
    printer.upsideDownOn()

    text = "Brair rabbit went to the briar patch and hooboy it was prickly"
    printer.println(text)
    printer.feed(7)

    printer.upsideDownOff()
    printer.println(text)
    printer.feed(7)


if __name__ == '__main__':
    printer_test()