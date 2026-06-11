This repository contains two Python programs:

1.Text Encryption & Decryption
2.Tic Tac Toe Game


A Python script that encrypts and decrypts text messages.  
It handles full sentences, safely splitting and parsing words based on their lengths.
How it works:
Encryption - For words with 3 or more,it moves the first letter to the end and adds 3 random characters to both the front and the back of the word.
For shorter words it simply reverse the string
Decryption - Reverses the exact encrytion steps.


A simple console-based Tic Tac Toe game implemented in Python.  
Two players can play alternately, marking `X` and `O` on a 3×3 grid.
-Interactive command-line interface
-Input validation (prevents overwriting moves)
-Win detection for rows, columns, and diagonals
-Declares a draw if the board is filled with no winner

1.Run the script.
2.Players take turns entering their move (row and column).
3.The game announces the winner or a draw at the end.
