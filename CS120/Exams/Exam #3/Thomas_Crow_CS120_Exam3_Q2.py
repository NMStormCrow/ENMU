#  CS 120 Exam 3 Question #2
#  Thomas Crow

# Heating and cooling degree days are measures used by utility companies to estimate 
# energy requirements. If the average temperature for a day is below 60, then the 
# number of degrees below 60 is added to the heating degree days. If the temperature is 
# above 80, the amount over 80 is added to the cooling degree days.  
# 
# Write a program that read a sequence of average daily temperatures from an existing 
# file, and computes the running total of cooling and heating degree days. The program 
# should print these two totals after all the data has been processed. 
# Note: Your file should contain at least 7 daily temperatures. (Submit this file together 
# with your program



    
def calcuateHC_Days():
    filename= input("Please enter the name of the file to evaluate cooling and heating days: ")
    infile = open(filename)
    line = (infile.readline())
    line = line.strip()
    numHotDays = 0
    numCoolDays = 0

    while (line != ""):
        if (float(line) > 80):
            numHotDays = numHotDays + 1
        elif (float(line) < 60):
            numCoolDays = numCoolDays + 1
        line = (infile.readline())
        line = line.strip()    
    print(f"The number of days above 80 degrees F that required cooling were {numHotDays}.")
    print(f"The number of days below 60 degrees F that required heating were {numCoolDays}.")
    infile.close()

def main():
    calcuateHC_Days()

main()