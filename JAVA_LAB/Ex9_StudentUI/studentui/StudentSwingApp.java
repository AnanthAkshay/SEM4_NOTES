package studentui;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;

public class StudentSwingApp extends JFrame implements ActionListener {
    JTextField txtName, txtUSN, txtAge, txtAddress;
    JTextField txtSgpa1, txtSgpa2, txtSgpa3, txtSgpa4;
    JComboBox<String> cmbCategory;
    JButton btnCompute, btnDone, btnDisplay;
    JTextArea txtOutput;
    
    ArrayList<String> studentRecords = new ArrayList<>();
    double cgpa = -1.0;

    public StudentSwingApp() {
        setTitle("Student Information System");
        setSize(600, 500);
        setLayout(new BorderLayout());
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        JPanel formPanel = new JPanel(new GridLayout(9, 2, 5, 5));
        
        formPanel.add(new JLabel("Name:"));
        txtName = new JTextField(); formPanel.add(txtName);
        
        formPanel.add(new JLabel("USN:"));
        txtUSN = new JTextField(); formPanel.add(txtUSN);
        
        formPanel.add(new JLabel("Age:"));
        txtAge = new JTextField(); formPanel.add(txtAge);
        
        formPanel.add(new JLabel("Address:"));
        txtAddress = new JTextField(); formPanel.add(txtAddress);
        
        formPanel.add(new JLabel("SGPA Sem 1:"));
        txtSgpa1 = new JTextField(); formPanel.add(txtSgpa1);
        
        formPanel.add(new JLabel("SGPA Sem 2:"));
        txtSgpa2 = new JTextField(); formPanel.add(txtSgpa2);
        
        formPanel.add(new JLabel("SGPA Sem 3:"));
        txtSgpa3 = new JTextField(); formPanel.add(txtSgpa3);
        
        formPanel.add(new JLabel("SGPA Sem 4:"));
        txtSgpa4 = new JTextField(); formPanel.add(txtSgpa4);
        
        formPanel.add(new JLabel("Category:"));
        String[] cats = {"General", "OBC", "SC", "ST", "Management"};
        cmbCategory = new JComboBox<>(cats);
        formPanel.add(cmbCategory);

        add(formPanel, BorderLayout.NORTH);

        txtOutput = new JTextArea();
        add(new JScrollPane(txtOutput), BorderLayout.CENTER);

        JPanel btnPanel = new JPanel();
        btnCompute = new JButton("Compute CGPA");
        btnDone = new JButton("Save Record");
        btnDisplay = new JButton("Display All");
        
        btnCompute.addActionListener(this);
        btnDone.addActionListener(this);
        btnDisplay.addActionListener(this);
        
        btnPanel.add(btnCompute);
        btnPanel.add(btnDone);
        btnPanel.add(btnDisplay);
        
        add(btnPanel, BorderLayout.SOUTH);
    }

    public void actionPerformed(ActionEvent e) {
        try {
            if (e.getSource() == btnCompute) {
                double s1 = Double.parseDouble(txtSgpa1.getText());
                double s2 = Double.parseDouble(txtSgpa2.getText());
                double s3 = Double.parseDouble(txtSgpa3.getText());
                double s4 = Double.parseDouble(txtSgpa4.getText());
                cgpa = (s1 + s2 + s3 + s4) / 4.0;
                JOptionPane.showMessageDialog(this, "CGPA Calculated: " + cgpa);
            } else if (e.getSource() == btnDone) {
                if (cgpa == -1.0) {
                    JOptionPane.showMessageDialog(this, "Compute CGPA first!");
                    return;
                }
                String record = txtName.getText() + " | " + txtUSN.getText() + " | Age: " + txtAge.getText() +
                        " | Addr: " + txtAddress.getText() + " | Cat: " + cmbCategory.getSelectedItem() +
                        " | CGPA: " + cgpa;
                studentRecords.add(record);
                JOptionPane.showMessageDialog(this, "Record Saved!");
                cgpa = -1.0; // Reset
            } else if (e.getSource() == btnDisplay) {
                txtOutput.setText("");
                for (String s : studentRecords) {
                    txtOutput.append(s + "\n");
                }
            }
        } catch (Exception ex) {
            JOptionPane.showMessageDialog(this, "Invalid input! Please enter correct values.");
        }
    }

    public static void main(String[] args) {
        new StudentSwingApp().setVisible(true);
    }
}