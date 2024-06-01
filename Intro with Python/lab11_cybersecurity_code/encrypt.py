# BASE LEVEL for Cybersecurity Lab 11
import conversions
import database

# test salter that was randomly generated
salter = [11, 32, 17, 25, 9, 25, 2, 20, 5, 13, 18, 6, 22, 14, 33, 35]

def salt(password):
    '''
    Duplicate and concatenate the password up to 16 characters.
    For example: password happyDay! would become happyDay!happyDa
    For example: password smile@ would become smile@smile@smil
    
    "Add" the salter to the password. Each character in the password is
    "shifted" as many characters as indicated in the corresponding salter
    then converted back to a character.
    For example: chr(ord(password[0]) + salter[0])
    
    EXCEPT make sure that all chars fall between [ and ~ (ASCII 33 to 126)
    For example: ord('|') = 124, shift=9. 124+9=133, and
        since >126, chr(133%126 + 33)

    RETURN the salted password (a string of characters between [ and ~ )
    '''

    # use the salter defined in the global scope of this file
    global salter



def create_bitstream(password,encodings):
    '''
    Convert each character of the password to its corresponing bitstream
    as defined in the encodings dictionary.
    For example, if password[0] = 'a' then add encodings['a'] to the bitstream.

    RETURN the bitstream (a string of 0s and 1s)
    '''
    pass


def hexify(bitstream):
    '''
    Convert the bitstream to a hex stream.
    Take every 4 bits and convert them to the corresponding hex value.
    For example, bitstream 001111110100 would be converted to '3F4'

    RETURN the hex string
    '''
    pass

def asciify(hexstring):
    '''
    Convert the series of hex digits to the corresponding ASCII
    '''
	pass
        

def encrypt(password):
    '''
    Use above functions to encrypt password.
    Salt it.
    Bitstream it.
    Flip it.
    Hexify it.

    RETURN the final hex string
    '''
	pass



