import requests
from bitcoin.base58 import *


endpoint      = 'https://api.trongrid.io'
solidity_node = 'walletsolidity'
full_node     = 'wallet'


def getbalance(address):
    hexstring = base58tohexstring(address)
    response = requests.get(endpoint + '/' + solidity_node + '/' + "getaccount", params = {"address" : hexstring})
    return response.json()["balance"]


def base58tohexstring(address):
    return decode(address).hex()[:-8]