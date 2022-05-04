// Assignment #4 - Link.java
// CS357
// Thomas Crow

public class Link {

//  Instance variable declarations    
    private int iData;
    private double dData;
    private Link next;

// Default constructor

    public Link(int idata, double ddata) {
        this.iData = idata;
        this.dData = ddata;
        this.next = null;
    }

//  Method: getiData()
//  Purpose: Return the integer data from Link instance
//  Arguments: None
//  Returns: Integer data as an integer

    public int getiData() {
        return this.iData;
    }

//  Method: getdData()
//  Purpose: Return the double data from Link instance
//  Arguments: None
//  Returns: Double data as an double

    public double getdData() {
        return this.dData;
    }

//  Method: setiData()
//  Purpose: Sets the integer data for a Link instance
//  Arguments: iData as an integer
//  Returns: Nonde

    public void setiData(int iData) {
        this.iData = iData;
    }

//  Method: setdData()
//  Purpose: Sets the double data for a Link instance
//  Arguments: dData as a double
//  Returns: None

    public void  setdData(Double dData) {
        this.dData = dData;
    }

//  Method: getNext()
//  Purpose: Returns the value of the next node 
//  Arguments: None
//  Returns: The value of of the next node as a value Link
    
    public Link getNext() {
        return this.next;
    }

//  Method: setNext()
//  Purpose: Sets the value of the next node 
//  Arguments: The next node as a link value
//  Returns: None

    public void setNext(Link next) {
        this.next = next;
    }
}
    