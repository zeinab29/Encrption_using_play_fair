
# remove duplicate letters and litter J from key.
from pydoc import plain
from re import X
import string
from unittest import result
from xml.etree.ElementTree import tostring


def prepare_key(key):
    simpleKeyArr = []
    for c in key:
        if c not in simpleKeyArr:
            if c == 'J':
                simpleKeyArr.append('I')
            else:
                simpleKeyArr.append(c)
    return simpleKeyArr

# create key matrix for encryption and decryption.    
def generate_key_matrix(key): 
    simpleKeyArr = prepare_key(key) 
    matrix_5x5 = [[0 for i in range (5)] for j in range(5)]
    is_I_exist = "I" in simpleKeyArr #boolean if key has I
    # A-Z's ASCII Value lies between 65 to 90 
    for i in range(65,91):
        if chr(i) not in simpleKeyArr:
            if i==73 and not is_I_exist:
                simpleKeyArr.append("I")
                is_I_exist = True
            elif i==73 or i==74 and is_I_exist:  # I = 73  # J = 74
                pass
            else:
                simpleKeyArr.append(chr(i))

    index = 0
    for i in range(0,5):
        for j in range(0,5):
            matrix_5x5[i][j] = simpleKeyArr[index]
            index+=1

    return matrix_5x5

# get index of each character
def Char_index (char,cipherKeyMatrix):
    indexOfChar = []
    # convert the character value from J to I
    if char=="J":
        char = "I"

    for i,j in enumerate(cipherKeyMatrix):
        for k,l in enumerate(j):
            if char == l:
                indexOfChar.append(i) #add 1st dimension of 5X5 matrix => i.e., indexOfChar = [i]
                indexOfChar.append(k) #add 2nd dimension of 5X5 matrix => i.e., indexOfChar = [i,k]
                return indexOfChar

#loop over plain text
def seperate(plainText,key):
    result =""
    list_of_words = plainText.split(" ")
    for word in list_of_words:
        ready_word = prepare_text(word)
        word_encrypted = Playfair_cipher_encryption(ready_word,key)
        result = result +" "+word_encrypted
    return result

def delete_char(word,idx):
    new_str =""
    for i in range(len(word)):
        if i != idx:
            new_str = new_str + word[i]
    return new_str

def prepare_text_decryption(cipherText):
    i = 0
    while i < len(cipherText):
        if i!= 0 and i != len(cipherText)-1 and cipherText[i] == 'X':
            if cipherText[i-1] == cipherText[i+1]:
                cipherText = delete_char(cipherText,i)
                
        if i ==len(cipherText)-1 and cipherText[i] == 'Z':
            cipherText = delete_char(cipherText,i)
        i+=1
    return cipherText

#loop over plain text
def seperate_decryption(cipherText,key):
    result =""
    list_of_words = cipherText.split(" ")
    for word in list_of_words:
        word_decrypted = Playfair_cipher_decryption(word,key)
        ready_word = prepare_text_decryption(word_decrypted)
        result = result +" "+ready_word
    return result
#prepare plain text
def prepare_text(plaintext):
    i = 0
    preproccessed = ""
    while i < len(plaintext):
        a = plaintext[i]
        b = ''
        if (i + 1) == len(plaintext):
            b = 'Z'
            preproccessed = preproccessed + a
            preproccessed = preproccessed + b
            break;
        else :
            b = plaintext[i+1]
            if a != b:
                preproccessed = preproccessed + a
                preproccessed = preproccessed + b
                i += 2
            else :
                preproccessed = preproccessed + a
                preproccessed = preproccessed + "X"
                i += 1
    return preproccessed
            



# core of the algorithm
def Playfair_cipher_encryption (plainText,key):
    cipherText = ""
    # 1. Generate Key Matrix
    keyMatrix = generate_key_matrix(key)
    # 2. Encrypt According to Rules of playfair cipher
    i = 0
    while i < len(plainText)-1:
        # 2.1 calculate two grouped characters indexes from keyMatrix
        n1 = Char_index(plainText[i],keyMatrix) 
        n2 = Char_index(plainText[i+1],keyMatrix)

        #same column 
        if n1[1] == n2[1]:
            i1 = (n1[0] + 1) % 5
            j1 = n1[1]
            i2 = (n2[0] + 1) % 5
            j2 = n2[1]
            cipherText = cipherText+keyMatrix[i1][j1]
            cipherText = cipherText+keyMatrix[i2][j2]
            

        # same row
        elif n1[0]==n2[0]:
            i1= n1[0]
            j1= (n1[1] + 1) % 5
            i2= n2[0]
            j2= (n2[1] + 1) % 5
            cipherText = cipherText+keyMatrix[i1][j1]
            cipherText = cipherText+keyMatrix[i2][j2]
            

        else:
            i1 = n1[0]
            j1 = n1[1]
            i2 = n2[0]
            j2 = n2[1]

            cipherText = cipherText+keyMatrix[i1][j2]
            cipherText = cipherText+keyMatrix[i2][j1]
            
        i += 2  
    return cipherText

# decryption 
def Playfair_cipher_decryption (cipherText,key):
    plainText = ""
    # 1. Generate Key Matrix
    keyMatrix = generate_key_matrix(key)
    # 2. Encrypt According to Rules of playfair cipher
    i = 0
    while i < len(cipherText)-1:
        # 2.1 calculate two grouped characters indexes from keyMatrix
        n1 = Char_index(cipherText[i],keyMatrix) 
        n2 = Char_index(cipherText[i+1],keyMatrix)

        #same column 
        if n1[1] == n2[1]:
            i1 = (n1[0] + 4) % 5
            j1 = n1[1]
            i2 = (n2[0] + 4) % 5
            j2 = n2[1]
            plainText = plainText +keyMatrix[i1][j1]
            plainText = plainText +keyMatrix[i2][j2]
            

        # same row
        elif n1[0]==n2[0]:
            i1= n1[0]
            j1= (n1[1] + 4) % 5
            i2= n2[0]
            j2= (n2[1] + 4) % 5
            plainText = plainText +keyMatrix[i1][j1]
            plainText = plainText +keyMatrix[i2][j2]
            

        else:
            i1 = n1[0]
            j1 = n1[1]
            i2 = n2[0]
            j2 = n2[1]

            plainText = plainText +keyMatrix[i1][j2]
            plainText = plainText +keyMatrix[i2][j1]
            
        i += 2  
    return plainText                  
# print plainText with correct way 
def print_text(cipherText):
    pass;
def main():

    #Getting user inputs Key (to make the 5x5 char matrix)
    print(prepare_text_decryption("cipheXerTeXtZ"))
    key = input("Enter key: \n").replace(" ","").upper()
    while(1):
        choice=int(input("\n 1.Encryption \n 2.Decryption: \n 3.EXIT \n"))
        if choice==1:
            plainText = input("Enter plainText: \n").upper()
            print(seperate(plainText,key))
        elif choice==2:
            cypherText = input("Enter CipherText: \n").upper()
            print(seperate_decryption(cypherText,key))
        elif choice==3:
            exit()
        else:
            print("Choose correct choice")


if __name__ == "__main__":
    main()