<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MSRIT Clothing — Premium Shirt Purchase Portal</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800&family=Inter:wght@400;500;600&family=JetBrains+Mono&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-dark: #070b13;
            --bg-panel: #0c1322;
            --bg-card: #131e33;
            --primary: #f89820; /* Amber Orange */
            --primary-hover: #e07f10;
            --border-color: #1e293b;
            --text-primary: #f8fafc;
            --text-secondary: #94a3b8;
            --font-display: 'Outfit', sans-serif;
            --font-sans: 'Inter', sans-serif;
            --font-mono: 'JetBrains Mono', monospace;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: var(--font-sans);
            color: var(--text-secondary);
            background-color: var(--bg-dark);
            line-height: 1.6;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }

        .container {
            width: 100%;
            max-width: 680px;
            background-color: var(--bg-panel);
            border: 1px solid var(--border-color);
            border-radius: 16px;
            padding: 40px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
        }

        h1 {
            font-family: var(--font-display);
            font-size: 2.2rem;
            font-weight: 800;
            text-align: center;
            color: var(--text-primary);
            margin-bottom: 25px;
            letter-spacing: -0.02em;
        }

        h1 span {
            color: var(--primary);
        }

        /* Cost Table */
        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 30px;
            font-size: 0.95rem;
        }

        th {
            background-color: var(--bg-card);
            color: var(--primary);
            font-family: var(--font-display);
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            padding: 12px;
            text-align: left;
            border: 1px solid var(--border-color);
        }

        td {
            padding: 12px;
            border: 1px solid var(--border-color);
            color: var(--text-primary);
        }

        tr:nth-child(even) td {
            background-color: rgba(255, 255, 255, 0.01);
        }

        /* Forms Elements */
        .form-group {
            margin-bottom: 20px;
        }

        label {
            display: block;
            font-weight: 600;
            margin-bottom: 8px;
            color: var(--text-primary);
            font-size: 0.9rem;
        }

        select, input[type="text"] {
            width: 100%;
            padding: 12px 16px;
            background-color: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            color: var(--text-primary);
            outline: none;
            font-size: 0.95rem;
            transition: all 0.3s ease;
        }

        select:focus, input[type="text"]:focus {
            border-color: var(--primary);
        }

        /* Radio Options */
        .radio-group {
            display: flex;
            gap: 20px;
            margin-top: 5px;
        }

        .radio-option {
            display: flex;
            align-items: center;
            gap: 8px;
            cursor: pointer;
            color: var(--text-primary);
            font-size: 0.95rem;
        }

        .radio-option input[type="radio"] {
            accent-color: var(--primary);
            width: 18px;
            height: 18px;
        }

        .btn-submit {
            display: block;
            width: 100%;
            padding: 14px;
            background-color: var(--primary);
            color: white;
            border: none;
            border-radius: 8px;
            font-family: var(--font-display);
            font-weight: 700;
            font-size: 1.1rem;
            cursor: pointer;
            transition: all 0.3s ease;
            margin-top: 30px;
        }

        .btn-submit:hover {
            background-color: var(--primary-hover);
            box-shadow: 0 4px 15px rgba(248, 152, 32, 0.3);
        }

        /* Output Receipt Box */
        .receipt-card {
            background: linear-gradient(135deg, rgba(248, 152, 32, 0.08) 0%, rgba(255, 255, 255, 0.01) 100%);
            border: 1px dashed var(--primary);
            border-radius: 12px;
            padding: 25px;
            margin-top: 35px;
        }

        .receipt-title {
            font-family: var(--font-display);
            font-size: 1.25rem;
            font-weight: 700;
            color: var(--primary);
            margin-bottom: 15px;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 8px;
        }

        .receipt-row {
            display: flex;
            justify-content: space-between;
            margin-bottom: 10px;
            font-size: 0.95rem;
        }

        .receipt-row .label {
            color: var(--text-secondary);
        }

        .receipt-row .val {
            font-weight: 600;
            color: var(--text-primary);
        }

        .receipt-row.total {
            border-top: 1px solid var(--border-color);
            padding-top: 12px;
            font-size: 1.15rem;
            font-weight: bold;
        }

        .receipt-row.total .val {
            color: var(--primary);
            font-family: var(--font-mono);
        }
    </style>
