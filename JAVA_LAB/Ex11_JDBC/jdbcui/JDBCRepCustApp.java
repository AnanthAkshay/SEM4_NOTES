package jdbcui;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.*;

public class JDBCRepCustApp extends JFrame {
    // DB details
    private static final String DB_URL = "jdbc:mysql://localhost:3306/advanced_java_db?useSSL=false&allowPublicKeyRetrieval=true";
    private static final String DB_USER = "root";
    private static final String DB_PASS = "admin";

    // Insert Panel Fields (Rep)
    private JTextField txtRepNo, txtRepName, txtRepState, txtRepCommission, txtRepRate;
    // Insert Panel Fields (Cust)
    private JTextField txtCustNo, txtCustName, txtCustState, txtCustLimit, txtCustRepNo;
    
    // Display Area
    private JTextArea txtDisplayConsole;
    private JButton btnInsertRep, btnInsertCust, btnFetchReps;

    public JDBCRepCustApp() {
        setTitle("JDBC MySQL Representative & Customer Portal (IS48 Ex-11)");
        setSize(800, 600);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        // Try initializing database tables
        initializeDatabaseSchema();

        // Main Tabbed Layout to switch between insert forms and display views
        JTabbedPane tabbedPane = new JTabbedPane();
        tabbedPane.setFont(new Font("Outfit", Font.BOLD, 13));
        
        // ---------------- TAB 1: INSERT DATA ----------------
        JPanel insertTab = new JPanel(new GridLayout(1, 2, 20, 20));
        insertTab.setBorder(BorderFactory.createEmptyBorder(15, 15, 15, 15));
        insertTab.setBackground(new Color(12, 19, 34));

        // Sub-Panel A: Representative Form
        JPanel repPanel = new JPanel(new GridLayout(6, 2, 10, 10));
        repPanel.setBorder(BorderFactory.createTitledBorder(
                BorderFactory.createLineBorder(new Color(30, 41, 59)), "Insert Representative Details",
                0, 0, new Font("Outfit", Font.BOLD, 12), new Color(248, 152, 32)));
        repPanel.setOpaque(false);
        
        txtRepNo = createStyledField();
        txtRepName = createStyledField();
        txtRepState = createStyledField();
        txtRepCommission = createStyledField();
        txtRepRate = createStyledField();
        btnInsertRep = createStyledButton("Insert Rep Record", new Color(248, 152, 32));

        addLabel(repPanel, "Rep Number:"); repPanel.add(txtRepNo);
        addLabel(repPanel, "Rep Name:"); repPanel.add(txtRepName);
        addLabel(repPanel, "State:"); repPanel.add(txtRepState);
        addLabel(repPanel, "Commission Amount:"); repPanel.add(txtRepCommission);
        addLabel(repPanel, "Commission Rate (%):"); repPanel.add(txtRepRate);
        repPanel.add(new JLabel("")); repPanel.add(btnInsertRep);
        insertTab.add(repPanel);

        // Sub-Panel B: Customer Form
        JPanel custPanel = new JPanel(new GridLayout(6, 2, 10, 10));
        custPanel.setBorder(BorderFactory.createTitledBorder(
                BorderFactory.createLineBorder(new Color(30, 41, 59)), "Insert Customer Details",
                0, 0, new Font("Outfit", Font.BOLD, 12), new Color(6, 182, 212)));
        custPanel.setOpaque(false);

        txtCustNo = createStyledField();
        txtCustName = createStyledField();
        txtCustState = createStyledField();
        txtCustLimit = createStyledField();
        txtCustRepNo = createStyledField();
        btnInsertCust = createStyledButton("Insert Customer Record", new Color(6, 182, 212));

        addLabel(custPanel, "Customer Number:"); custPanel.add(txtCustNo);
        addLabel(custPanel, "Customer Name:"); custPanel.add(txtCustName);
        addLabel(custPanel, "State:"); custPanel.add(txtCustState);
        addLabel(custPanel, "Credit Limit (INR):"); custPanel.add(txtCustLimit);
        addLabel(custPanel, "Associated Rep No:"); custPanel.add(txtCustRepNo);
        custPanel.add(new JLabel("")); custPanel.add(btnInsertCust);
        insertTab.add(custPanel);
        
        tabbedPane.addTab("📥 Data Entry Panel", insertTab);

        // ---------------- TAB 2: QUERY CONSOLE ----------------
        JPanel queryTab = new JPanel(new BorderLayout(15, 15));
        queryTab.setBorder(BorderFactory.createEmptyBorder(15, 15, 15, 15));
        queryTab.setBackground(new Color(7, 11, 19));

        JPanel northBar = new JPanel(new FlowLayout(FlowLayout.LEFT));
        northBar.setOpaque(false);
        btnFetchReps = createStyledButton("Display Representatives for Credit Limit > 15,000", new Color(16, 185, 129));
        northBar.add(btnFetchReps);
        queryTab.add(northBar, BorderLayout.NORTH);

        txtDisplayConsole = new JTextArea();
        txtDisplayConsole.setEditable(false);
        txtDisplayConsole.setFont(new Font("Monospaced", Font.PLAIN, 12));
        txtDisplayConsole.setBackground(new Color(12, 19, 34));
        txtDisplayConsole.setForeground(new Color(16, 185, 129));
        JScrollPane scrollPane = new JScrollPane(txtDisplayConsole);
        queryTab.add(scrollPane, BorderLayout.CENTER);

        tabbedPane.addTab("🖥️ Database Query Console", queryTab);

        add(tabbedPane);

        // ACTION EVENT LISTENERS
        btnInsertRep.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    int repNo = Integer.parseInt(txtRepNo.getText().trim());
                    String name = txtRepName.getText().trim();
                    String state = txtRepState.getText().trim();
                    double commission = Double.parseDouble(txtRepCommission.getText().trim());
                    double rate = Double.parseDouble(txtRepRate.getText().trim());

                    if (name.isEmpty() || state.isEmpty()) {
                        showError("Text fields cannot be empty!");
                        return;
                    }

                    insertRepresentativeRecord(repNo, name, state, commission, rate);
                    JOptionPane.showMessageDialog(JDBCRepCustApp.this, "Representative record successfully added to MySQL database!", "Success", JOptionPane.INFORMATION_MESSAGE);
                    clearRepFields();

                } catch (NumberFormatException ex) {
                    showError("Invalid numerical entries!");
                }
            }
        });

        btnInsertCust.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    int custNo = Integer.parseInt(txtCustNo.getText().trim());
                    String name = txtCustName.getText().trim();
                    String state = txtCustState.getText().trim();
                    double limit = Double.parseDouble(txtCustLimit.getText().trim());
                    int repNo = Integer.parseInt(txtCustRepNo.getText().trim());

                    if (name.isEmpty() || state.isEmpty()) {
                        showError("Text fields cannot be empty!");
                        return;
                    }

                    insertCustomerRecord(custNo, name, state, limit, repNo);
                    JOptionPane.showMessageDialog(JDBCRepCustApp.this, "Customer record successfully added to MySQL database!", "Success", JOptionPane.INFORMATION_MESSAGE);
                    clearCustFields();

                } catch (NumberFormatException ex) {
                    showError("Invalid numerical entries!");
                }
            }
        });

        btnFetchReps.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                fetchHighCreditReps();
            }
        });
    }

    // JDBC Database operations
    private Connection getConnection() throws SQLException {
        return DriverManager.getConnection(DB_URL, DB_USER, DB_PASS);
    }

    private void initializeDatabaseSchema() {
        try {
            // Load driver dynamically
            Class.forName("com.mysql.cj.jdbc.Driver");
            
            try (Connection conn = getConnection(); Statement stmt = conn.createStatement()) {
                // Create database if not exists
                stmt.executeUpdate("CREATE DATABASE IF NOT EXISTS advanced_java_db");
                stmt.executeUpdate("USE advanced_java_db");

                // Create tables
                stmt.executeUpdate("CREATE TABLE IF NOT EXISTS Representative (" +
                        "RepNo INT PRIMARY KEY," +
                        "RepName VARCHAR(100)," +
                        "State VARCHAR(50)," +
                        "Commission DOUBLE," +
                        "Rate DOUBLE)");

                stmt.executeUpdate("CREATE TABLE IF NOT EXISTS Customer (" +
                        "CustNo INT PRIMARY KEY," +
                        "CustName VARCHAR(100)," +
                        "State VARCHAR(50)," +
                        "Credit_Limit DOUBLE," +
                        "RepNo INT," +
                        "FOREIGN KEY (RepNo) REFERENCES Representative(RepNo))");

                System.out.println("JDBC Schema Initialization Complete.");
            }
        } catch (ClassNotFoundException ex) {
            System.err.println("MySQL JDBC Driver missing. Ensure mysql-connector-j jar is present in classpath.");
        } catch (SQLException ex) {
            System.err.println("SQLException: " + ex.getMessage());
        }
    }

    private void insertRepresentativeRecord(int repNo, String name, String state, double comm, double rate) {
        String sql = "INSERT INTO Representative (RepNo, RepName, State, Commission, Rate) VALUES (?, ?, ?, ?, ?) " +
                "ON DUPLICATE KEY UPDATE RepName=?, State=?, Commission=?, Rate=?";
        try (Connection conn = getConnection(); PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setInt(1, repNo);
            pstmt.setString(2, name);
            pstmt.setString(3, state);
            pstmt.setDouble(4, comm);
            pstmt.setDouble(5, rate);
            // for update values
            pstmt.setString(6, name);
            pstmt.setString(7, state);
            pstmt.setDouble(8, comm);
            pstmt.setDouble(9, rate);
            pstmt.executeUpdate();
        } catch (SQLException ex) {
            showError("SQL Exception: " + ex.getMessage());
        }
    }

    private void insertCustomerRecord(int custNo, String name, String state, double limit, int repNo) {
        String sql = "INSERT INTO Customer (CustNo, CustName, State, Credit_Limit, RepNo) VALUES (?, ?, ?, ?, ?) " +
                "ON DUPLICATE KEY UPDATE CustName=?, State=?, Credit_Limit=?, RepNo=?";
        try (Connection conn = getConnection(); PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setInt(1, custNo);
            pstmt.setString(2, name);
            pstmt.setString(3, state);
            pstmt.setDouble(4, limit);
            pstmt.setInt(5, repNo);
            // for update
            pstmt.setString(6, name);
            pstmt.setString(7, state);
            pstmt.setDouble(8, limit);
            pstmt.setInt(9, repNo);
            pstmt.executeUpdate();
        } catch (SQLException ex) {
            showError("SQL Exception: " + ex.getMessage());
        }
    }

    private void fetchHighCreditReps() {
        txtDisplayConsole.setText("");
        txtDisplayConsole.append("Querying database: FETCH Representatives whose Customers have Credit_Limit > 15,000...\n\n");
        txtDisplayConsole.append(String.format("%-10s | %-20s | %-12s | %-12s | %-10s\n", "RepNo", "RepName", "State", "Commission", "Rate"));
        txtDisplayConsole.append("----------------------------------------------------------------------------\n");

        String sql = "SELECT DISTINCT r.RepNo, r.RepName, r.State, r.Commission, r.Rate " +
                     "FROM Representative r INNER JOIN Customer c ON r.RepNo = c.RepNo " +
                     "WHERE c.Credit_Limit > 15000";

        try (Connection conn = getConnection(); Statement stmt = conn.createStatement(); ResultSet rs = stmt.executeQuery(sql)) {
            int count = 0;
            while (rs.next()) {
                count++;
                txtDisplayConsole.append(String.format("%-10d | %-20s | %-12s | %-12.2f | %-10.2f\n",
                        rs.getInt("RepNo"),
                        rs.getString("RepName"),
                        rs.getString("State"),
                        rs.getDouble("Commission"),
                        rs.getDouble("Rate")));
            }
            txtDisplayConsole.append("\nQuery finished. " + count + " records returned.");
        } catch (SQLException ex) {
            txtDisplayConsole.append("❌ SQL ERROR: Unable to fetch data.\nDetail: " + ex.getMessage());
        }
    }

    private JTextField createStyledField() {
        JTextField field = new JTextField();
        field.setFont(new Font("Inter", Font.PLAIN, 14));
        field.setBackground(new Color(19, 30, 51));
        field.setForeground(Color.WHITE);
        field.setCaretColor(Color.WHITE);
        field.setBorder(BorderFactory.createLineBorder(new Color(30, 41, 59), 1));
        return field;
    }

    private JButton createStyledButton(String text, Color baseColor) {
        JButton btn = new JButton(text);
        btn.setFont(new Font("Outfit", Font.BOLD, 13));
        btn.setBackground(baseColor);
        btn.setForeground(Color.WHITE);
        btn.setFocusPainted(false);
        return btn;
    }

    private void addLabel(JPanel panel, String labelText) {
        JLabel label = new JLabel(labelText);
        label.setFont(new Font("Inter", Font.BOLD, 11));
        label.setForeground(new Color(148, 163, 184));
        panel.add(label);
    }

    private void clearRepFields() {
        txtRepNo.setText(""); txtRepName.setText(""); txtRepState.setText(""); txtRepCommission.setText(""); txtRepRate.setText("");
    }

    private void clearCustFields() {
        txtCustNo.setText(""); txtCustName.setText(""); txtCustState.setText(""); txtCustLimit.setText(""); txtCustRepNo.setText("");
    }

    private void showError(String msg) {
        JOptionPane.showMessageDialog(this, msg, "Database Error", JOptionPane.ERROR_MESSAGE);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new JDBCRepCustApp().setVisible(true);
            }
        });
    }
}
