package customerui;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.HashMap;
import java.util.Map;

public class CustomerPurchaseApp extends JFrame {
    // Local databases
    private Map<String, String> customerDatabase; // phone -> custId
    private Map<String, Item> itemDatabase; // itemId -> Item
    
    // Components
    private JTextField txtMobile, txtCustId, txtItemId, txtQty, txtItemName, txtTotalCost;
    private JButton btnLookup, btnPurchase, btnDiscounts, btnPrint;

    private static class Item {
        String name;
        double price;

        Item(String name, double price) {
            this.name = name;
            this.price = price;
        }
    }

    public CustomerPurchaseApp() {
        // Mock Databases Setup
        customerDatabase = new HashMap<>();
        customerDatabase.put("9876543210", "CUST-001");
        customerDatabase.put("9988776655", "CUST-002");
        
        itemDatabase = new HashMap<>();
        itemDatabase.put("ITEM-10", new Item("Cotton Polo Shirt", 1200.0));
        itemDatabase.put("ITEM-20", new Item("Denim Regular Shirt", 1800.0));
        itemDatabase.put("ITEM-30", new Item("Oxford Button-Down", 2200.0));

        // Start Login Prompt
        if (!promptLogin()) {
            System.exit(0); // Exit if login fails
        }

        // Initialize Window
        setTitle("MSRIT Customer Billing & Purchase Panel (IS48 Ex-10)");
        setSize(650, 480);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        // Styling Base Panel
        JPanel mainPanel = new JPanel(new BorderLayout(15, 15));
        mainPanel.setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));
        mainPanel.setBackground(new Color(7, 11, 19)); // Cosmic theme

        // Header
        JLabel lblHeader = new JLabel("CUSTOMER PURCHASE REGISTRY", JLabel.CENTER);
        lblHeader.setFont(new Font("Outfit", Font.BOLD, 20));
        lblHeader.setForeground(new Color(248, 152, 32)); // Java Orange
        mainPanel.add(lblHeader, BorderLayout.NORTH);

        // Ingestion panel
        JPanel gridPanel = new JPanel(new GridLayout(6, 2, 10, 10));
        gridPanel.setOpaque(false);

        txtMobile = createStyledField();
        txtCustId = createStyledField();
        txtCustId.setEditable(false);
        txtItemId = createStyledField();
        txtQty = createStyledField();
        txtItemName = createStyledField();
        txtItemName.setEditable(false);
        txtTotalCost = createStyledField();
        txtTotalCost.setEditable(false);

        // Row 1: Mobile Lookups
        JPanel lookupPanel = new JPanel(new BorderLayout(5, 0));
        lookupPanel.setOpaque(false);
        lookupPanel.add(txtMobile, BorderLayout.CENTER);
        btnLookup = createStyledButton("Lookup", new Color(6, 182, 212));
        lookupPanel.add(btnLookup, BorderLayout.EAST);

        addLabel(gridPanel, "Enter Mobile Number:");
        gridPanel.add(lookupPanel);

        addLabel(gridPanel, "Customer ID:");
        gridPanel.add(txtCustId);

        addLabel(gridPanel, "Enter Item ID (ITEM-10/20/30):");
        gridPanel.add(txtItemId);

        addLabel(gridPanel, "Quantity:");
        gridPanel.add(txtQty);

        addLabel(gridPanel, "Item Selected:");
        gridPanel.add(txtItemName);

        addLabel(gridPanel, "Total Cost (INR):");
        gridPanel.add(txtTotalCost);

        mainPanel.add(gridPanel, BorderLayout.CENTER);

        // Actions panel
        JPanel actionPanel = new JPanel(new FlowLayout(FlowLayout.CENTER, 15, 10));
        actionPanel.setOpaque(false);
        btnPurchase = createStyledButton("Purchase Item", new Color(6, 182, 212));
        btnDiscounts = createStyledButton("Show Discounts", new Color(248, 152, 32));
        btnPrint = createStyledButton("Print Receipt", new Color(16, 185, 129));

        btnDiscounts.setEnabled(false);
        btnPrint.setEnabled(false);

        actionPanel.add(btnPurchase);
        actionPanel.add(btnDiscounts);
        actionPanel.add(btnPrint);
        mainPanel.add(actionPanel, BorderLayout.SOUTH);

        add(mainPanel);

        // LISTENERS
        btnLookup.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String mobile = txtMobile.getText().trim();
                if (!mobile.matches("^[0-9]{10}$")) {
                    JOptionPane.showMessageDialog(CustomerPurchaseApp.this, "Mobile number must be exactly 10 digits!", "Input Error", JOptionPane.ERROR_MESSAGE);
                    return;
                }

                if (customerDatabase.containsKey(mobile)) {
                    String id = customerDatabase.get(mobile);
                    txtCustId.setText(id);
                    JOptionPane.showMessageDialog(CustomerPurchaseApp.this, "Welcome back! Existing Customer ID found: " + id, "Customer Verified", JOptionPane.INFORMATION_MESSAGE);
                } else {
                    // Create new customer
                    String id = "CUST-0" + (customerDatabase.size() + 1);
                    customerDatabase.put(mobile, id);
                    txtCustId.setText(id);
                    JOptionPane.showMessageDialog(CustomerPurchaseApp.this, "New Customer Registered! Assigned Customer ID: " + id, "New Customer Added", JOptionPane.INFORMATION_MESSAGE);
                }
            }
        });

        btnPurchase.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String custId = txtCustId.getText().trim();
                String itemId = txtItemId.getText().trim().toUpperCase();
                String qtyStr = txtQty.getText().trim();

                if (custId.isEmpty()) {
                    JOptionPane.showMessageDialog(CustomerPurchaseApp.this, "Please run customer mobile lookup first!", "Error", JOptionPane.WARNING_MESSAGE);
                    return;
                }

                if (!itemDatabase.containsKey(itemId)) {
                    JOptionPane.showMessageDialog(CustomerPurchaseApp.this, "Invalid Item ID! (Available: ITEM-10, ITEM-20, ITEM-30)", "Error", JOptionPane.ERROR_MESSAGE);
                    return;
                }

                try {
                    int qty = Integer.parseInt(qtyStr);
                    if (qty <= 0) {
                        JOptionPane.showMessageDialog(CustomerPurchaseApp.this, "Quantity must be greater than zero!", "Error", JOptionPane.ERROR_MESSAGE);
                        return;
                    }

                    Item item = itemDatabase.get(itemId);
                    double cost = item.price * qty;

                    // Display details
                    txtItemName.setText(item.name);
                    txtTotalCost.setText(String.format("%.2f", cost));

                    btnDiscounts.setEnabled(true);
                    btnPrint.setEnabled(true);

                } catch (NumberFormatException ex) {
                    JOptionPane.showMessageDialog(CustomerPurchaseApp.this, "Quantity must be an integer!", "Error", JOptionPane.ERROR_MESSAGE);
                }
            }
        });

        btnDiscounts.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Option Dialog box displaying discounts
                String[] options = {"Festival Discount (10%)", "New Member Discount (5%)", "Premium Offer (15%)"};
                int selection = JOptionPane.showOptionDialog(
                        CustomerPurchaseApp.this,
                        "Select a discount to apply to this purchase:",
                        "Discount Coupons Portal",
                        JOptionPane.DEFAULT_OPTION,
                        JOptionPane.QUESTION_MESSAGE,
                        null,
                        options,
                        options[0]
                );

                if (selection >= 0) {
                    double discountPercent = (selection == 0) ? 0.10 : (selection == 1) ? 0.05 : 0.15;
                    double currentCost = Double.parseDouble(txtTotalCost.getText());
                    double finalCost = currentCost * (1 - discountPercent);
                    txtTotalCost.setText(String.format("%.2f", finalCost));
                    JOptionPane.showMessageDialog(CustomerPurchaseApp.this, "Applied coupon! Calculated Discount: " + (discountPercent*100) + "%", "Discount Applied", JOptionPane.INFORMATION_MESSAGE);
                }
            }
        });

        btnPrint.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Display receipt in pop-up box
                String receipt = String.format(
                        "====================================\n" +
                        "      MSRIT CLOTHING OUTLET BILL    \n" +
                        "====================================\n" +
                        "Customer ID : %s\n" +
                        "Mobile No   : %s\n" +
                        "Item Name   : %s\n" +
                        "Quantity    : %s\n" +
                        "Total Paid  : INR %s\n" +
                        "====================================\n" +
                        "Thank you for shopping with us!",
                        txtCustId.getText(), txtMobile.getText(), txtItemName.getText(), txtQty.getText(), txtTotalCost.getText()
                );
                
                JOptionPane.showMessageDialog(CustomerPurchaseApp.this, receipt, "Purchase Invoice Receipt", JOptionPane.INFORMATION_MESSAGE);
            }
        });
    }

    private boolean promptLogin() {
        JPanel loginPanel = new JPanel(new GridLayout(2, 2, 5, 5));
        JTextField username = new JTextField();
        JPasswordField password = new JPasswordField();
        loginPanel.add(new JLabel("Username:"));
        loginPanel.add(username);
        loginPanel.add(new JLabel("Password:"));
        loginPanel.add(password);

        int result = JOptionPane.showConfirmDialog(
                null,
                loginPanel,
                "Billing Terminal Secure Login",
                JOptionPane.OK_CANCEL_OPTION,
                JOptionPane.PLAIN_MESSAGE
        );

        if (result == JOptionPane.OK_OPTION) {
            String user = username.getText().trim();
            String pass = new String(password.getPassword());
            if (user.equals("admin") && pass.equals("is48")) {
                JOptionPane.showMessageDialog(null, "Login Successful! Welcome to the Terminal.", "Success", JOptionPane.INFORMATION_MESSAGE);
                return true;
            } else {
                JOptionPane.showMessageDialog(null, "Invalid Credentials! Access Denied.", "Login Failed", JOptionPane.ERROR_MESSAGE);
                return false;
            }
        }
        return false;
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
        btn.setFont(new Font("Outfit", Font.BOLD, 14));
        btn.setBackground(baseColor);
        btn.setForeground(Color.WHITE);
        btn.setFocusPainted(false);
        btn.setBorder(BorderFactory.createEmptyBorder(6, 12, 6, 12));
        return btn;
    }

    private void addLabel(JPanel panel, String labelText) {
        JLabel label = new JLabel(labelText);
        label.setFont(new Font("Inter", Font.BOLD, 12));
        label.setForeground(new Color(148, 163, 184));
        panel.add(label);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new CustomerPurchaseApp().setVisible(true);
            }
        });
    }
}
