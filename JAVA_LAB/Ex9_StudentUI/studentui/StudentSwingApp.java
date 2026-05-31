package studentui;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.util.List;

public class StudentSwingApp extends JFrame {
    // GUI Components
    private JTextField txtName, txtUSN, txtAge, txtAddress;
    private JTextField txtSgpa1, txtSgpa2, txtSgpa3, txtSgpa4;
    private JComboBox<String> cmbCategory;
    private JButton btnCompute, btnDone, btnComplete;
    private JTextArea txtOutput;
    
    // Collection list to store students
    private List<Student> studentList;
    private double calculatedCgpa = -1.0;

    // Student Helper Class
    private static class Student {
        String name, usn, address, category;
        int age;
        double cgpa;

        Student(String name, String usn, int age, String address, double cgpa, String category) {
            this.name = name;
            this.usn = usn;
            this.age = age;
            this.address = address;
            this.cgpa = cgpa;
            this.category = category;
        }

        @Override
        public String toString() {
            return String.format("USN: %s | Name: %-15s | Age: %d | Address: %-10s | CGPA: %.2f | Category: %s\n",
                    usn, name, age, address, cgpa, category);
        }
    }

    public StudentSwingApp() {
        studentList = new ArrayList<>();
        
        // Setup Window attributes
        setTitle("Student Information Database System (IS48 Ex-9)");
        setSize(750, 650);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        
        // Master Panel with Cosmic Color Styling
        JPanel mainPanel = new JPanel(new BorderLayout(15, 15));
        mainPanel.setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));
        mainPanel.setBackground(new Color(12, 19, 34)); // Match Solar Eclipse Dark
        
        // Header
        JLabel lblHeader = new JLabel("STUDENT REGISTRATION PORTAL", JLabel.CENTER);
        lblHeader.setFont(new Font("Outfit", Font.BOLD, 22));
        lblHeader.setForeground(new Color(248, 152, 32)); // Java Orange Accent
        mainPanel.add(lblHeader, BorderLayout.NORTH);

        // Input Form (using a 2-column GridBagLayout for alignment)
        JPanel formPanel = new JPanel(new GridBagLayout());
        formPanel.setOpaque(false);
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new java.awt.Insets(6, 6, 6, 6);
        gbc.fill = GridBagConstraints.HORIZONTAL;

        // Form Fields Initialization
        txtName = createStyledField();
        txtUSN = createStyledField();
        txtAge = createStyledField();
        txtAddress = createStyledField();
        txtSgpa1 = createStyledField();
        txtSgpa2 = createStyledField();
        txtSgpa3 = createStyledField();
        txtSgpa4 = createStyledField();
        
        String[] categories = {"General", "OBC", "SC", "ST", "Management"};
        cmbCategory = new JComboBox<>(categories);
        cmbCategory.setFont(new Font("Inter", Font.BOLD, 14));
        cmbCategory.setBackground(new Color(19, 30, 51));
        cmbCategory.setForeground(Color.WHITE);

        // Map inputs in grid
        addFormRow(formPanel, "Student Name:", txtName, gbc, 0, 0);
        addFormRow(formPanel, "USN (10-char Alphanum):", txtUSN, gbc, 1, 0);
        addFormRow(formPanel, "Age (Years):", txtAge, gbc, 2, 0);
        addFormRow(formPanel, "Address:", txtAddress, gbc, 3, 0);
        addFormRow(formPanel, "SGPA - Sem 1:", txtSgpa1, gbc, 4, 0);
        addFormRow(formPanel, "SGPA - Sem 2:", txtSgpa2, gbc, 5, 0);
        addFormRow(formPanel, "SGPA - Sem 3:", txtSgpa3, gbc, 6, 0);
        addFormRow(formPanel, "SGPA - Sem 4:", txtSgpa4, gbc, 7, 0);
        addFormRow(formPanel, "Category Status:", cmbCategory, gbc, 8, 0);

        mainPanel.add(formPanel, BorderLayout.WEST);

        // Right Output Console Area
        JPanel outputPanel = new JPanel(new BorderLayout(10, 10));
        outputPanel.setOpaque(false);
        JLabel lblConsole = new JLabel("COLLECTION REGISTRY CONSOLE");
        lblConsole.setFont(new Font("Outfit", Font.BOLD, 14));
        lblConsole.setForeground(new Color(6, 182, 212)); // Cyan Accent
        outputPanel.add(lblConsole, BorderLayout.NORTH);
        
        txtOutput = new JTextArea(15, 25);
        txtOutput.setEditable(false);
        txtOutput.setFont(new Font("Monospaced", Font.PLAIN, 12));
        txtOutput.setBackground(new Color(7, 11, 19));
        txtOutput.setForeground(new Color(16, 185, 129)); // Emerald Green
        JScrollPane scroll = new JScrollPane(txtOutput);
        outputPanel.add(scroll, BorderLayout.CENTER);

        mainPanel.add(outputPanel, BorderLayout.CENTER);

        // Bottom Action buttons
        JPanel buttonPanel = new JPanel(new FlowLayout(FlowLayout.CENTER, 15, 10));
        buttonPanel.setOpaque(false);
        
        btnCompute = createStyledButton("Compute CGPA", new Color(6, 182, 212));
        btnDone = createStyledButton("Done (Save Record)", new Color(248, 152, 32));
        btnComplete = createStyledButton("Complete (Show List)", new Color(16, 185, 129));
        
        // Initial state restrictions
        btnDone.setEnabled(false);
        
        buttonPanel.add(btnCompute);
        buttonPanel.add(btnDone);
        buttonPanel.add(btnComplete);
        mainPanel.add(buttonPanel, BorderLayout.SOUTH);

        add(mainPanel);

        // ACTION HANDLERS
        btnCompute.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if (validateFields()) {
                    double s1 = Double.parseDouble(txtSgpa1.getText().trim());
                    double s2 = Double.parseDouble(txtSgpa2.getText().trim());
                    double s3 = Double.parseDouble(txtSgpa3.getText().trim());
                    double s4 = Double.parseDouble(txtSgpa4.getText().trim());
                    
                    calculatedCgpa = (s1 + s2 + s3 + s4) / 4.0;
                    JOptionPane.showMessageDialog(StudentSwingApp.this,
                            String.format("Calculated Average CGPA of 4 semesters: %.2f", calculatedCgpa),
                            "CGPA Calculation Complete", JOptionPane.INFORMATION_MESSAGE);
                    
                    btnDone.setEnabled(true); // Allow saving
                }
            }
        });

        btnDone.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if (calculatedCgpa < 0) {
                    JOptionPane.showMessageDialog(StudentSwingApp.this, "Please compute CGPA first!", "Error", JOptionPane.ERROR_MESSAGE);
                    return;
                }
                
                String name = txtName.getText().trim();
                String usn = txtUSN.getText().trim().toUpperCase();
                int age = Integer.parseInt(txtAge.getText().trim());
                String address = txtAddress.getText().trim();
                String category = cmbCategory.getSelectedItem().toString();
                
                // Instantiate and store student
                Student s = new Student(name, usn, age, address, calculatedCgpa, category);
                studentList.add(s);
                
                JOptionPane.showMessageDialog(StudentSwingApp.this, "Student record successfully added to local collection!", "Success", JOptionPane.INFORMATION_MESSAGE);
                
                // Clear input form and reset buttons
                clearForm();
                btnDone.setEnabled(false);
                calculatedCgpa = -1.0;
            }
        });

        btnComplete.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                txtOutput.setText("");
                if (studentList.isEmpty()) {
                    txtOutput.append("Registry collection is empty.");
                    return;
                }
                
                txtOutput.append("--- MSRIT REGISTERED STUDENTS LIST ---\n");
                for (Student s : studentList) {
                    txtOutput.append(s.toString());
                }
            }
        });
    }

    // Helper functions for styling Swing components
    private JTextField createStyledField() {
        JTextField field = new JTextField(12);
        field.setFont(new Font("Inter", Font.PLAIN, 14));
        field.setBackground(new Color(19, 30, 51));
        field.setForeground(Color.WHITE);
        field.setCaretColor(Color.WHITE);
        field.setBorder(BorderFactory.createLineBorder(new Color(30, 41, 59), 1));
        return field;
    }

    private JButton createStyledButton(String text, Color baseColor) {
        JButton btn = new JButton(text);
        btn.setFont(new Font("Outfit", Font.BOLD, 14));
        btn.setBackground(baseColor);
        btn.setForeground(Color.WHITE);
        btn.setFocusPainted(false);
        btn.setBorder(BorderFactory.createEmptyBorder(8, 15, 8, 15));
        return btn;
    }

    private void addFormRow(JPanel panel, String labelText, Component comp, GridBagConstraints gbc, int row, int col) {
        JLabel label = new JLabel(labelText);
        label.setFont(new Font("Inter", Font.BOLD, 12));
        label.setForeground(new Color(148, 163, 184)); // Muted Grey
        
        gbc.gridx = col;
        gbc.gridy = row;
        panel.add(label, gbc);
        
        gbc.gridx = col + 1;
        panel.add(comp, gbc);
    }

    private void clearForm() {
        txtName.setText("");
        txtUSN.setText("");
        txtAge.setText("");
        txtAddress.setText("");
        txtSgpa1.setText("");
        txtSgpa2.setText("");
        txtSgpa3.setText("");
        txtSgpa4.setText("");
        cmbCategory.setSelectedIndex(0);
    }

    // Comprehensive validations
    private boolean validateFields() {
        try {
            String name = txtName.getText().trim();
            String usn = txtUSN.getText().trim();
            String address = txtAddress.getText().trim();
            
            if (name.isEmpty() || usn.isEmpty() || address.isEmpty()) {
                showError("All text fields must be filled!");
                return false;
            }
            
            // USN Regex Validation
            if (!usn.matches("^[a-zA-Z0-9]{10}$")) {
                showError("USN must be exactly 10 alphanumeric characters!");
                return false;
            }
            
            // Age validation
            int age = Integer.parseInt(txtAge.getText().trim());
            if (age < 15 || age > 60) {
                showError("Age must be a valid integer between 15 and 60!");
                return false;
            }
            
            // SGPAs validation
            double[] sgpas = new double[4];
            sgpas[0] = Double.parseDouble(txtSgpa1.getText().trim());
            sgpas[1] = Double.parseDouble(txtSgpa2.getText().trim());
            sgpas[2] = Double.parseDouble(txtSgpa3.getText().trim());
            sgpas[3] = Double.parseDouble(txtSgpa4.getText().trim());
            
            for (int i = 0; i < 4; i++) {
                if (sgpas[i] < 0.0 || sgpas[i] > 10.0) {
                    showError("SGPA for Sem " + (i + 1) + " must be between 0.0 and 10.0!");
                    return false;
                }
            }
            
            return true;
        } catch (NumberFormatException e) {
            showError("Numerical fields (Age, SGPA) contain invalid inputs!");
            return false;
        }
    }

    private void showError(String msg) {
        JOptionPane.showMessageDialog(this, msg, "Validation Error", JOptionPane.ERROR_MESSAGE);
    }

    public static void main(String[] args) {
        // Run Swing application safely
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new StudentSwingApp().setVisible(true);
            }
        });
    }
}
