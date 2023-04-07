# alphabet list
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# function for catching errors
def catch_errors(text_input):
    if text_input.isnumeric() or text_input.islower() or not text_input.isalpha():
        print('Error: You need to put uppercase letters only! Try to run the program again.')
        quit()
# input variable for the message
message = input('Message (only uppercase letters and no spaces): ')
# function init
catch_errors(message)
# input variable for the key
key = input('Key (all capital letters and no spaces): ')
# function init for key var.
catch_errors(key)
# placeholder variables for the mod value and encrypted message
encrypted_message = ''
mod = 0
# while loop to correspond key chars. with message chars.
while len(key) < len(message):
    key += key
# remove extra chars. of key before adding the values of chars. of message var.
if len(key) > len(message):
    key = key[:((len(message)))]
# for loop
for i in range(len(message)): 
    message_index = alphabet.index(message[i]) #19
    for j in range(len(key)): 
        key_index = alphabet.index(key[i])
    mod = message_index + key_index
    if mod >= 26:
        mod -= 26
    encrypted_message += alphabet[mod]

#execution
print('\033[32m~' * (19 + len(encrypted_message)) + '\033[0m')
print('Encrypted message: \033[33m' + encrypted_message + '\033[0m')
print('\033[32m~' * (19 + len(encrypted_message)) + '\033[0m')