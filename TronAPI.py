import requests
from bitcoin.base58 import *


endpoint          = 'https://api.trongrid.io'
solidity_node     = 'walletsolidity'
solidity_node_ext = 'walletextension'
full_node         = 'wallet'


def getbalance(address):
    hexstring = base58tohexstring(address)
    response = requests.get(endpoint + '/' + solidity_node + '/' +
                            "getaccount", params = {"address" : hexstring})
    return response.json()["balance"]

def gettransactions(address):
    hexstring = base58tohexstring(address)
    response = requests.get(endpoint + '/' + solidity_node_ext + '/' +
                            "gettransactionsfromthis", params = {"account" : {"address" : "41E552F6487585C2B58BC2C9BB4492BC1F17132CD0"}, "offset": 0, "limit": 10})
    print(response.text)


def base58tohexstring(address):
    return decode(address).hex()[:-8]