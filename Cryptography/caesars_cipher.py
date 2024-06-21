#We will try to start using function definitions in order to create this code

def caesar(message, key_shift, direction):
    #First we will define an alphabet, we'll use english alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    #we will need to store the final message
    final_message = ''

    #now, we will need to find the position in which a character from our message is in our alphabet, we'll use built in methods

    for character in message.lower(): #lower method is used because our alphabet is in lower case letters, so we need to compare the message
        #as such.

        #if any character in the message is not a character, it must be added without changes, to ensure message integrity
        if not character.isalpha():
            final_message += character 
        #now let us do the substitution    
        else:
            current_letter_index = alphabet.find(character) #current character position in our alphabet
            new_letter_index = (current_letter_index + key_shift*direction) % len(alphabet) #position substitution modulo the size of alphabet
            final_message += alphabet[new_letter_index] 
    return final_message

#now let us do an encryption and decryption functions

def encryption(message, key_shift):
    return caesar(message, key_shift,1)

def decryption(message, key_shit):
    return caesar(message, key_shit, -1)
