public class tester1 {
    public static void main(String[] args) {

        Bug myBug = new Bug();
        myBug.move();
        myBug.move();    
        myBug.turn();    
        myBug.move();
        myBug.turn();    
        myBug.move();
        myBug.turn();    
        myBug.move();
        myBug.move();
        System.out.println("Expected postition: 10");
        System.out.println("Current postition: " + myBug.getPostition());
    }
}
