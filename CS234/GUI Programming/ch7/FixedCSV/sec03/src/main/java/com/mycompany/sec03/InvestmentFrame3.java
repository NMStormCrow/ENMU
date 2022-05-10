/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.sec03;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JScrollBar;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;

/**
 *
 * @author CEHVAREE
 */
public class InvestmentFrame3 extends JFrame {
    
    private static final int FRAME_WIDTH = 450;
    private static final int FRAME_HEIGHT = 250;
    
    private static final int AREA_ROWS = 10;
    private static final int AREA_COLUMS = 30;
    
    private static final double DEFAULT_RATE = 5;
    private static final double INITIAL_BALANCE = 1000;
    
    private JLabel rateLabel;
    private JTextField rateField;
    private JButton button;
    private JTextArea resultArea;
    private double balance;

    public InvestmentFrame3() {
        balance = INITIAL_BALANCE;
        resultArea = new JTextArea(AREA_ROWS, AREA_COLUMS);
        resultArea.setText(balance + "\n");
        resultArea.setEditable(false);
        
        createTextField();
        createButton();
        createPanel();
        
        setSize(FRAME_WIDTH, FRAME_HEIGHT);
    }
    
    private void createTextField()
    {
        rateLabel = new JLabel("Interest rate: ");
        
        final int FIELD_WIDTH = 10;
        rateField = new JTextField(FIELD_WIDTH);
        rateField.setText("" + DEFAULT_RATE);
    }
    
    class AddInterestListener implements ActionListener
    {
        @Override
        public void actionPerformed(ActionEvent e) {
            double rate = Double.parseDouble(rateField.getText());
            double interest = balance * rate / 100;
            balance = balance + interest;
            resultArea.append(balance + "\n");
        }
    }
    
    private void createButton()
    {
        button = new JButton("Add interest");
        ActionListener listener = new AddInterestListener();
        button.addActionListener(listener);
    }
    
    private void createPanel()
    {
        JPanel panel = new JPanel();
        panel.add(rateLabel);
        panel.add(rateField);
        panel.add(button);
        JScrollPane scrollPane = new JScrollPane(resultArea);        
        panel.add(scrollPane);
        add(panel);
        
    }
}
