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


def test_print_modes():
    printer = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)

    import itertools
    # nums = ["".join(seq) for seq in itertools.product("01", repeat=6)]
    # nums = [str(x) for x in nums]
    # nums = filter(lambda x: x.count('1') == 1, nums)
    # nums = [int(x, 2) for x in nums]
    # nums.sort()


    printer.writeBytes(27, 123, 1)
    text = "TEST: Brair rabbit went to the briar patch and hooboy it was prickly"
    r_text = printer.textWrapped(text)
    print r_text
    printer.writePrintMode()
    printer.println(text)
    printer.feed(7)



if __name__ == '__main__':
    # printer_test()
    test_print_modes()


    # text = "TEST: Brair rabbit went to the briar patch and hooboy it was prickly"
    # r_text = textWrapped(text)



    # import itertools
    # nums = ["".join(seq) for seq in itertools.product("01", repeat=6)]
    # nums = [str(x) for x in nums]
    # nums = filter(lambda x: x.count('1') == 1, nums)
    # # nums = [int(x, 2) for x in nums]
    # nums.sort()
    #
    # for num in nums:
    #     print num