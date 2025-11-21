from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'retro-pizza-secret-key-1985'  # Change this in production

# Pizza pricing
SIZE_PRICES = {
    "S": 15,
    "M": 20,
    "L": 25
}

# Topping options with prices
TOPPINGS = {
    "1": {"name": "Pepperoni", "price": {"S": 2, "M": 3, "L": 3}},
    "2": {"name": "Mushrooms", "price": {"S": 1.5, "M": 2, "L": 2.5}},
    "3": {"name": "Olives", "price": {"S": 1.5, "M": 2, "L": 2.5}},
    "4": {"name": "Green Peppers", "price": {"S": 1, "M": 1.5, "L": 2}},
    "5": {"name": "Onions", "price": {"S": 1, "M": 1.5, "L": 2}},
    "6": {"name": "Sausage", "price": {"S": 2.5, "M": 3, "L": 3.5}},
    "7": {"name": "Bacon", "price": {"S": 2.5, "M": 3, "L": 3.5}},
    "8": {"name": "Pineapple", "price": {"S": 1.5, "M": 2, "L": 2.5}},
    "9": {"name": "Jalapeños", "price": {"S": 1.5, "M": 2, "L": 2.5}},
    "10": {"name": "Extra Cheese", "price": {"S": 1, "M": 1, "L": 1}},
    "11": {"name": "Chicken", "price": {"S": 2.5, "M": 3, "L": 3.5}},
    "12": {"name": "Anchovies", "price": {"S": 2, "M": 2.5, "L": 3}}
}

# Special combo deals
COMBO_DEALS = {
    "meat_lovers": {
        "toppings": ["Pepperoni", "Sausage", "Bacon", "Chicken"],
        "discount": 0.15,
        "name": "Meat Lovers Combo"
    },
    "veggie_delight": {
        "toppings": ["Mushrooms", "Olives", "Green Peppers", "Onions"],
        "discount": 0.12,
        "name": "Veggie Delight Combo"
    },
    "supreme": {
        "toppings": ["Pepperoni", "Mushrooms", "Olives", "Green Peppers", "Onions", "Sausage"],
        "discount": 0.20,
        "name": "Supreme Combo"
    },
    "hawaiian": {
        "toppings": ["Pineapple", "Chicken"],
        "discount": 0.10,
        "name": "Hawaiian Combo"
    }
}

def calculate_combo_discount(selected_toppings, base_total):
    """Check if user qualifies for any combo deals"""
    best_discount = 0
    best_combo = None
    
    for combo_name, combo_info in COMBO_DEALS.items():
        required_toppings = set(combo_info["toppings"])
        selected_set = set(selected_toppings)
        
        if required_toppings.issubset(selected_set):
            discount_amount = base_total * combo_info["discount"]
            if discount_amount > best_discount:
                best_discount = discount_amount
                best_combo = combo_info
    
    return best_combo, best_discount

def calculate_bill(size, selected_toppings):
    """Calculate the total bill"""
    base_price = SIZE_PRICES[size]
    bill = base_price
    
    topping_costs = []
    for topping_name in selected_toppings:
        for key, topping in TOPPINGS.items():
            if topping["name"] == topping_name:
                cost = topping["price"][size]
                topping_costs.append((topping_name, cost))
                bill += cost
                break
    
    combo, discount = calculate_combo_discount(selected_toppings, bill)
    
    if combo:
        bill -= discount
        return bill, base_price, topping_costs, combo, discount
    
    return bill, base_price, topping_costs, None, 0

@app.route('/')
def index():
    """Main page with pizza ordering form"""
    # Calculate discount percentage for template
    combo_deals_with_percent = {}
    for key, combo in COMBO_DEALS.items():
        combo_deals_with_percent[key] = {
            **combo,
            'discount_percent': int(combo['discount'] * 100)
        }
    
    return render_template('index.html', 
                         size_prices=SIZE_PRICES, 
                         toppings=TOPPINGS,
                         combo_deals=combo_deals_with_percent)

@app.route('/calculate', methods=['POST'])
def calculate():
    """Calculate pizza order and show receipt"""
    size = request.form.get('size', '').upper()
    selected_toppings = request.form.getlist('toppings')
    
    # Validate size
    if size not in SIZE_PRICES:
        return redirect(url_for('index'))
    
    # Get topping names from IDs
    topping_names = []
    for topping_id in selected_toppings:
        if topping_id in TOPPINGS:
            topping_names.append(TOPPINGS[topping_id]["name"])
    
    # Calculate bill
    bill, base_price, topping_costs, combo, discount = calculate_bill(size, topping_names)
    
    size_name = {"S": "Small", "M": "Medium", "L": "Large"}[size]
    subtotal = base_price + sum(cost for _, cost in topping_costs)
    
    # Add discount percentage to combo if exists and format numbers
    if combo:
        combo = {**combo, 'discount_percent': int(combo['discount'] * 100)}
    
    # Format numbers for display
    base_price_fmt = f"{base_price:.2f}"
    subtotal_fmt = f"{subtotal:.2f}"
    total_fmt = f"{bill:.2f}"
    discount_fmt = f"{discount:.2f}" if discount > 0 else "0.00"
    topping_costs_fmt = [(name, f"{cost:.2f}") for name, cost in topping_costs]
    
    return render_template('receipt.html',
                         size=size,
                         size_name=size_name,
                         base_price=base_price,
                         base_price_fmt=base_price_fmt,
                         topping_costs=topping_costs_fmt,
                         subtotal=subtotal,
                         subtotal_fmt=subtotal_fmt,
                         combo=combo,
                         discount=discount,
                         discount_fmt=discount_fmt,
                         total=bill,
                         total_fmt=total_fmt,
                         size_prices=SIZE_PRICES,
                         toppings=TOPPINGS)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
