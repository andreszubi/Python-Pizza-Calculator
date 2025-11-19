import sys

def print_header():
    """Print a fun welcome header"""
    print("\n" + "="*50)
    print("🍕 WELCOME TO PYTHON PIZZA DELIVERIES! 🍕")
    print("="*50 + "\n")

def print_separator():
    """Print a separator line"""
    print("-" * 50)

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
        "discount": 0.15,  # 15% off
        "name": "Meat Lovers Combo"
    },
    "veggie_delight": {
        "toppings": ["Mushrooms", "Olives", "Green Peppers", "Onions"],
        "discount": 0.12,  # 12% off
        "name": "Veggie Delight Combo"
    },
    "supreme": {
        "toppings": ["Pepperoni", "Mushrooms", "Olives", "Green Peppers", "Onions", "Sausage"],
        "discount": 0.20,  # 20% off
        "name": "Supreme Combo"
    },
    "hawaiian": {
        "toppings": ["Pineapple", "Chicken"],
        "discount": 0.10,  # 10% off
        "name": "Hawaiian Combo"
    }
}

def get_pizza_size():
    """Get and validate pizza size"""
    while True:
        size = input(f"What size pizza do you want? (S:${SIZE_PRICES['S']}/M:${SIZE_PRICES['M']}/L:${SIZE_PRICES['L']}):\n").upper().strip()
        if size in SIZE_PRICES:
            return size
        print("❌ Invalid size! Please choose S, M, or L.\n")
        print(f"Valid sizes: S:${SIZE_PRICES['S']}, M:${SIZE_PRICES['M']}, L:${SIZE_PRICES['L']}\n")

def display_toppings_menu():
    """Display available toppings"""
    print("\n📋 AVAILABLE TOPPINGS:")
    print_separator()
    for key, topping in TOPPINGS.items():
        print(f"{key:>3}. {topping['name']:<20} ${topping['price']['M']:.2f} (M size)")
    print_separator()

def get_toppings(size):
    """Get toppings selection from user"""
    selected_toppings = []
    display_toppings_menu()
    
    print(f"\n💡 Tip: You can select multiple toppings! Enter numbers separated by commas.")
    print(f"💡 Or type 'DONE' when you're finished selecting toppings.\n")
    
    while True:
        choice = input("Select topping(s) by number (or 'DONE' to finish):\n").strip().upper()
        
        if choice == "DONE":
            if not selected_toppings:
                print("⚠️  You haven't selected any toppings yet! Add at least one or type 'DONE' again to skip.\n")
                continue
            break
        
        # Handle comma-separated selections
        choices = [c.strip() for c in choice.split(",")]
        
        for c in choices:
            if c in TOPPINGS:
                topping_name = TOPPINGS[c]["name"]
                if topping_name not in selected_toppings:
                    selected_toppings.append(topping_name)
                    price = TOPPINGS[c]["price"][size]
                    print(f"✅ Added {topping_name} (+${price:.2f})")
                else:
                    print(f"⚠️  {topping_name} is already on your pizza!")
            else:
                print(f"❌ Invalid selection: {c}")
    
    return selected_toppings

def calculate_combo_discount(selected_toppings, base_total):
    """Check if user qualifies for any combo deals"""
    best_discount = 0
    best_combo = None
    
    for combo_name, combo_info in COMBO_DEALS.items():
        required_toppings = set(combo_info["toppings"])
        selected_set = set(selected_toppings)
        
        # Check if all required toppings are selected
        if required_toppings.issubset(selected_set):
            discount_amount = base_total * combo_info["discount"]
            if discount_amount > best_discount:
                best_discount = discount_amount
                best_combo = combo_info
    
    return best_combo, best_discount

def calculate_bill(size, selected_toppings):
    """Calculate the total bill"""
    # Base price
    base_price = SIZE_PRICES[size]
    bill = base_price
    
    # Add topping prices
    topping_costs = []
    for topping_name in selected_toppings:
        # Find the topping key
        for key, topping in TOPPINGS.items():
            if topping["name"] == topping_name:
                cost = topping["price"][size]
                topping_costs.append((topping_name, cost))
                bill += cost
                break
    
    # Check for combo deals
    combo, discount = calculate_combo_discount(selected_toppings, bill)
    
    if combo:
        bill -= discount
        return bill, base_price, topping_costs, combo, discount
    
    return bill, base_price, topping_costs, None, 0

def display_receipt(size, selected_toppings, bill_details):
    """Display a nice receipt"""
    bill, base_price, topping_costs, combo, discount = bill_details
    
    print("\n" + "="*50)
    print("🧾 YOUR PIZZA ORDER RECEIPT")
    print("="*50)
    
    size_name = {"S": "Small", "M": "Medium", "L": "Large"}[size]
    print(f"\n🍕 {size_name} Pizza: ${base_price:.2f}")
    
    if topping_costs:
        print("\n📌 Toppings:")
        for topping_name, cost in topping_costs:
            print(f"   • {topping_name:<20} ${cost:.2f}")
    else:
        print("\n📌 No toppings selected")
    
    subtotal = base_price + sum(cost for _, cost in topping_costs)
    
    if combo:
        print(f"\n🎉 SPECIAL DEAL: {combo['name']}!")
        print(f"   Discount ({combo['discount']*100:.0f}% off): -${discount:.2f}")
    
    print("\n" + "-"*50)
    print(f"💰 TOTAL: ${bill:.2f}")
    print("="*50)
    
    if combo:
        print(f"\n🎊 Congratulations! You saved ${discount:.2f} with the {combo['name']}!")
    
    print("\n🍕 Enjoy your pizza! 🍕\n")

def main():
    """Main function to run the pizza calculator"""
    print_header()
    
    # Get pizza size
    size = get_pizza_size()
    print(f"\n✅ Great choice! {size} size pizza selected.\n")
    
    # Get toppings
    selected_toppings = get_toppings(size)
    
    # Calculate bill
    bill_details = calculate_bill(size, selected_toppings)
    
    # Display receipt
    display_receipt(size, selected_toppings, bill_details)
    
    # Ask if they want to order again
    while True:
        again = input("Would you like to place another order? (Y/N): ").upper().strip()
        if again == "Y":
            print("\n")
            main()
            return
        elif again == "N":
            print("\n👋 Thanks for choosing Python Pizza Deliveries! Have a great day!\n")
            return
        else:
            print("Please enter Y or N.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Order cancelled. Thanks for visiting Python Pizza Deliveries!\n")
        sys.exit(0)
