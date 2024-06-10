from escpos.printer import Usb

printer = Usb(0x0483, 0x5743, in_ep=0x81, out_ep=0x02)
printer.text("Hello World\n")
printer.cut()