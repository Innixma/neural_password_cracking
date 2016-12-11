import string
import re
import random
#from random import SystemRandom
import rstr
import os

# rs = Rstr(SystemRandom())

txtFileDirectoryPath = './passwordFiles' #Change this path to the directory where you want
if not os.path.isdir(txtFileDirectoryPath):                                                   #the password files to be placed
    os.makedirs(txtFileDirectoryPath)

readPasswordFile = '10000frequentWordsMedium.txt'
with open(readPasswordFile) as wordFile:
    wordsList = wordFile.readlines()
fileSize = len(wordsList)

os.chdir(txtFileDirectoryPath)
for j in [500,1000,1500,2000]:
    passwordOutputFile = 'FourType' + str(j) + '.txt'
    writeFile = open(passwordOutputFile, 'w')
    for index in range (0, 30000):
        wordOne = random.randrange(0, j, 1)
        wordTwo = random.randrange(0, j, 1)
        wordThree = random.randrange(0, j, 1)
        wordFour = random.randrange(0, j, 1)
        newWord = wordsList[wordOne].strip('\n') + wordsList[wordTwo].strip('\n') + wordsList[wordThree].strip('\n') + wordsList[wordFour].strip('\n') + '\n'
        writeFile.write(newWord)
    writeFile.close()

for j in [500,1000,1500,2000]:
    passwordOutputFile = 'ThreeType' + str(j) + '.txt'
    writeFile = open(passwordOutputFile, 'w')
    for index in range (0, 30000):
        wordOne = random.randrange(0, fileSize, 1)
        wordTwo = random.randrange(0, fileSize, 1)
        wordThree = random.randrange(0, fileSize, 1)
        newWord = wordsList[wordOne].strip('\n') + wordsList[wordTwo].strip('\n') + wordsList[wordThree].strip('\n') + '\n'
        writeFile.write(newWord)
    writeFile.close()

for j in [500,1000,1500,2000]:
    passwordOutputFile = 'FourType' + str(j) + 'Upper.txt'
    writeFile = open(passwordOutputFile, 'w')
    for index in range (0, 30000):
        wordOne = random.randrange(0, fileSize, 1)
        wordTwo = random.randrange(0, fileSize, 1)
        wordThree = random.randrange(0, fileSize, 1)
        wordFour = random.randrange(0, fileSize, 1)
        newWord = wordsList[wordOne].strip('\n').title() + wordsList[wordTwo].strip('\n').title() + wordsList[wordThree].strip('\n').title() + wordsList[wordFour].strip('\n').title() + '\n'
        writeFile.write(newWord)
    writeFile.close()

for j in [500,1000,1500,2000]:
    passwordOutputFile = 'ThreeType' + str(j) + 'Upper.txt'
    writeFile = open(passwordOutputFile, 'w')
    for index in range (0, 30000):
        wordOne = random.randrange(0, fileSize, 1)
        wordTwo = random.randrange(0, fileSize, 1)
        wordThree = random.randrange(0, fileSize, 1)
        newWord = wordsList[wordOne].strip('\n').title() + wordsList[wordTwo].strip('\n').title() + wordsList[wordThree].strip('\n').title() + '\n'
        writeFile.write(newWord)
    writeFile.close()

passwordOutputFile = '8type2.txt'
writeFile = open(passwordOutputFile, 'w')
for index in range (0, 30000):
    charList = string.ascii_letters
    charList += string.digits
    newWord = rstr.rstr(charList, 8)
    newWord += '\n'
    writeFile.write(newWord)
writeFile.close()

passwordOutputFile = '8type3.txt'
writeFile = open(passwordOutputFile, 'w')
for index in range (0, 30000):
    charList = string.ascii_letters
    charList += string.digits
    charList += string.punctuation
    newWord = rstr.rstr(charList, 8)
    newWord += '\n'
    writeFile.write(newWord)
writeFile.close()

passwordOutputFile = '12type2.txt'
writeFile = open(passwordOutputFile, 'w')
for index in range (0, 30000):
    charList = string.ascii_letters
    charList += string.digits
    newWord = rstr.rstr(charList, 12)
    newWord += '\n'
    writeFile.write(newWord)
writeFile.close()

passwordOutputFile = '12type3.txt'
writeFile = open(passwordOutputFile, 'w')
for index in range (0, 30000):
    charList = string.ascii_letters
    charList += string.digits
    charList += string.punctuation
    newWord = rstr.rstr(charList, 12)
    newWord += '\n'
    writeFile.write(newWord)
writeFile.close()

passwordOutputFile = '16type2.txt'
writeFile = open(passwordOutputFile, 'w')
for index in range (0, 30000):
    charList = string.ascii_letters
    charList += string.digits
    newWord = rstr.rstr(charList, 16)
    newWord += '\n'
    writeFile.write(newWord)
writeFile.close()

passwordOutputFile = '16type3.txt'
writeFile = open(passwordOutputFile, 'w')
for index in range (0, 30000):
    charList = string.ascii_letters
    charList += string.digits
    charList += string.punctuation
    newWord = rstr.rstr(charList, 16)
    newWord += '\n'
    writeFile.write(newWord)
writeFile.close()


txtFileDirectoryPath = '..'  #Path of txt src files and .py file
os.chdir(txtFileDirectoryPath)
readPasswordFile = 'TwentyThousandLeaguesUnderTheSeaVerne.txt'
with open(readPasswordFile) as bookFile:
    bookList = bookFile.readlines()

numLines = len(bookList)
pattern = re.compile(r'"?\.{1,4}$')
txtFileDirectoryPath = './passwordFiles'
os.chdir(txtFileDirectoryPath)

passwordOutputFile = 'bookWordsFirstLetter.txt'
writeFile = open(passwordOutputFile, 'w')
for index in range (0, numLines): #change
    bookLineSplit = bookList[index].split()
    listLen = len(bookLineSplit)
    if listLen > 1:
        for k in range (0, listLen):
            if bookLineSplit[k][0] not in string.punctuation:
                newWord += bookLineSplit[k][0]
                isMatch = pattern.search(bookLineSplit[k])
                if isMatch != None:
                    wordLen = len(newWord)
                    if wordLen > 3 and wordLen < 25:
                        newWord += '\n'
                        writeFile.write(newWord)
                        newWord = ''
                    else:
                        newWord = ''
writeFile.close()
