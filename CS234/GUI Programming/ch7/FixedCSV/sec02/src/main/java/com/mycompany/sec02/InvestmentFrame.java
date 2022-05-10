/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.sec02;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

/**
 *
 * @author CEHVAREE
 */
public class InvestmentFrame extends JFrame {
    
    private JButton button;
    private JLabel resultLabel;
    private double balance;
    
    private static final int FRAME_HEIGTH = 300;
    private static final int FRAME_WIDTH = 100;
    
    private static final double INTEREST_RATE = 5;
    private static final double INITIAL_BALANCE = 1000;
    
    
    
    public InvestmentFrame() {
        balance = INITIAL_BALANCE;
        
        createComponents();
        setSize(FRAME_HEIGTH, FRAME_WIDTH);
        
    }
    
    
    class AddInterestListener implements ActionListener
    {

        @Override
        public void actionPerformed(ActionEvent e) {
        
            double interest = balance * INTEREST_RATE /100;
            balance = balance + interest;
            resultLabel.setText(String.format("Balance:" +  balance));    
        }
    }
    
    private void createComponents()
    {
        button = new JButton("Add interest");
        ActionListener listener = new AddInterestListener();
        button.addActionListener(listener);
        
        resultLabel = new JLabel("Balance: " + String.format("%.2f", balance));
        
        JPanel panel = new JPanel();
        panel.add(button);
        panel.add(resultLabel);
        
        add(panel);
        
    }


    
    
    
}
