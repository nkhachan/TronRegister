import requests
from Transaction import *
from bitcoin.base58 import *

gridendpoint      = 'https://api.trongrid.io'
scanendpoint      = 'https://api.tronscan.org'
solidity_node     = 'walletsolidity'
solidity_node_ext = 'walletextension'
full_node         = 'wallet'
api               = 'api'


def getbalance(address):
    hexstring = base58tohexstring(address)
    response = requests.get(gridendpoint + '/' + solidity_node + '/' +
                            "getaccount", params = {"address" : hexstring})
    return response.json()["balance"]


def gettransactions(address):
    '''

        GetTransaction API has following elements in each transaction :

                {
                  "hash": "string",
                  "block": 0,
                  "timestamp": "2018-11-13T20:48:28.782Z",
                  "confirmed": true,
                  "ownerAddress": "string",
                  "toAddress": "string",
                  "contractData": {
                    "boolean": true,
                    "number": true,
                    "string": true,
                    "object": true,
                    "array": true,
                    "null": true
                  },
                  "contractType": 0,
                  "data": "string"
                }

    '''
    response = requests.get(scanendpoint + '/' + api + '/' +
                            "transaction", params = {"address" : address})
    return response.json()["data"]


def gettransfers(address):
    '''

        GetTransfer API has following elements in each transaction :

            {
              "id": "string",
              "transactionHash": "string",
              "block": 0,
              "timestamp": "2018-11-13T22:22:34.141Z",
              "transferFromAddress": "string",
              "transferToAddress": "string",
              "amount": 0,
              "tokenName": "string",
              "confirmed": true
            }


    '''
    response = requests.get(scanendpoint + '/' + api + '/' +
                            "transfer", params = {"address" : address})
    return response.json()["data"]


def getlasttransfer(address):
    response = requests.get(scanendpoint + '/' + api + '/' +
                            "transfer", params = {"address" : address, "limit" : 1})
    return response.json()["data"]

def getlasttransactionobject(address):
    return Transaction(getlasttransfer(address)[0])


def gettransactionobjects(address):
    transactions = []
    for transaction in gettransfers(address):
        transactions.append(Transaction(transaction))
    return transactions


def printtransfers(address):
    for transfer in gettransfers(address):
        print(Transaction(transfer))




def formatBalance(balance):
    return float(str(balance)[:-4])/100


def base58tohexstring(address):
    return decode(address).hex()[:-8]