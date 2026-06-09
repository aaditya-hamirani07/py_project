A Python script that encrypt and decrypts text messages,it handles full sentences ,safely splitting and parsing words based on there lengths.

How it works:

Encryption - For words with 3 or more,it moves the first letter to the end and adds 3 random characters to both the front and the back of the word.

For shorter words it simply reverse the string
             
Decryption - Reverses the exact encrytion steps.

