# Assignment #2 Question #3
#
# Thomas Crow
# Date 8/28/2021
#
# Requirements: Modify the class example (convert temperature) so that it computes and prints a table of Celsius temperatures
# and the Fahrenheit equivalents every 10 degrees from 0°C to 100°C.
#
# Formula: Farenheit = (9/5 * Celsius) + 32
#
# Notes for Instructor:
#
# I have formatted the output to display the floating point value of Fahrenheit to zero decimal places
#
# For additional practice, given your challenge in class of making a "pretty table",
# I've added to the formatting of the table with borders, tab spaces, and use of the degree symbol.
#
# I used formatted strings, which I know isn't supported before Python 3.6.  However, this exercise gave me an opportunity
# to really use these for the first time.

def main():

    border = ("---------------------------------")
    degree_symbol = ('\u00b0')

    print (border)
    print (f"|\tC{degree_symbol}\t|\tF{degree_symbol}\t|")
    print (border)

    for i in range(11):
        celsius = i * 10
        farenheit = (9/5 * celsius) + 32
        print (f"|\t{celsius}{degree_symbol}\t|\t{format(farenheit, '.0f')}{degree_symbol}\t|")
        print (border)

main()
