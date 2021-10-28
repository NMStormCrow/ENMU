#  CS 120 Exam 2 Question #2
#  Thomas Crow


def computeEaster():
    
    userYear=eval(input("Please enter a year: "))

    if (userYear >= 1982) and (userYear <= 2048):
        a = (userYear % 19)
        b = (userYear % 4)
        c = (userYear % 7)
        d = ((19 * a) + 24) % 30
        e = ((2 * b) + (4 * c) + (6 * d) + 5) % 7

        if ((d +e) > 9):
            print(f"Easter is on 4/{((d + e) - 9)}/{userYear}")
        else:
            print(f"Easter is on 3/{(22 + (d + e))}/{userYear}")


    else:
        print("The year is not within the rang 1982-2048")

def main():
    computeEaster()


main()