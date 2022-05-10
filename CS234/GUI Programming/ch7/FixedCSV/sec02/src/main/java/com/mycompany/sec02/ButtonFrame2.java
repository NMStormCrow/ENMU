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
public class ButtonFrame2 extends JFrame{
    
    private JButton button;
    private JLabel label;
    
    private static final int FRAME_WIDTH = 300;
    private static final int FRAME_HEIGHT = 100;
    
    private int count;
    
    public ButtonFrame2()
    {
        count = 0;
        createComponents();
        setSize(FRAME_WIDTH, FRAME_HEIGHT);
    }
    
    
    class ClickListener implements ActionListener
    {

        @Override
        public void actionPerformed(ActionEvent e) {
            count++;
            label.setText("Times cliecked: " + count);
        }
    }
    
    private void createComponents()
    {
        button = new JButton("Click me");
        ActionListener listener = new ClickListener();
        button.addActionListener(listener);
        
        label = new JLabel("Hello world");
        
        JPanel panel = new JPanel();
        panel.add(button);
        panel.add(label);
        
        add(panel);
        
    }
    
}
