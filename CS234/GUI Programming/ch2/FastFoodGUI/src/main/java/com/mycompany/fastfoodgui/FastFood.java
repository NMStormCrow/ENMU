/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.fastfoodgui;

import java.util.HashMap;
import java.util.Map;

/**
 *
 * @author CEHVAREE
 */
public class FastFood {
    
    private HashMap<String, Double> menu = new HashMap<>();
    private static final double TAX = 0.10;
    private double subtotal = 0.0;
    private double total = 0.0;

    public FastFood() {
        
        menu.put("burger", 2.5);
        menu.put("fries", 1.5);
        menu.put("soda", 3.0);
        menu.put("cake", 3.5);
        
//        System.out.println(menu.size());
        printMenu();
    }
    
    public void printMenu()
    {
        for (String m : menu.keySet())
        {
            System.out.println(menu.get(m));
        }
    }
    
    public void computeTotal()
    {
        total = subtotal + (subtotal * TAX);
    }

    public double getTotal() {
        return total;
    }
    
    public void computeSubtotal(HashMap<String, Integer> counts)
    {
        for ( String k : counts.keySet())
        {
            subtotal = subtotal + (counts.get(k)*menu.get(k));
        }
        
    }

    public double getSubtotal() {
        return subtotal;
    }
    
    public double getPrice(String product) {
        
        double price = menu.get(product);
        System.out.println("price" + price);
        return price;
    }

    public void setSubtotal(double subtotal) {
        this.subtotal = subtotal;
    }

    public void setTotal(double total) {
        this.total = subtotal;
    }
    
    
}
