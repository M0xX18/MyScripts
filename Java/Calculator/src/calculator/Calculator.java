/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package calculator;

import javax.swing.SwingUtilities;

/**
 *
 * @author papitas
 */
public class Calculator {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
    SwingUtilities.invokeLater(() -> {
        CalculadoraGUI calc = new CalculadoraGUI();
        calc.setVisible(true);
    });
}
    
}
