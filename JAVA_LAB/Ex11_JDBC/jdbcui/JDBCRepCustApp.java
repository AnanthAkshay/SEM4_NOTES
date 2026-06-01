package jdbcui;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.*;

public class JDBCRepCustApp extends JFrame implements ActionListener {
    JTextField txtRepNo, txtRepName, txtState, txtComm, txtRate;
    JTextField txtCustNo, txtCustName, txtCustState, txtLimit, txtCustRepNo;
    JButton btnInsertRep, btnInsertCust, btnFetch;
    JTextArea txtDisplay;

    public JDBCRepCustApp() {
        setTitle("JDBC MySQL Portal");
        setSize(700, 600);
        setLayout(new BorderLayout());
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JPanel panel = new JPanel(new GridLayout(6, 4, 5, 5));
        
        panel.add(new JLabel("Rep No:")); txtRepNo = new JTextField(); panel.add(txtRepNo);
        panel.add(new JLabel("Cust No:")); txtCustNo = new JTextField(); panel.add(txtCustNo);
        
        panel.add(new JLabel("Rep Name:")); txtRepName = new JTextField(); panel.add(txtRepName);
        panel.add(new JLabel("Cust Name:")); txtCustName = new JTextField(); panel.add(txtCustName);
        
        panel.add(new JLabel("Rep State:")); txtState = new JTextField(); panel.add(txtState);
        panel.add(new JLabel("Cust State:")); txtCustState = new JTextField(); panel.add(txtCustState);
        
        panel.add(new JLabel("Commission:")); txtComm = new JTextField(); panel.add(txtComm);
        panel.add(new JLabel("Credit Limit:")); txtLimit = new JTextField(); panel.add(txtLimit);
        
        panel.add(new JLabel("Rate:")); txtRate = new JTextField(); panel.add(txtRate);
        panel.add(new JLabel("Cust Rep No:")); txtCustRepNo = new JTextField(); panel.add(txtCustRepNo);

        btnInsertRep = new JButton("Insert Rep"); panel.add(btnInsertRep);
        btnInsertCust = new JButton("Insert Cust"); panel.add(btnInsertCust);
        
        add(panel, BorderLayout.NORTH);

        txtDisplay = new JTextArea();
        add(new JScrollPane(txtDisplay), BorderLayout.CENTER);

        btnFetch = new JButton("Fetch Reps (Limit > 15000)");
        add(btnFetch, BorderLayout.SOUTH);

        btnInsertRep.addActionListener(this);
        btnInsertCust.addActionListener(this);
        btnFetch.addActionListener(this);
    }

    public void actionPerformed(ActionEvent e) {
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/db", "root", "admin");
             Statement stmt = conn.createStatement()) {
            
            if (e.getSource() == btnInsertRep) {
                String sql = "INSERT INTO Representative VALUES (" + txtRepNo.getText() + ",'" + 
                             txtRepName.getText() + "','" + txtState.getText() + "'," + 
                             txtComm.getText() + "," + txtRate.getText() + ")";
                stmt.executeUpdate(sql);
                JOptionPane.showMessageDialog(this, "Representative Inserted");
            } else if (e.getSource() == btnInsertCust) {
                String sql = "INSERT INTO Customer VALUES (" + txtCustNo.getText() + ",'" + 
                             txtCustName.getText() + "','" + txtCustState.getText() + "'," + 
                             txtLimit.getText() + "," + txtCustRepNo.getText() + ")";
                stmt.executeUpdate(sql);
                JOptionPane.showMessageDialog(this, "Customer Inserted");
            } else if (e.getSource() == btnFetch) {
                String sql = "SELECT r.* FROM Representative r JOIN Customer c ON r.RepNo = c.RepNo WHERE c.Credit_Limit > 15000";
                ResultSet rs = stmt.executeQuery(sql);
                txtDisplay.setText("Reps with Customer Limit > 15000:\n");
                while (rs.next()) {
                    txtDisplay.append(rs.getString(1) + " | " + rs.getString(2) + " | " + rs.getString(3) + "\n");
                }
            }
        } catch (Exception ex) {
            JOptionPane.showMessageDialog(this, "Error: " + ex.getMessage());
        }
    }

    public static void main(String[] args) {
        new JDBCRepCustApp().setVisible(true);
    }
}