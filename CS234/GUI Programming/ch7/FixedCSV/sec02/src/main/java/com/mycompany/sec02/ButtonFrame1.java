/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.sec02;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;


/**
 *
 * @author CEHVAREE
 */
public class ButtonFrame1 extends JFrame{
    
    private static final int FRAME_WIDTH = 300;
    private static final int FRAME_HEIGHT = 100;
    
    public ButtonFrame1()
    {
        createComponents();
        setSize(FRAME_WIDTH, FRAME_HEIGHT);
    }
    
    private void createComponents()
    {
        JButton button = new JButton("Click me");
        JPanel panel = new JPanel();
        panel.add(button);
        add(panel);
        
        ActionListener istener = new ClickListener();
        button.addActionListener(istener);
        
    }
    
    
}
