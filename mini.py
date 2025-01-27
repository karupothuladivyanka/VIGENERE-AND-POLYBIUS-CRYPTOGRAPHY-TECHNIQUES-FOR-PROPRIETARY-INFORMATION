def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))
     
# This function returns the 
# encrypted text generated 
# with the help of the key
def cipherText(string, key):
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) +
             ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return("" . join(cipher_text))
     
# This function decrypts the 
# encrypted text and returns 
# the original text
def originalText(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) -
             ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return("" . join(orig_text))
     
# Driver code
if _name_ == "_main_":
    string = input("Enter The String : ")
    keyword = input("Enter the keyword : ")
    key = generateKey(string, keyword)
    cipher_text = cipherText(string,key)
    print("Ciphertext :", cipher_text)
    print("Original/Decrypted Text :", 
           originalText(cipher_text, key))
    
# Python Program to implement polybius cipher

# function to display polybius cipher text
def polybiusCipher(S):

        # convert each character to its encrypted code
        for char in S:
            
                # finding row of the table
                row = int((ord(char) - ord('A')) / 5) + 1
        
                # finding column of the table 
                col = ((ord(char) - ord('A')) % 5) + 1

                # if character is 'K'
                if char == 'k':
                        row = row - 1
                        col = 5 - col + 1
                        
                # if character is greater than 'j'
                elif ord(char) >= ord('J'):
                        if col == 1 :
                            col = 6
                            row = row - 1
                            
                        col = col - 1
                        
                print(row, col, end ='', sep ='')

# Driver's Code
if _name_ == "_main_":

        S = input("Enter the String : ")

        # print the cipher of "geeksforgeeks"
        polybiusCipher(S)