# Assignment #8 Question #1
#
# Thomas Crow
# Date 10/10/2021
#
#   Requirements:
#   Write a program to print the lyrics for ten verses of "The Ants Go Marching." A couple of sample verses are given below.
#   You may choose your own activity for the "little one" in each verse, but be sure to choose something that makes the rhyme work (or almost work) .


def song_verse(action):
    print("The ants go marching one by one, hurrah, hurrah.")
    print("The ants go marching one by one, hurrah, hurrah.")
    print("The ants go marching one by one,")
    print(f"The little one stops to {action}.")
    print("And they all go marching down,")
    print("To the ground, to get out of the rain.")
    print("BOOM! BOOM! BOOM!")
    print()

def main():
    song_verse("suck his thumb")
    song_verse("tie her shoe")
    song_verse("climb a tree")
    song_verse("shut the door")
    song_verse("take a dive")
    song_verse("pick up sticks")
    song_verse("pray to heaven")
    song_verse("check the gate")
    song_verse("check the time")
    song_verse("say “The End!\"")

main()
