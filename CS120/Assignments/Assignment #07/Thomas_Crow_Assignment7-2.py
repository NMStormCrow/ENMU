# Assignment #7 Question #2
#
# Thomas Crow
# Date 10/03/2021
#
# Requirements:
#
#
#    Write a program to analyze a file that: determine the number of lines, words, and characters contained therein.
#
#    The program should accept a file name as input and then print three numbers showing the count of lines, words, and characters in the file.
#
#    Remark: For your submission, should include the file you used here.
#
#

def main():

#   Initialize variables
    FileName=input("Please enter the filename to analyze: ")
    InFile=open(FileName, 'r')
    LineCount=0
    WordCount=0
    CharacterCount=0

    for EachLine in InFile:
        LineCount+=1
        LineSplitWords=EachLine.split()
        NumberOfWordsInLine=len(LineSplitWords)
        WordCount+=NumberOfWordsInLine
        CharacterCount+=len(EachLine)

#   User Output
    print("The number of lines in the file is:", LineCount)
    print("The number of words in the file is:", WordCount)
    print("The number of characters in the file is:", CharacterCount)

#   Close open files
    InFile.close


main()
