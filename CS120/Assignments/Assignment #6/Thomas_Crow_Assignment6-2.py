# Assignment #6 Question #2
#
# Thomas Crow
# Date 9/26/2021
#
#
#
#    An acronym is a word formed by taking the first letters of the words in a phrase and making a word from them. For example, RAM is an acronym for “Random Access Memory."
#
#    Write a program that allows the user to type in a phrase and then outputs the acronym for that phrase.
#
#    Hint: use the function split() to get the separate words
#
#          use the slicing to get the first letter of the word

def main():

    UserPhrase = (input("Pleae enter a phrase to turned into an Acronym: "))
    UserSplitPhrase = UserPhrase.split()

    print("The phrase entered is:",UserPhrase)
    numPhraseElements = (len(UserSplitPhrase))

    userAcronym = ""

    for i in range(numPhraseElements):
        loopChar = UserSplitPhrase[i][:1]
        userAcronym = userAcronym + loopChar.upper()

    print("The acronym is:",userAcronym)

main()
