import json

def login(username, password):
    return searchfile("localdata/users.txt", username, password)


def searchfile(file, username, password):
    '''

    :param file:
    :return:
    '''

    with open(file) as file:
        data = json.loads(file.read())
    if ((username in data.keys()) and (data[username] == password)):
        return True
    return False

def register(username, password, address):
    with open("localdata/users.txt") as file:
        data = json.loads(file.read())
    data[username] = password