/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.library;

/**
 *
 * @author CEHVAREE
 */
public class Book {
    
    private int number;
    private String title;
    private Boolean borrowed;
    private String borrower;
 
    public static Book[] bookObject = new Book[9];
    
    public Book(int bookNumber, String bookTitle)
    {
        number = bookNumber;
        title = bookTitle;
        borrowed = false;
    }
    
    public String getTitle()
    {
        return title;
    }
    
    public Boolean getBorrowed()
    {
        return borrowed;
    }
    
    public String getBorrower()
    {
        return borrower;
    }
    
    
    public void borrowBook(String borrowerName)
    {
        borrowed = true;
        borrower = borrowerName;
    }
    
    
    public void returnBook()
    {
        borrowed = false;
        borrower = "";
    }
    
    
}
