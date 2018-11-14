
def login(username, password):

    searched = searchfile("/localdata/users.txt", username, password)
    if (searched):
        return searched

    register()



def searchfile(file, username, password):
    '''

    :param file:
    :return:
    '''

    desiredstring = username + password

    with open(file) as userfile:
        for line in userfile:
            pass

    return False


def register():