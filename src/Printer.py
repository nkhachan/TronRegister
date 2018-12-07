from Bill import bill
from CoinMarketCap import *

import serial
import subprocess


def printOutFinalBill():

    script = ["python2.7", "PrintQRCode.py", bill]
    process = subprocess.Popen(" ".join(script),
                               shell=True,
                               env={"PYTHONPATH": "."})