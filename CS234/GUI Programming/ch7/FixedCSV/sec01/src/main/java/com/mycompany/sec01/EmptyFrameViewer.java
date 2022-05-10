/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.sec01;
import javax.swing.JFrame;

/**
 *
 * @author CEHVAREE
 */
public class EmptyFrameViewer {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        final int FRAME_WIDTH = 300;
        final int FRAME_HEIGHT = 400;
        
        JFrame frame = new JFrame();
        frame.setSize(FRAME_WIDTH, FRAME_HEIGHT);
        frame.setTitle("Empty frame");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        frame.setVisible(true);
        
    }
    
}
