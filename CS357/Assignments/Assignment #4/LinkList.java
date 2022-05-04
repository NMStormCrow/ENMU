// Assignment #4 - LinkList.java
// CS357
// Thomas Crow

class LinkList {
    
//  Instance variable declarations    
    private Link head;
    int counter;
    
//  Default constructor
    public LinkList() {
        this.head = null;
    }

//  Method: insertFirst()
//  Purpose: insert a new link at the beginning of the list
//  Arguments: The first value of the link as an int value
//             The second value of the link as a double value
//  Returns: None

    public void insertFirst(int iData, double dData) {
        
        Link newNode = new Link(iData, dData);
       
        if (this.head == null) {
            this.head = newNode;
        }
        else {
            newNode.setNext(this.head);
            this.head = newNode;
        }
        counter++;
    }
    

//  Method: insertAfter()
//  Purpose: insert a new link after a specific link 
//  Arguments: The key as an int value
//             The first value of the link as an int value
//             The second value of the link as a double value
//  Returns: None

    public boolean insertAfter(int key, int iData, double dData) {

        Link currentNode = this.head;
        Link newNode = new Link(iData, dData);

        for (int i = 0; i < counter; i++) {
            if(currentNode.getiData() == key) {
                newNode.setNext(currentNode.getNext());
                currentNode.setNext(newNode);
                counter++;
                return true;
            }
            currentNode = currentNode.getNext();
        }

        return false;
    }
    
//  Method: find()
//  Purpose: Find a link list node that matches the key value provided, if one exists
//  Arguments: The key as an integer value
//  Returns: The found node as a node value, the value null if one is not found

    public Link find(int key) {
        
        Link currentNode = this.head;
        
        for (int i = 0; i < this.counter; i++) {
            if (currentNode.getiData() == key) 
                return currentNode;
            else
                currentNode = currentNode.getNext();
        }

        return null;

    }

//  Method: deleteLast()
//  Purpose: Delete the last link, assuming the list is not empty
//  Arguments: None
//  Returns: The deleted link as a value link

    public Link deleteLast() {

        Link currentLink = this.head;
        Link deletedLink = null;

        if (this.counter == 0)
            return null;

        if (this.counter == 1) {
            deletedLink = this.head;
            this.head = null;
            counter--;
            return deletedLink;
        }

        for (int i = 0; i < (counter - 2); i++) {
            currentLink = currentLink.getNext();
        }

        deletedLink = currentLink.getNext();
        currentLink.setNext(null);
        counter--;
        return deletedLink;
    }


//  Method: displayList()
//  Purpose: display the list
//  Arguments: None
//  Returns: None

    public void displayList() {

        Link currentNode = this.head;    
            
        if(this.head == null) {    
            System.out.println("List contains no nodes.");    
            return;    
        }    
        System.out.println("Values contained in linked list:");    
        while(currentNode != null) {    
            System.out.println(currentNode.getiData() + " " + currentNode.getdData());    
            currentNode = currentNode.getNext();    
        }    
        System.out.println();    
    }    
    
//  Method: isEmpty()
//  Purpose: Returns TRUE if the list is empty
//  Arguments: None
//  Returns: Logicial value of list being empty as a boolean value 

    public boolean isEmpty() {

        boolean listEmpty = false;

        return listEmpty;
    }
}