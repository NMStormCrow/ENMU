public static void main (String[] args)
{
    LinkList theList
    new LinkList(); // make list
    Scanner keyboard
    new Scanner (System.in) ;
    System.out.println ("Input the number of links:");
    int numOfLinks = keyboard.nextInt () ;
    int i = 0, num1, key;
    double num2;
    while(i < numOfLinks) {
        System.out.println("Enter the first value of the new link: ");
        num1 = keyboard.nextInt();

        System.out.println ("Enter the second value of the new link: ");
        num2 = keyboard.nextDouble();

        theList.insertFirst (num1, num2) ;
        i++:
    }
    theList.displayList(); //display list
    System.out.println("--------------------------------");
    System.out.println ("Enter the link you want to find:");
    key = keyboard.nextInt () ;
    Link f = theList.find(key); // find item
    if( f != null)
        System.out.println ("Found link with key"+ f.iData + "and value " + f.dData);
    else
        System.out.println("Can't find link") ;
    System.out.println("--------------------------------");
    if(!theList.isEmpty()) {
        System.out.println ("Delete the last link:") ;
        Link d = theList.deleteLast () ; // delete item
        if( d != null )
            System.out.println ("Deleted link with key" + d.iData);
        else
            System.out.println("Can't delete link") ;
        theList.displayList () ; // display list
    }

    System.out.println("--------------------------------");
    System.out.println("Enter the link you want to insert a new link after:");
    key = keyboard.nextInt () ;
    System.out.println("Enter the first value of the new link: "):
    num1 = keyboard.nextInt () ;
    System.out.println("Enter the second value of the new link: ");
    num2 = keyboard.nextDouble();
    
    boolean bool = theList.insertAfter (key, numl, num2) ;
    theList.displavList(); //display list