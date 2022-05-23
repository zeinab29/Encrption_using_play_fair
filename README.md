# Encrption_using_playfair
This is a code for encrption and dycrption using Playfair Cipher
The Playfair Cipher Encryption Algorithm: 
The Algorithm consists of 2 steps: 
 

1. Generate the key Square(5×5): 
* The key square is a 5×5 grid of alphabets that acts as the key for encrypting the plaintext. Each of the 25 alphabets must be unique and one letter of the alphabet       (usually J) is omitted from the table (as the table can hold only 25 alphabets). If the plaintext contains J, then it is replaced by I. 
 
* The initial alphabets in the key square are the unique alphabets of the key in the order in which they appear followed by the remaining letters of the alphabet in       order. 
 
2. Algorithm to encrypt the plain text: The plaintext is split into pairs of two letters (digraphs). If there is an odd number of letters, a Z is added to the last letter.
    * For example: 
 
          PlainText: "instruments" 
          After Split: 'in' 'st' 'ru' 'me' 'nt' 'sz'

1. Pair cannot be made with same letter. Break the letter in single and add a bogus letter to the previous letter.

         Plain Text: “hello”

         After Split: ‘he’ ‘lx’ ‘lo’

         Here ‘x’ is the bogus letter.

2. If the letter is standing alone in the process of pairing, then add an extra bogus letter with the alone letter

       Plain Text: “helloe”

       AfterSplit: ‘he’ ‘lx’ ‘lo’ ‘ez’

       Here ‘z’  is the bogus letter.

Rules for Encryption: 
 

* If both the letters are in the same column: Take the letter below each one (going back to the top if at the bottom).
  For example: 
 
      Diagraph: "me"
      Encrypted Text: cl
      Encryption: 
         m -> c
         e -> l
     
     
     ![image](https://user-images.githubusercontent.com/54827182/169903783-7bf65909-0465-4eed-a182-9dba8c7d1dd3.png)



* If both the letters are in the same row: Take the letter to the right of each one (going back to the leftmost if at the rightmost position).
  For example: 
 
      Diagraph: "st"
      Encrypted Text: tl
      Encryption: 
        s -> t
        t -> l
      
   ![image](https://user-images.githubusercontent.com/54827182/169904281-e5f631ec-61c3-44e6-aa93-92de6bbca15d.png)
* If neither of the above rules is true: Form a rectangle with the two letters and take the letters on the horizontal opposite corner of the rectangle.
  For example: 
 
      Diagraph: "nt"
      Encrypted Text: rq
      Encryption: 
         n -> r
         t -> q
      
    ![image](https://user-images.githubusercontent.com/54827182/169904589-52ed29e5-0400-40ab-b241-836172d90696.png)


Decryption Technique
Decrypting the Playfair cipher is as simple as doing the same process in reverse. The receiver has the same key and can create the same key table, and then decrypt any messages made using that key.
The Playfair Cipher Decryption Algorithm: 
The Algorithm consistes of 2 steps: 
 

1. Generate the key Square(5×5) at the receiver’s end: 
  * The key square is a 5×5 grid of alphabets that acts as the key for encrypting the plaintext. Each of the 25 alphabets must be unique and one letter of the alphabet     (usually J) is omitted from the table (as the table can hold only 25 alphabets). If the plaintext contains J, then it is replaced by I. 
 
  * The initial alphabets in the key square are the unique alphabets of the key in the order in which they appear followed by the remaining letters of the alphabet in     order. 
 
2. Algorithm to decrypt the ciphertext: The ciphertext is split into pairs of two letters (digraphs). 
 
⚡⚡Note: The ciphertext always have even number of characters.

For example: 
 
    CipherText: "gatlmzclrqtx" 
    After Split: 'ga' 'tl' 'mz' 'cl' 'rq' 'tx'
    
   
   
▶Rules for Decryption: 
  If both the letters are in the same column: Take the letter above each one (going back to the bottom if at the top).
    For example: 
 
     Diagraph: "cl" 
     Decrypted Text: me
     Decryption: 
        c -> m
        l -> e
 
algorithm to decrypt the ciphertext

 
* If both the letters are in the same row: Take the letter to the left of each one (going back to the rightmost if at the leftmost position).
  For example: 
 
      Diagraph: "tl" 
      Decrypted Text: st 
      Decryption: 
       t -> s
       l -> t
 

 
* If neither of the above rules is true: Form a rectangle with the two letters and take the letters on the horizontal opposite corner of the rectangle.
  For example: 
 
      Diagraph: "rq" 
      Decrypted Text: nt 
      Decryption: 
          r -> n
          q -> t
 
