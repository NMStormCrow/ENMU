/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tickets;

/**
 *
 * @author CEHVAREE
 */
public class Ticket {
    
    private static int adult;
    private static int child;
    private static boolean returnWanted;
    private static boolean firstWanted;
    private static double ticketcost;
    private static double dayTotal = 0;

    public static int getAdult() {
        return adult;
    }

    public static int getChild() {
        return child;
    }

    public static boolean isReturnWanted() {
        return returnWanted;
    }

    public static boolean isFirstWanted() {
        return firstWanted;
    }

    public static double getTicketcost() {
        return ticketcost;
    }

    public static double getDayTotal() {
        return dayTotal;
    }

    public static void setAdult(int adult) {
        Ticket.adult = adult;
    }

    public static void setChild(int child) {
        Ticket.child = child;
    }

    public static void setReturnWanted(boolean returnWanted) {
        Ticket.returnWanted = returnWanted;
    }

    public static void setFirstWanted(boolean firstWanted) {
        Ticket.firstWanted = firstWanted;
    }

    public static void setTicketcost(double ticketcost) {
        Ticket.ticketcost = ticketcost;
    }

    public static void setDayTotal(double dayTotal) {
        Ticket.dayTotal += dayTotal;
    }
    
    
    
}
