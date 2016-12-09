Line 11: path for directory where password text files will be placed. Change
string to whatever you want.

Line 127: path for location of .py file and src txt files. Change to fit
correct directory location.

Files:

passwordGen.py:
python file that generates passwords and files

TwentyThousandLeaguesUnderTheSeaVerne.txt:
source text used by passwordGen.py for generating a type of password

wordsEn.txt:
dictionary of words used by passwordGen.py


NOTE:
Uses python v 3.5.2

The first password generated inside of the 'bookWordsFirstLetter.txt'
password file is jibberish. remove it.

To generate a new set of passwords it is best to remove the entire
password file created by the program. While passwordGen.py does overwrite files
it does not seem to consistently overwrite the 'bookWordsFirstLetter.txt' file
