/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/GUIForms/JFrame.java to edit this template
 */
package calculator;
import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

/**
 *
 * @author papitas
 */
public class CalculadoraGUI extends javax.swing.JFrame {
    
    private final StringBuilder operacion = new StringBuilder();
    
    /**
     * Creates new form CalculadoraGUI
     */
    public CalculadoraGUI() {
        initComponents();
        agregarEventos();
    }
    
    private void agregarEventos() {
        ActionListener listener = new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                JButton boton = (JButton) e.getSource();
                String texto = boton.getText();
                manejarEntrada(texto);
            }
        };

        JButton[] botones = {Button0, Button1, Button2, Button3, Button4, Button5, Button6, Button7, Button8, Button9, 
                            ButtonPlus, ButtonLess, ButtonMult, ButtonDiv, ButtonEq, ButtonC, 
                            ButtonOpenPar, ButtonClosePar, ButtonSqrt, ButtonExp};

        for (JButton boton : botones) {
            boton.addActionListener(listener);
        }
    }
    
    private void manejarEntrada(String texto) {
        if (operacion.length() > 0) {
            char ultimo = operacion.charAt(operacion.length() - 1);
            if (texto.matches("[0-9]") && (ultimo == ')' || ultimo == '√')) {
                operacion.append("*");
            } else if (texto.equals("(") && (Character.isDigit(ultimo) || ultimo == ')')) {
                operacion.append("*");
            }
        }
        
        switch (texto) {
            case "=":
                evaluarExpresion();
                break;
            case "C":
                operacion.setLength(0);
                Operaciones.setText("");
                break;
            case "√":
                if (operacion.length() > 0 && Character.isDigit(operacion.charAt(operacion.length() - 1))) {
                    operacion.append("*√(");
                } else {
                    operacion.append("√(");
                }
                Operaciones.setText(operacion.toString());
                break;
            case "^":
                operacion.append("^");
                Operaciones.setText(operacion.toString());
                break;
            default:
                operacion.append(texto);
                Operaciones.setText(operacion.toString());
                break;
        }
    }
    
    private void evaluarExpresion() {
        try {
            double resultado = evaluar(operacion.toString());
            if (resultado == (int) resultado) {
                Operaciones.setText(String.valueOf((int) resultado));
                operacion.setLength(0);
                operacion.append((int) resultado);
            } else {
                Operaciones.setText(String.valueOf(resultado));
                operacion.setLength(0);
                operacion.append(resultado);
            }
        } catch (Exception e) {
            Operaciones.setText("Error");
            operacion.setLength(0);
        }
    }
    
      private double evaluar(String expresion) {
          return new Object() {
              int pos = -1, ch;
              
              void siguiente() {
                  ch = (++pos < expresion.length()) ? expresion.charAt(pos) : -1;
              }
              
              boolean consumir(int charEsperado) {
                  while (ch == ' ') siguiente();
                  if (ch == charEsperado) {
                      siguiente();
                      return true;
                  }
                  return false;
              }
              
              double parse() {
                  siguiente();
                  double x = parseExpresion();
                  if (pos < expresion.length()) throw new RuntimeException("Error en la expresión");
                  return x;
              }
              
              double parseExpresion() {
                  double x = parseTermino();
                  while (true) {
                      if (consumir('+')) x += parseTermino();
                      else if (consumir('-')) x -= parseTermino();
                      else return x;
                  }
              }
              
              double parseTermino() {
                  double x = parseFactor();
                  while (true) {
                      if (consumir('*')) x *= parseFactor();
                      else if (consumir('/')) x /= parseFactor();
                      else return x;
                  }
              }
              
              double parseFactor() {
                  if (consumir('+')) return parseFactor();
                  if (consumir('-')) return -parseFactor();
                  
                  double x;
                  int startPos = this.pos;
                  if (consumir('(')) {
                      x = parseExpresion();
                      consumir(')');
                  } else if (consumir('√')) {
                      x = Math.sqrt(parseFactor());
                  } else {
                      while ((ch >= '0' && ch <= '9') || ch == '.') siguiente();
                      x = Double.parseDouble(expresion.substring(startPos, this.pos));
                  }
                  
                  if (consumir('^')) {
                      x = Math.pow(x, parseFactor());
                  }
                  return x;
              }
          }.parse();
      }
    
    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        Interface = new javax.swing.JDesktopPane();
        Pantalla = new javax.swing.JScrollPane();
        Operaciones = new javax.swing.JTextArea();
        Button7 = new javax.swing.JButton();
        Button4 = new javax.swing.JButton();
        Button1 = new javax.swing.JButton();
        Button8 = new javax.swing.JButton();
        Button2 = new javax.swing.JButton();
        Button5 = new javax.swing.JButton();
        Button3 = new javax.swing.JButton();
        Button6 = new javax.swing.JButton();
        Button9 = new javax.swing.JButton();
        ButtonDiv = new javax.swing.JButton();
        ButtonMult = new javax.swing.JButton();
        ButtonLess = new javax.swing.JButton();
        ButtonC = new javax.swing.JButton();
        Button0 = new javax.swing.JButton();
        ButtonEq = new javax.swing.JButton();
        ButtonPlus = new javax.swing.JButton();
        ButtonOpenPar = new javax.swing.JButton();
        ButtonClosePar = new javax.swing.JButton();
        ButtonSqrt = new javax.swing.JButton();
        ButtonExp = new javax.swing.JButton();
        jLabel1 = new javax.swing.JLabel();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

        Interface.setBorder(new javax.swing.border.SoftBevelBorder(javax.swing.border.BevelBorder.RAISED));

        Operaciones.setEditable(false);
        Operaciones.setColumns(1);
        Operaciones.setFont(new java.awt.Font("sansserif", 1, 29)); // NOI18N
        Operaciones.setRows(1);
        Operaciones.setTabSize(1);
        Operaciones.setBorder(new javax.swing.border.SoftBevelBorder(javax.swing.border.BevelBorder.RAISED));
        Pantalla.setViewportView(Operaciones);

        Button7.setBackground(new java.awt.Color(204, 204, 204));
        Button7.setFont(new java.awt.Font("sansserif", 1, 30)); // NOI18N
        Button7.setText("7");
        Button7.setBorder(new javax.swing.border.SoftBevelBorder(javax.swing.border.BevelBorder.RAISED));
        Button7.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                Button7ActionPerformed(evt);
            }
        });

        Button4.setBackground(new java.awt.Color(204, 204, 204));
        Button4.setFont(new java.awt.Font("sansserif", 1, 30)); // NOI18N
        Button4.setText("4");
        Button4.setBorder(new javax.swing.border.SoftBevelBorder(javax.swing.border.BevelBorder.RAISED));
        Button4.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                Button4ActionPerformed(evt);
            }
        });

        Button1.setBackground(new java.awt.Color(204, 204, 204));
        Button1.setFont(new java.awt.Font("sansserif", 1, 30)); // NOI18N
        Button1.setText("1");
        Button1.setBorder(new javax.swing.border.SoftBevelBorder(javax.swing.border.BevelBorder.RAISED));
        Button1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                Button1ActionPerformed(evt);
            }
        });

        Button8.setBackground(new java.awt.Color(204, 204, 204));
        Button8.setFont(new java.awt.Font("sansserif", 1, 30)); // NOI18N
        Button8.setText("8");
        Button8.setBorder(new javax.swing.border.SoftBevelBorder(javax.swing.border.BevelBorder.RAISED));
        Button8.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                Button8ActionPerformed(evt);
            }
        });

        Button2.setBackground(new java.awt.Color(204, 204, 204));
        Button2.setFont(new java.awt.Font("sansserif", 1, 30)); // NOI18N
        Button2.setText("2");
        Button2.setBorder(new javax.swing.border.SoftBevelBorder(javax.swing.border.BevelBorder.RAISED));
        Button2.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                Button2ActionPerformed(evt);
            }
        });

        Button5.setBackground(new java.awt.Color(204, 204, 204));
        Button5.setFont(new java.awt.Font("sansserif", 1, 30)); // NOI18N
        Button5.setText("5");
        Button5.setBorder(new javax.swing.border.SoftBevelBorder(javax.swing.border.BevelBorder.RAISED));
        Button5.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                Button5ActionPerformed(evt);
            }
        });

        Button3.setBackground(new java.awt.Color(204, 204, 204));
        Button3.setFont(new java.awt.Font("sansserif", 1, 30)); // NOI18N
        Button3.setText("3");
        Button3.setBorder(new javax.swing.border.SoftBevelBorder(javax.swing.border.BevelBorder.RAISED));
        Button3.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                Button3ActionPerformed(evt);
            }
        });

        Button6.setBackground(new java.awt.Color(204, 204, 204));
        Button6.setFont(new java.awt.Font("sansserif", 1, 30)); // NOI18N
        Button6.setText("6");
        Button6.setBorder(new javax.swing.border.SoftBevelBorder(javax.swing.border.BevelBorder.RAISED));
        Button6.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                Button6ActionPerformed(evt);
            }
        });

        Button9.setBackground(new java.awt.Color(204, 204, 204));
        Button9.setFont(new java.awt.Font("sansserif", 1, 30)); // NOI18N
        Button9.setText("9");
        Button9.setBorder(new javax.swing.border.SoftBevelBorder(javax.swing.border.BevelBorder.RAISED));
        Button9.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                Button9ActionPerformed(evt);
            }
        });

        ButtonDiv.setBackground(new java.awt.Color(255, 255, 204));
        ButtonDiv.setFont(new java.awt.Font("sansserif", 1, 30)); // NOI18N
        ButtonDiv.setText("/");
        ButtonDiv.setBorder(new javax.swing.border.SoftBevelBorder(javax.swing.border.BevelBorder.RAISED));
        ButtonDiv.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                ButtonDivActionPerformed(evt);
            }
        });

        ButtonMult.setBackground(new java.awt.Color(255, 255, 204));
        ButtonMult.setFont(new java.awt.Font("sansserif", 1, 30)); // NOI18N
        ButtonMult.setText("*");
        ButtonMult.setBorder(new javax.swing.border.SoftBevelBorder(javax.swing.border.BevelBorder.RAISED));
        ButtonMult.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                ButtonMultActionPerformed(evt);
            }
        });

        ButtonLess.setBackground(new java.awt.Color(255, 255, 204));
        ButtonLess.setFont(new java.awt.Font("sansserif", 1, 30)); // NOI18N
        ButtonLess.setText("-");
        ButtonLess.setBorder(new javax.swing.border.SoftBevelBorder(javax.swing.border.BevelBorder.RAISED));
        ButtonLess.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                ButtonLessActionPerformed(evt);
            }
        });

        ButtonC.setBackground(new java.awt.Color(255, 153, 153));
        ButtonC.setFont(new java.awt.Font("sansserif", 1, 30)); // NOI18N
        ButtonC.setText("C");
        ButtonC.setBorder(new javax.swing.border.SoftBevelBorder(javax.swing.border.BevelBorder.RAISED));
        ButtonC.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                ButtonCActionPerformed(evt);
            }
        });

        Button0.setBackground(new java.awt.Color(204, 204, 204));
        Button0.setFont(new java.awt.Font("sansserif", 1, 30)); // NOI18N
        Button0.setText("0");
        Button0.setBorder(new javax.swing.border.SoftBevelBorder(javax.swing.border.BevelBorder.RAISED));
        Button0.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                Button0ActionPerformed(evt);
            }
        });

        ButtonEq.setBackground(new java.awt.Color(153, 204, 255));
        ButtonEq.setFont(new java.awt.Font("sansserif", 1, 30)); // NOI18N
        ButtonEq.setText("=");
        ButtonEq.setBorder(new javax.swing.border.SoftBevelBorder(javax.swing.border.BevelBorder.RAISED));
        ButtonEq.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                ButtonEqActionPerformed(evt);
            }
        });

        ButtonPlus.setBackground(new java.awt.Color(255, 255, 204));
        ButtonPlus.setFont(new java.awt.Font("sansserif", 1, 30)); // NOI18N
        ButtonPlus.setText("+");
        ButtonPlus.setBorder(new javax.swing.border.SoftBevelBorder(javax.swing.border.BevelBorder.RAISED));
        ButtonPlus.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                ButtonPlusActionPerformed(evt);
            }
        });

        ButtonOpenPar.setBackground(new java.awt.Color(255, 255, 204));
        ButtonOpenPar.setFont(new java.awt.Font("sansserif", 1, 30)); // NOI18N
        ButtonOpenPar.setText("(");
        ButtonOpenPar.setBorder(new javax.swing.border.SoftBevelBorder(javax.swing.border.BevelBorder.RAISED));
        ButtonOpenPar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                ButtonOpenParActionPerformed(evt);
            }
        });

        ButtonClosePar.setBackground(new java.awt.Color(255, 255, 204));
        ButtonClosePar.setFont(new java.awt.Font("sansserif", 1, 30)); // NOI18N
        ButtonClosePar.setText(")");
        ButtonClosePar.setBorder(new javax.swing.border.SoftBevelBorder(javax.swing.border.BevelBorder.RAISED));
        ButtonClosePar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                ButtonCloseParActionPerformed(evt);
            }
        });

        ButtonSqrt.setBackground(new java.awt.Color(255, 255, 204));
        ButtonSqrt.setFont(new java.awt.Font("Accanthis ADF Std", 1, 30)); // NOI18N
        ButtonSqrt.setText("√");
        ButtonSqrt.setBorder(new javax.swing.border.SoftBevelBorder(javax.swing.border.BevelBorder.RAISED));
        ButtonSqrt.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                ButtonSqrtActionPerformed(evt);
            }
        });

        ButtonExp.setBackground(new java.awt.Color(255, 255, 204));
        ButtonExp.setFont(new java.awt.Font("sansserif", 1, 30)); // NOI18N
        ButtonExp.setText("^");
        ButtonExp.setBorder(new javax.swing.border.SoftBevelBorder(javax.swing.border.BevelBorder.RAISED));
        ButtonExp.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                ButtonExpActionPerformed(evt);
            }
        });

        jLabel1.setFont(new java.awt.Font("sansserif", 1, 13)); // NOI18N
        jLabel1.setText("PapitasCalculator3000");

        Interface.setLayer(Pantalla, javax.swing.JLayeredPane.DEFAULT_LAYER);
        Interface.setLayer(Button7, javax.swing.JLayeredPane.DEFAULT_LAYER);
        Interface.setLayer(Button4, javax.swing.JLayeredPane.DEFAULT_LAYER);
        Interface.setLayer(Button1, javax.swing.JLayeredPane.DEFAULT_LAYER);
        Interface.setLayer(Button8, javax.swing.JLayeredPane.DEFAULT_LAYER);
        Interface.setLayer(Button2, javax.swing.JLayeredPane.DEFAULT_LAYER);
        Interface.setLayer(Button5, javax.swing.JLayeredPane.DEFAULT_LAYER);
        Interface.setLayer(Button3, javax.swing.JLayeredPane.DEFAULT_LAYER);
        Interface.setLayer(Button6, javax.swing.JLayeredPane.DEFAULT_LAYER);
        Interface.setLayer(Button9, javax.swing.JLayeredPane.DEFAULT_LAYER);
        Interface.setLayer(ButtonDiv, javax.swing.JLayeredPane.DEFAULT_LAYER);
        Interface.setLayer(ButtonMult, javax.swing.JLayeredPane.DEFAULT_LAYER);
        Interface.setLayer(ButtonLess, javax.swing.JLayeredPane.DEFAULT_LAYER);
        Interface.setLayer(ButtonC, javax.swing.JLayeredPane.DEFAULT_LAYER);
        Interface.setLayer(Button0, javax.swing.JLayeredPane.DEFAULT_LAYER);
        Interface.setLayer(ButtonEq, javax.swing.JLayeredPane.DEFAULT_LAYER);
        Interface.setLayer(ButtonPlus, javax.swing.JLayeredPane.DEFAULT_LAYER);
        Interface.setLayer(ButtonOpenPar, javax.swing.JLayeredPane.DEFAULT_LAYER);
        Interface.setLayer(ButtonClosePar, javax.swing.JLayeredPane.DEFAULT_LAYER);
        Interface.setLayer(ButtonSqrt, javax.swing.JLayeredPane.DEFAULT_LAYER);
        Interface.setLayer(ButtonExp, javax.swing.JLayeredPane.DEFAULT_LAYER);
        Interface.setLayer(jLabel1, javax.swing.JLayeredPane.DEFAULT_LAYER);

        javax.swing.GroupLayout InterfaceLayout = new javax.swing.GroupLayout(Interface);
        Interface.setLayout(InterfaceLayout);
        InterfaceLayout.setHorizontalGroup(
            InterfaceLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(InterfaceLayout.createSequentialGroup()
                .addContainerGap()
                .addGroup(InterfaceLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, InterfaceLayout.createSequentialGroup()
                        .addGap(0, 0, Short.MAX_VALUE)
                        .addComponent(jLabel1)
                        .addContainerGap())
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, InterfaceLayout.createSequentialGroup()
                        .addComponent(Pantalla)
                        .addContainerGap())))
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, InterfaceLayout.createSequentialGroup()
                .addContainerGap(25, Short.MAX_VALUE)
                .addGroup(InterfaceLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(Button1, javax.swing.GroupLayout.PREFERRED_SIZE, 71, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(Button7, javax.swing.GroupLayout.PREFERRED_SIZE, 71, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(Button4, javax.swing.GroupLayout.PREFERRED_SIZE, 71, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(ButtonC, javax.swing.GroupLayout.PREFERRED_SIZE, 71, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(ButtonOpenPar, javax.swing.GroupLayout.PREFERRED_SIZE, 71, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addGroup(InterfaceLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(Button2, javax.swing.GroupLayout.PREFERRED_SIZE, 71, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(Button8, javax.swing.GroupLayout.PREFERRED_SIZE, 71, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(Button5, javax.swing.GroupLayout.PREFERRED_SIZE, 71, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(Button0, javax.swing.GroupLayout.PREFERRED_SIZE, 71, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(ButtonClosePar, javax.swing.GroupLayout.PREFERRED_SIZE, 71, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addGroup(InterfaceLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(InterfaceLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                        .addGroup(InterfaceLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(Button6, javax.swing.GroupLayout.PREFERRED_SIZE, 71, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(Button9, javax.swing.GroupLayout.PREFERRED_SIZE, 71, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addComponent(Button3, javax.swing.GroupLayout.PREFERRED_SIZE, 71, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addComponent(ButtonEq, javax.swing.GroupLayout.PREFERRED_SIZE, 71, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(ButtonSqrt, javax.swing.GroupLayout.PREFERRED_SIZE, 71, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addGroup(InterfaceLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(ButtonMult, javax.swing.GroupLayout.PREFERRED_SIZE, 71, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(ButtonLess, javax.swing.GroupLayout.PREFERRED_SIZE, 71, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(ButtonDiv, javax.swing.GroupLayout.PREFERRED_SIZE, 71, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(ButtonPlus, javax.swing.GroupLayout.PREFERRED_SIZE, 71, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(ButtonExp, javax.swing.GroupLayout.PREFERRED_SIZE, 71, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(19, 19, 19))
        );
        InterfaceLayout.setVerticalGroup(
            InterfaceLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(InterfaceLayout.createSequentialGroup()
                .addContainerGap()
                .addComponent(Pantalla, javax.swing.GroupLayout.PREFERRED_SIZE, 54, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 12, Short.MAX_VALUE)
                .addGroup(InterfaceLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(InterfaceLayout.createSequentialGroup()
                        .addComponent(ButtonOpenPar, javax.swing.GroupLayout.PREFERRED_SIZE, 67, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(Button7, javax.swing.GroupLayout.PREFERRED_SIZE, 67, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addComponent(Button4, javax.swing.GroupLayout.PREFERRED_SIZE, 67, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addComponent(Button1, javax.swing.GroupLayout.PREFERRED_SIZE, 67, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(ButtonC, javax.swing.GroupLayout.PREFERRED_SIZE, 67, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(InterfaceLayout.createSequentialGroup()
                        .addGroup(InterfaceLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                            .addComponent(ButtonClosePar, javax.swing.GroupLayout.PREFERRED_SIZE, 67, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(ButtonExp, javax.swing.GroupLayout.PREFERRED_SIZE, 67, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(ButtonSqrt, javax.swing.GroupLayout.PREFERRED_SIZE, 67, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addGroup(InterfaceLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(InterfaceLayout.createSequentialGroup()
                                .addComponent(ButtonDiv, javax.swing.GroupLayout.PREFERRED_SIZE, 67, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                                .addComponent(ButtonMult, javax.swing.GroupLayout.PREFERRED_SIZE, 67, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                                .addComponent(ButtonLess, javax.swing.GroupLayout.PREFERRED_SIZE, 67, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addComponent(ButtonPlus, javax.swing.GroupLayout.PREFERRED_SIZE, 67, javax.swing.GroupLayout.PREFERRED_SIZE))
                            .addGroup(InterfaceLayout.createSequentialGroup()
                                .addGroup(InterfaceLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                                    .addComponent(Button8, javax.swing.GroupLayout.PREFERRED_SIZE, 67, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(Button9, javax.swing.GroupLayout.PREFERRED_SIZE, 67, javax.swing.GroupLayout.PREFERRED_SIZE))
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                                .addGroup(InterfaceLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                                    .addComponent(Button5, javax.swing.GroupLayout.PREFERRED_SIZE, 67, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(Button6, javax.swing.GroupLayout.PREFERRED_SIZE, 67, javax.swing.GroupLayout.PREFERRED_SIZE))
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                                .addGroup(InterfaceLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                                    .addComponent(Button2, javax.swing.GroupLayout.PREFERRED_SIZE, 67, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(Button3, javax.swing.GroupLayout.PREFERRED_SIZE, 67, javax.swing.GroupLayout.PREFERRED_SIZE))
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addGroup(InterfaceLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                                    .addComponent(Button0, javax.swing.GroupLayout.PREFERRED_SIZE, 67, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(ButtonEq, javax.swing.GroupLayout.PREFERRED_SIZE, 67, javax.swing.GroupLayout.PREFERRED_SIZE))))))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jLabel1))
        );

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(Interface)
                .addContainerGap())
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(Interface)
                .addContainerGap())
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void Button7ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_Button7ActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_Button7ActionPerformed

    private void Button4ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_Button4ActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_Button4ActionPerformed

    private void Button1ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_Button1ActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_Button1ActionPerformed

    private void Button8ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_Button8ActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_Button8ActionPerformed

    private void Button2ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_Button2ActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_Button2ActionPerformed

    private void Button5ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_Button5ActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_Button5ActionPerformed

    private void Button3ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_Button3ActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_Button3ActionPerformed

    private void Button6ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_Button6ActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_Button6ActionPerformed

    private void Button9ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_Button9ActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_Button9ActionPerformed

    private void ButtonDivActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_ButtonDivActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_ButtonDivActionPerformed

    private void ButtonMultActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_ButtonMultActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_ButtonMultActionPerformed

    private void ButtonLessActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_ButtonLessActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_ButtonLessActionPerformed

    private void ButtonCActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_ButtonCActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_ButtonCActionPerformed

    private void Button0ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_Button0ActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_Button0ActionPerformed

    private void ButtonEqActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_ButtonEqActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_ButtonEqActionPerformed

    private void ButtonPlusActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_ButtonPlusActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_ButtonPlusActionPerformed

    private void ButtonOpenParActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_ButtonOpenParActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_ButtonOpenParActionPerformed

    private void ButtonCloseParActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_ButtonCloseParActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_ButtonCloseParActionPerformed

    private void ButtonSqrtActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_ButtonSqrtActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_ButtonSqrtActionPerformed

    private void ButtonExpActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_ButtonExpActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_ButtonExpActionPerformed

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
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(CalculadoraGUI.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(CalculadoraGUI.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(CalculadoraGUI.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(CalculadoraGUI.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new CalculadoraGUI().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton Button0;
    private javax.swing.JButton Button1;
    private javax.swing.JButton Button2;
    private javax.swing.JButton Button3;
    private javax.swing.JButton Button4;
    private javax.swing.JButton Button5;
    private javax.swing.JButton Button6;
    private javax.swing.JButton Button7;
    private javax.swing.JButton Button8;
    private javax.swing.JButton Button9;
    private javax.swing.JButton ButtonC;
    private javax.swing.JButton ButtonClosePar;
    private javax.swing.JButton ButtonDiv;
    private javax.swing.JButton ButtonEq;
    private javax.swing.JButton ButtonExp;
    private javax.swing.JButton ButtonLess;
    private javax.swing.JButton ButtonMult;
    private javax.swing.JButton ButtonOpenPar;
    private javax.swing.JButton ButtonPlus;
    private javax.swing.JButton ButtonSqrt;
    private javax.swing.JDesktopPane Interface;
    private javax.swing.JTextArea Operaciones;
    private javax.swing.JScrollPane Pantalla;
    private javax.swing.JLabel jLabel1;
    // End of variables declaration//GEN-END:variables
}
