#  CS 120 Exam 2 Question #3
#  Thomas Crow


def orderList(list, listLength):

    orderedList = []

    minValue = 10000
    


    for i in range(listLength):
        for j in range(listLength):
            if (list[j] < minValue):
                minValue = list[j]
                maxIndex = j
        list[maxIndex] = 10000        
        orderedList.append(minValue)
        minValue = 10000
    
    print(f"{orderedList}")

    
  
#    print(f"{list}")
#    print(f"{orderedList}")

def main():
    list1 = [2,3,5,8,1,3,10]
    list2 = [10,9,8,7,6,5,4,3,2,1]


    orderList(list1, len(list1))
    orderList(list2, len(list2))

main()