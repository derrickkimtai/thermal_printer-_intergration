from escpos.printer import Usb
from datetime import datetime

printer = Usb(0x0fe6, 0x811e, in_ep=0x82, out_ep=0x01)

printer.text("Hello World\n")
title = "Receipt: The Olmismis FCS"
date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
farmer_name = "John Doe"
farmer_number = "123456"

# Print the receipt
printer.set('center')  # Center align the text
printer.text(f"{title}\n")
printer.text(f"Date and Time: {date_time}\n")
printer.text(f"Farmer Name: {farmer_name}\n")
printer.text(f"Farmer Number: {farmer_number}\n")
printer.cut()