</head>
<body>

    <div class="container">
        <h1>MSRIT <span>Shirt Purchase Portal</span></h1>

        <!-- Shirt Catalog Rates -->
        <table>
            <thead>
                <tr>
                    <th>Shirt Type</th>
                    <th>Base Price (INR)</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Formal Cotton Shirt</td>
                    <td>1,200.00</td>
                </tr>
                <tr>
                    <td>Denim Regular Shirt</td>
                    <td>1,800.00</td>
                </tr>
                <tr>
                    <td>Premium Oxford Weave</td>
                    <td>2,200.00</td>
                </tr>
            </tbody>
        </table>

        <!-- Purchase form -->
        <form method="POST" action="shirt_purchase.jsp">
            <div class="form-group">
                <label for="shirtType">Select Shirt Type:</label>
                <select name="shirtType" id="shirtType">
                    <option value="Formal Cotton">Formal Cotton Shirt</option>
                    <option value="Denim Regular">Denim Regular Shirt</option>
                    <option value="Premium Oxford">Premium Oxford Weave</option>
                </select>
            </div>

            <div class="form-group">
                <label>Select Neck Styling:</label>
                <div class="radio-group">
                    <label class="radio-option">
                        <input type="radio" name="neckType" value="Round Neck" checked>
                        Round Neck
                    </label>
                    <label class="radio-option">
                        <input type="radio" name="neckType" value="V Neck">
                        V Neck
                    </label>
                    <label class="radio-option">
                        <input type="radio" name="neckType" value="Collar">
                        Collar
                    </label>
                </div>
            </div>

            <div class="form-group">
                <label for="quantity">Purchase Quantity:</label>
                <input type="text" name="quantity" id="quantity" placeholder="e.g. 2" required>
            </div>

            <button type="submit" class="btn-submit">Compute Order Total</button>
        </form>

        <!-- JSP Backend Calculation -->
        <%
            String shirtType = request.getParameter("shirtType");
            String neckType = request.getParameter("neckType");
            String qtyStr = request.getParameter("quantity");

            if (shirtType != null && neckType != null && qtyStr != null) {
                try {
                    int qty = Integer.parseInt(qtyStr.trim());
                    if (qty <= 0) {
                        throw new NumberFormatException();
                    }

                    // Price lookups
                    double unitPrice = 0.0;
                    if (shirtType.equals("Formal Cotton")) {
                        unitPrice = 1200.0;
                    } else if (shirtType.equals("Denim Regular")) {
                        unitPrice = 1800.0;
                    } else if (shirtType.equals("Premium Oxford")) {
                        unitPrice = 2200.0;
                    }

                    double totalCost = unitPrice * qty;
        %>
                    <!-- Display Computed Receipt -->
                    <div class="receipt-card">
                        <div class="receipt-title">🛒 Purchase Invoice Summary</div>
                        <div class="receipt-row">
                            <span class="label">Shirt Type Selection:</span>
                            <span class="val"><%= shirtType %></span>
                        </div>
                        <div class="receipt-row">
                            <span class="label">Neck Cut Styling:</span>
                            <span class="val"><%= neckType %></span>
                        </div>
                        <div class="receipt-row">
                            <span class="label">Unit Base Price:</span>
                            <span class="val">INR <%= String.format("%.2f", unitPrice) %></span>
                        </div>
                        <div class="receipt-row">
                            <span class="label">Quantity Purchased:</span>
                            <span class="val"><%= qty %> units</span>
                        </div>
                        <div class="receipt-row total">
                            <span class="label" style="color:var(--text-primary);">Total Billing Cost:</span>
                            <span class="val">INR <%= String.format("%.2f", totalCost) %></span>
                        </div>
                    </div>
        <%
                } catch (NumberFormatException e) {
        %>
                    <div class="receipt-card" style="border-color:var(--primary); background:rgba(255, 67, 94, 0.05);">
                        <div class="receipt-title" style="color:var(--primary);">❌ Processing Error</div>
                        <p style="color:var(--text-primary); font-size:0.95rem;">Invalid quantity entered! Quantity must be a positive integer greater than zero.</p>
                    </div>
        <%
                }
            }
        %>

    </div>

</body>
</html>
