<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
    <title>Shirt Purchase Portal</title>
</head>
<body>
    <h2>Shirt Purchase Portal</h2>
    <form method="POST" action="shirt_purchase.jsp">
        <label>Select Shirt Type:</label>
        <select name="shirtType">
            <option value="Formal Cotton">Formal Cotton Shirt (1200)</option>
            <option value="Denim Regular">Denim Regular Shirt (1800)</option>
            <option value="Premium Oxford">Premium Oxford Weave (2200)</option>
        </select><br><br>
        
        <label>Select Neck Styling:</label>
        <input type="radio" name="neckType" value="Round Neck" checked> Round Neck
        <input type="radio" name="neckType" value="V Neck"> V Neck
        <input type="radio" name="neckType" value="Collar"> Collar<br><br>
        
        <label>Quantity:</label>
        <input type="text" name="quantity" required><br><br>
        
        <button type="submit">Compute Total</button>
    </form>

    <% 
        String shirtType = request.getParameter("shirtType");
        String neckType = request.getParameter("neckType");
        String qtyStr = request.getParameter("quantity");
        
        if (shirtType != null && qtyStr != null) {
            try {
                int qty = Integer.parseInt(qtyStr);
                double price = shirtType.equals("Formal Cotton") ? 1200 : shirtType.equals("Denim Regular") ? 1800 : 2200;
                double total = price * qty;
    %>
                <h3>Purchase Summary:</h3>
                <p>Shirt: <%= shirtType %></p>
                <p>Neck: <%= neckType %></p>
                <p>Quantity: <%= qty %></p>
                <p><b>Total Cost: INR <%= total %></b></p>
    <% 
            } catch (Exception e) {
                out.println("<p style='color:red;'>Invalid Quantity!</p>");
            }
        }
    %>
</body>
</html>