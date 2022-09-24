/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.products;

import javax.swing.JToggleButton;

/**
 *
 * @author CEHVAREE
 */
public class productSeletor extends javax.swing.JFrame {

    /**
     * Creates new form productSeletor
     */
    public productSeletor() {
        initComponents();
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        lblAvocado = new javax.swing.JLabel();
        lblOnion = new javax.swing.JLabel();
        lblStrawberry = new javax.swing.JLabel();
        lblTomato = new javax.swing.JLabel();
        btnAvocado = new javax.swing.JToggleButton();
        btnOnion = new javax.swing.JToggleButton();
        btnStrawberry = new javax.swing.JToggleButton();
        btnTomato = new javax.swing.JToggleButton();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setTitle("Produce availability");
        getContentPane().setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        lblAvocado.setIcon(new javax.swing.ImageIcon(getClass().getResource("/avocado.png"))); // NOI18N
        getContentPane().add(lblAvocado, new org.netbeans.lib.awtextra.AbsoluteConstraints(20, 70, 150, 130));

        lblOnion.setIcon(new javax.swing.ImageIcon(getClass().getResource("/red-onion.png"))); // NOI18N
        getContentPane().add(lblOnion, new org.netbeans.lib.awtextra.AbsoluteConstraints(170, 70, 150, 150));

        lblStrawberry.setIcon(new javax.swing.ImageIcon(getClass().getResource("/strawberry.png"))); // NOI18N
        getContentPane().add(lblStrawberry, new org.netbeans.lib.awtextra.AbsoluteConstraints(340, 70, 140, 150));

        lblTomato.setIcon(new javax.swing.ImageIcon(getClass().getResource("/tomato.png"))); // NOI18N
        getContentPane().add(lblTomato, new org.netbeans.lib.awtextra.AbsoluteConstraints(510, 90, 150, 140));

        btnAvocado.setSelected(true);
        btnAvocado.setText("off");
        btnAvocado.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnAvocadoActionPerformed(evt);
            }
        });
        getContentPane().add(btnAvocado, new org.netbeans.lib.awtextra.AbsoluteConstraints(60, 250, -1, -1));

        btnOnion.setSelected(true);
        btnOnion.setText("off");
        btnOnion.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnOnionActionPerformed(evt);
            }
        });
        getContentPane().add(btnOnion, new org.netbeans.lib.awtextra.AbsoluteConstraints(220, 250, -1, -1));

        btnStrawberry.setSelected(true);
        btnStrawberry.setText("off");
        btnStrawberry.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnStrawberryActionPerformed(evt);
            }
        });
        getContentPane().add(btnStrawberry, new org.netbeans.lib.awtextra.AbsoluteConstraints(390, 250, -1, -1));

        btnTomato.setSelected(true);
        btnTomato.setText("off");
        btnTomato.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnTomatoActionPerformed(evt);
            }
        });
        getContentPane().add(btnTomato, new org.netbeans.lib.awtextra.AbsoluteConstraints(580, 250, -1, -1));

        setBounds(0, 0, 700, 403);
    }// </editor-fold>//GEN-END:initComponents

    private void btnAvocadoActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnAvocadoActionPerformed
        
        JToggleButton btn = (JToggleButton) evt.getSource();
        if (btn.isSelected())
        {
            lblAvocado.setVisible(true);
            btnAvocado.setText("off");
        }
        else
        {
            lblAvocado.setVisible(false);
            btnAvocado.setText("on");
        }
        
    }//GEN-LAST:event_btnAvocadoActionPerformed

    private void btnOnionActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnOnionActionPerformed
        
        JToggleButton btn = (JToggleButton) evt.getSource();
        if (btn.isSelected())
        {
            lblOnion.setVisible(true);
            btnOnion.setText("off");
        }
        else
        {
            lblOnion.setVisible(false);
            btnOnion.setText("on");
        }
        
    }//GEN-LAST:event_btnOnionActionPerformed

    private void btnStrawberryActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnStrawberryActionPerformed
        
        JToggleButton btn = (JToggleButton) evt.getSource();
        if (btn.isSelected())
        {
            lblStrawberry.setVisible(true);
            btnStrawberry.setText("off");
        }
        else
        {
            lblStrawberry.setVisible(false);
            btnStrawberry.setText("on");
        }
        
    }//GEN-LAST:event_btnStrawberryActionPerformed

    private void btnTomatoActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnTomatoActionPerformed
        
        JToggleButton btn = (JToggleButton) evt.getSource();
        if (btn.isSelected())
        {
            lblTomato.setVisible(true);
            btnTomato.setText("off");
        }
        else
        {
            lblTomato.setVisible(false);
            btnTomato.setText("on");
        }
        
    }//GEN-LAST:event_btnTomatoActionPerformed

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Windows".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(productSeletor.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(productSeletor.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(productSeletor.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(productSeletor.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new productSeletor().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JToggleButton btnAvocado;
    private javax.swing.JToggleButton btnOnion;
    private javax.swing.JToggleButton btnStrawberry;
    private javax.swing.JToggleButton btnTomato;
    private javax.swing.JLabel lblAvocado;
    private javax.swing.JLabel lblOnion;
    private javax.swing.JLabel lblStrawberry;
    private javax.swing.JLabel lblTomato;
    // End of variables declaration//GEN-END:variables
}