#!/usr/bin/env python
# coding: utf-8

# In[156]:


def shift_letter(letter, shift):
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"] 
    if letter == " ":
        return " "
    else:
        ALPHA = alphabet.index(letter)
        shifted_number = ALPHA + shift
        shifted_letter = shifted_number%26
    return alphabet[shifted_letter]

shift_letter("Z", 2)


# In[1]:


def caesar_cipher(message, shift):
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"] 
    output = ""
    for x in message:
        if x == " ":
            output += x
        else:
            ALPHA = alphabet.index(x)
            shifted_number = ALPHA + shift
            shifted_letter = shifted_number%26
            output += alphabet[shifted_letter]
    return output


# In[ ]:


def shift_by_letter(letter, letter_shift):
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"] 
    if letter == " ":
        return " "
    else:
        ALPHA = alphabet.index(letter)
        BETA = alphabet.index(letter_shift)
        shifted_number = ALPHA + BETA
        shifted_letter = shifted_number%26
    return alphabet[shifted_letter]


# In[343]:


def vigenere_cipher(message, key):
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"] 
    output = ""
    new_key = (len(message)//len(key) + 1) * key
    
    for x in range(len(message)):
        if message[x] == " ":
            output += " "
        else:
            message_position = alphabet.index(message[x])
            key_position = alphabet.index(new_key[x])
            shifted_number = message_position + key_position
            shifted_letter = shifted_number%26 
            
            output += alphabet[shifted_letter]
            
    return output


# In[308]:


def scytale_cipher(message, shift):
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"] 
    output = ""
    
    while len(message)%shift != 0:
        message += "_"
    for i in range(len(message)):
        message_letter = message[(i // shift) + (len(message) // shift) * (i % shift)]
        output += message_letter
        
    return output


# In[411]:


def scytale_decipher(message, shift):
    counter = 0
    output = ""
    while (shift*counter)/(shift) <= len(message)-1:
        output += message[(shift*counter)%len(message)+(shift*counter)//len(message)]
        counter += 1
        
    return output

