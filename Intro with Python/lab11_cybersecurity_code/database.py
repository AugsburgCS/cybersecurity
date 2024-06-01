# These functions are the ADVANCED requirements

filename = 'users.txt'

def load_users():
    '''
    Create and return a database of username/password based on the file contents.
    The password is the encrypted password.
    '''
    
    global filename

    # place file contents into a list.
    # each list element corresponds to 1 line in the file
    f = open(filename,'r')
    text = f.read().splitlines()
    f.close()

    # place user(key) - password(value) pairs in a dictionary
    users_db = {}
    for line in text:
        user = line.split()[0]
        password = line.split()[1]
        users_db[user] = password

    return users_db
        

def write_users():
    '''
    Take the contents of the dictionary and write it to the file.
    Use 'w' when opening the file to overwrite the contents.
    Separate the username and encrypted password with a space character.
    '''
    
    global filename
    pass

def add_account():
    '''
    Get a username from the user:
        Make sure it is 8 to 10 characters long.
        Make sure it is unique (i.e. not already in the dictionary)
        Continually ask until these criteria are met
    Get a password from the user:
        Make sure it is 6 to 15 characters long.
        Continually ask until these criteria are met
    Add the username and password to the dictionary.
    Write the dictionary to the file.
    '''
    pass

# keep this here outside the if-statement
# it creates the database that is used in other files
users_db = load_users()


