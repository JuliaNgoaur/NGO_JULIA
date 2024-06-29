#!/usr/bin/env python
# coding: utf-8

# In[40]:


def bin_to_dec(binary_string):
    output = 0
    power = len(binary_string) - 1
    counter = 0
    
    while counter != len(binary_string):
        output += int(binary_string[counter]) * (2 ** (power - counter))
        counter += 1
    return output

bin_to_dec("1000")


# In[42]:


def dec_to_bin(number):
    output = ""
    
    if number == 0:
        return "0"
        
    while number > 0:
        remainder = number % 2
        output = str(remainder) + output
        number = number // 2
    
    return output

dec_to_bin(12)


# In[91]:


encoder_dict = {
        " ":"0",
        "A":"2",
        "B":"22",
        "C":"222",
        "D":"3",
        "E":"33",
        "F":"333",
        "G":"4",
        "H":"44",
        "I":"444",
        "J":"5",
        "K":"55",
        "L":"555",
        "M":"6",
        "N":"66",
        "O":"666",
        "P":"7",
        "Q":"77",
        "R":"777",
        "S":"7777",
        "T":"8",
        "U":"88",
        "V":"888",
        "W":"9",
        "X":"99",
        "Y":"999",
        "Z":"9999"
    }
def telephone_cipher(message):

    ALPHA = list(encoder_dict.keys())
    NUM = list(encoder_dict.values())
    output = ""
    counter = 0
    
    while counter != len(message):
        if counter > 0 and encoder_dict[message[counter]][0] == encoder_dict[message[counter-1]][0]:
            output += "_"
        output += str(NUM[ALPHA.index(message[counter])])
        counter += 1
        
    return output
    
telephone_cipher("XFABR")


# In[148]:


decipher_dict = {
        "0":" ",
        '2': 'A',
        '22': 'B',
        '222': 'C',
        '3': 'D',
        '33': 'E',
        '333': 'F',
        '4': 'G',
        '44': 'H',
        '444': 'I',
        '5': 'J',
        '55': 'K',
        '555': 'L',
        '6': 'M',
        '66': 'N',
        '666': 'O',
        '7': 'P',
        '77': 'Q',
        '777': 'R',
        '7777': 'S',
        '8': 'T',
        '88': 'U',
        '888': 'V',
        '9': 'W',
        '99': 'X',
        '999': 'Y',
        '9999': 'Z'
    }
def telephone_decipher(telephone_string):

    counter = 0
    character = ""
    output = ""

    while counter < len(telephone_string):
        if telephone_string[counter] == '_':
            counter += 1
            continue
        
        character = telephone_string[counter]
        next_counter = counter + 1
        
        while next_counter < len(telephone_string) and telephone_string[next_counter] == telephone_string[counter]:
            character += telephone_string[next_counter]
            next_counter += 1
        
        output += decipher_dict[character]
        counter = next_counter
    
    return output
    
telephone_decipher("993332_22777")

