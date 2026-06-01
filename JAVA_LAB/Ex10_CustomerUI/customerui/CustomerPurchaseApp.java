package customerui;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.HashMap;

public class CustomerPurchaseApp extends JFrame implements ActionListener {
    JTextField txtMobile, txtCustId, txtItemId, txtQty, txtItemName, txtTotal;
    JButton btnLookup, btnPurchase, btnDiscount, btnPrint;

    HashMap<String, String> customers = new HashMap<>();
    HashMap<String, Double> itemPrices = new HashMap<>();
    HashMap<String, String> itemNames = new HashMap<>();

    public CustomerPurchaseApp() {
        setTitle("Customer Billing Hub");
        setSize(400, 400);
        setLayout(new GridLayout(8, 2, 5, 5));
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        customers.put("9876543210", "CUST01");
        itemPrices.put("ITEM1", 1200.0); itemNames.put("ITEM1", "Formal Shirt");
        itemPrices.put("ITEM2", 1800.0); itemNames.put("ITEM2", "Denim Shirt");

        add(new JLabel("Mobile Number:")); txtMobile = new JTextField(); add(txtMobile);
        add(new JLabel("Customer ID:")); txtCustId = new JTextField(); txtCustId.setEditable(false); add(txtCustId);
        add(new JLabel("Item ID (ITEM1/ITEM2):")); txtItemId = new JTextField(); add(txtItemId);
        add(new JLabel("Quantity:")); txtQty = new JTextField(); add(txtQty);
        add(new JLabel("Item Name:")); txtItemName = new JTextField(); txtItemName.setEditable(false); add(txtItemName);
        add(new JLabel("Total Cost:")); txtTotal = new JTextField(); txtTotal.setEditable(false); add(txtTotal);

        btnLookup = new JButton("Lookup"); add(btnLookup);
        btnPurchase = new JButton("Purchase"); add(btnPurchase);
        btnDiscount = new JButton("Discount"); add(btnDiscount);
        btnPrint = new JButton("Print Bill"); add(btnPrint);

        btnLookup.addActionListener(this);
        btnPurchase.addActionListener(this);
        btnDiscount.addActionListener(this);
        btnPrint.addActionListener(this);
    }

    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == btnLookup) {
            String mobile = txtMobile.getText();
            if (customers.containsKey(mobile)) {
                txtCustId.setText(customers.get(mobile));
            } else {
                String newId = "CUST" + (customers.size() + 1);
                customers.put(mobile, newId);
                txtCustId.setText(newId);
                JOptionPane.showMessageDialog(this, "New Customer Added!");
            }
        } else if (e.getSource() == btnPurchase) {
            try {
                String item = txtItemId.getText().toUpperCase();
                int qty = Integer.parseInt(txtQty.getText());
                if (itemPrices.containsKey(item)) {
                    txtItemName.setText(itemNames.get(item));
                    txtTotal.setText(String.valueOf(itemPrices.get(item) * qty));
                } else {
                    JOptionPane.showMessageDialog(this, "Invalid Item!");
                }
            } catch (Exception ex) {
                JOptionPane.showMessageDialog(this, "Invalid Quantity!");
            }
        } else if (e.getSource() == btnDiscount) {
            String[] options = {"10%", "5%", "15%"};
            int choice = JOptionPane.showOptionDialog(this, "Select Discount", "Discount",
                    JOptionPane.DEFAULT_OPTION, JOptionPane.INFORMATION_MESSAGE, null, options, options[0]);
            double discount = (choice == 0) ? 0.10 : (choice == 1) ? 0.05 : (choice == 2) ? 0.15 : 0;
            double cost = Double.parseDouble(txtTotal.getText());
            txtTotal.setText(String.valueOf(cost * (1 - discount)));
        } else if (e.getSource() == btnPrint) {
            String bill = "Cust ID: " + txtCustId.getText() + "\nItem: " + txtItemName.getText() +
                          "\nQty: " + txtQty.getText() + "\nTotal: " + txtTotal.getText();
            JOptionPane.showMessageDialog(this, bill, "Invoice", JOptionPane.INFORMATION_MESSAGE);
        }
    }

    public static void main(String[] args) {
        new CustomerPurchaseApp().setVisible(true);
    }
}