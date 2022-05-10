/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.sec01;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
/**
 *
 * @author CEHVAREE
 */
public class FilledFrameviewer {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        final int FRAME_HEIGHT = 300;
        final int FRAME_WIDTH = 400;
        
        JFrame frame = new JFrame();
        frame.setSize(FRAME_WIDTH, FRAME_HEIGHT);
        frame.setTitle("A frame with two components");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        
        JButton button = new JButton("Click me!");
        JLabel label = new JLabel("Hello, world!");
        JPanel panel = new JPanel();
        
        panel.add(button);
        panel.add(label);
        
        frame.add(panel);
        
        
        frame.setVisible(true);
    }
    
}
