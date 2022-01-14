# Assignment #7 Question #1
#
# Thomas Crow
# Date 10/03/2021
#
# Requirements:
#   One problem with the class example is that it does not deal with the case when we "drop off the end"
#   of the alphabet. A true Caesar cipher does the shifting in a circular fashion where the next character after "z" is "a."
#
#   Modify the solution to the class example to make it circular. Assume that the input consists only of letters and spaces.
#
#   Hint: do not need to code the space.
#
#

def main():

#   User input
    OrigMessage=input("Please enter a string of plaintext: ")
    Key=int(input("Please enter the value of the key: "))

#   Initialize variables
    WhiteSpace=" "
#   If entered key is greated than 26, we can work with the mod value to determine how many letters we will shift the text
    FormatedKey=Key%26
    CodedMessage=""

    for EachLetter in OrigMessage:
        if EachLetter.isupper():
            if (ord(EachLetter)+FormatedKey) > 90:
                CodedMessage=CodedMessage+chr(ord(EachLetter)+FormatedKey-26)
            else:
                CodedMessage=CodedMessage+chr(ord(EachLetter)+FormatedKey)
        elif EachLetter.islower():
            if (ord(EachLetter)+FormatedKey) > 122:
                CodedMessage=CodedMessage+chr(ord(EachLetter)+FormatedKey-26)
            else:
                CodedMessage=CodedMessage+chr(ord(EachLetter)+FormatedKey)
        elif EachLetter.isspace():
            CodedMessage=CodedMessage+EachLetter

#   Print output to user

    print("\n" * 5)
    print('*' * (len(OrigMessage) + 35))
    print('*' * 3,WhiteSpace * (len(OrigMessage)+ 27),'*' * 3)
    print("***  The original message:",OrigMessage,"    ***")
    print('*' * 3,WhiteSpace * (len(OrigMessage)+ 27),'*' * 3)
    print('*' * (len(OrigMessage) + 35))
    print('*' * 3,WhiteSpace * (len(OrigMessage)+ 27),'*' * 3)
    print("***  The provided key was:",Key," " * (len(OrigMessage)+ 2),"***")
    print('*' * 3,WhiteSpace * (len(OrigMessage)+ 27),'*' * 3)
    print('*' * (len(OrigMessage) + 35))
    print('*' * 3,WhiteSpace * (len(OrigMessage)+ 27),'*' * 3)
    print("***  The coded message is:",CodedMessage,"    ***")
    print('*' * 3,WhiteSpace * (len(OrigMessage)+ 27),'*' * 3)
    print('*' * (len(OrigMessage) + 35))


main()
