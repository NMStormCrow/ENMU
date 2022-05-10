/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.sec01;
import javax.swing.JFrame;
import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JPanel;

/**
 *
 * @author CEHVAREE
 */
public class FilledFrame extends JFrame{
    
    private JButton button;
    private JLabel label;
    
    private static final int FRAME_WIDTH = 300;
    private static final int FRAME_HEIGTH = 100;
    
    public FilledFrame()
    {
        createComponents();
        setSize(FRAME_WIDTH, FRAME_HEIGTH);
    }
    
    private void createComponents()
    {
        button = new JButton("Click me");
        label = new JLabel("Hello World!");
        
        JPanel panel = new JPanel();
        panel.add(button);
        panel.add(label);
        this.add(panel);
    }
    
}
