import adafruit_thermal_printer
import serial
from Bill import bill

def printOutFinalBill():

    ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.67)
    uart = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=3000)
    printer = ThermalPrinter(uart)
    printer.warm_up()

    printer.size = adafruit_thermal_printer.SIZE_LARGE
    printer.justify = adafruit_thermal_printer.JUSTIFY_CENTER
    printer.underline = adafruit_thermal_printer.UNDERLINE_THICK

    printer.print('Garam Market!')

    printer.underline = None
    printer.size = adafruit_thermal_printer.SIZE_SMALL
    printer.justify = adafruit_thermal_printer.JUSTIFY_CENTER
    printer.underline = adafruit_thermal_printer.UNDERLINE_THICK
    printer.print('9700 Gilman Dr')
    printer.print('La Jolla, CA, 92093')

    printer.feed(2)

    printer.print(' Product   Price    Amount   Total')
    # printer.underline = adafruit_thermal_printer.UNDERLINE_THICK
    printer.print('-------------------------------')
    printer.justify = adafruit_thermal_printer.JUSTIFY_CENTER
    for item in bill.items:
        printer.print(item.name + "   " + item.price + "  " + item.quantity + "  " + item.price*item.quantity)
    printer.print('-------------------------------')

    printer.bold = True
    printer.justify = adafruit_thermal_printer.JUSTIFY_CENTER
    printer.print('Total: ')
    printer.bold = False

    printer.justify = adafruit_thermal_printer.JUSTIFY_RIGHT
    printer.print(bill.sum)

    printer.feed(2)

# QR Code