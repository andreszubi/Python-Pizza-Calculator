# 🍕 Python Pizza Calculator

An interactive and fun command-line pizza ordering calculator built with Python. Calculate your pizza order total with multiple toppings, automatic combo deal detection, and detailed receipts!

## Features

### 🎯 Core Functionality
- **Three Pizza Sizes**: Small ($15), Medium ($20), Large ($25)
- **12 Topping Options**: Choose from a variety of delicious toppings
- **Multiple Topping Selection**: Add as many toppings as you want
- **Automatic Combo Deals**: Get discounts when you order qualifying combinations
- **Detailed Receipts**: See a complete breakdown of your order
- **Interactive Experience**: User-friendly interface with helpful tips and validation

### 🎁 Special Combo Deals

The calculator automatically detects and applies discounts when you order these combinations:

1. **Meat Lovers Combo** (15% off)
   - Pepperoni, Sausage, Bacon, Chicken

2. **Veggie Delight Combo** (12% off)
   - Mushrooms, Olives, Green Peppers, Onions

3. **Supreme Combo** (20% off)
   - Pepperoni, Mushrooms, Olives, Green Peppers, Onions, Sausage

4. **Hawaiian Combo** (10% off)
   - Pineapple, Chicken

## 📋 Available Toppings

| # | Topping | Small | Medium | Large |
|---|---------|-------|--------|-------|
| 1 | Pepperoni | $2.00 | $3.00 | $3.00 |
| 2 | Mushrooms | $1.50 | $2.00 | $2.50 |
| 3 | Olives | $1.50 | $2.00 | $2.50 |
| 4 | Green Peppers | $1.00 | $1.50 | $2.00 |
| 5 | Onions | $1.00 | $1.50 | $2.00 |
| 6 | Sausage | $2.50 | $3.00 | $3.50 |
| 7 | Bacon | $2.50 | $3.00 | $3.50 |
| 8 | Pineapple | $1.50 | $2.00 | $2.50 |
| 9 | Jalapeños | $1.50 | $2.00 | $2.50 |
| 10 | Extra Cheese | $1.00 | $1.00 | $1.00 |
| 11 | Chicken | $2.50 | $3.00 | $3.50 |
| 12 | Anchovies | $2.00 | $2.50 | $3.00 |

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your system

### Installation
1. Clone or download this repository
2. Navigate to the project directory:
   ```bash
   cd Python-Pizza-Calculator
   ```

### Running the Program
Simply run the Python script:
```bash
python3 Pizza-Calculator.py
```

Or on Windows:
```bash
python Pizza-Calculator.py
```

## 📖 How to Use

1. **Select Pizza Size**: Choose from Small (S), Medium (M), or Large (L)
   - The prompt shows prices for each size

2. **Choose Toppings**: 
   - A menu of available toppings will be displayed
   - Enter the number(s) of your desired toppings
   - You can select multiple toppings at once by separating numbers with commas (e.g., `1,2,3`)
   - Type `DONE` when you're finished selecting toppings

3. **View Receipt**: 
   - Your order summary will be displayed with:
     - Pizza size and base price
     - All selected toppings with individual prices
     - Any applicable combo deal discounts
     - Final total

4. **Place Another Order**: 
   - After viewing your receipt, you can choose to place another order or exit

## 💡 Example Usage

```
What size pizza do you want? (S:$15/M:$20/L:$25):
M

Select topping(s) by number (or 'DONE' to finish):
1,6,7,11

Select topping(s) by number (or 'DONE' to finish):
DONE

🧾 YOUR PIZZA ORDER RECEIPT
==================================================
🍕 Medium Pizza: $20.00

📌 Toppings:
   • Pepperoni            $3.00
   • Sausage              $3.00
   • Bacon                $3.00
   • Chicken              $3.00

🎉 SPECIAL DEAL: Meat Lovers Combo!
   Discount (15% off): -$4.80

--------------------------------------------------
💰 TOTAL: $27.20
==================================================

🎊 Congratulations! You saved $4.80 with the Meat Lovers Combo!
```

## 🎨 Features in Detail

### Input Validation
- Size validation ensures only valid sizes (S, M, L) are accepted
- Topping validation prevents invalid selections
- Prevents duplicate toppings from being added

### User Experience
- Clear, formatted output with emojis for visual appeal
- Helpful tips and instructions throughout
- Real-time feedback when adding toppings
- Detailed receipt with itemized breakdown
- Graceful error handling

### Combo Deal Logic
- Automatically detects when your order qualifies for combo deals
- Applies the best available discount if multiple combos qualify
- Clearly displays savings on the receipt

## 🛠️ Technical Details

### Project Structure
```
Python-Pizza-Calculator/
├── Pizza-Calculator.py    # Main application file
└── README.md              # This file
```

### Key Functions
- `get_pizza_size()`: Validates and retrieves pizza size selection
- `display_toppings_menu()`: Shows available toppings with prices
- `get_toppings()`: Handles multiple topping selection
- `calculate_combo_discount()`: Detects applicable combo deals
- `calculate_bill()`: Computes total with base price, toppings, and discounts
- `display_receipt()`: Formats and displays order summary

## 🤝 Contributing

Feel free to fork this project and add your own features! Some ideas:
- Additional toppings
- More combo deals
- Delivery fee calculation
- Multiple pizza orders
- Save order history

## 📝 License

This project is open source and available for educational purposes.

## 🎉 Enjoy Your Pizza!

Happy coding and enjoy your virtual pizza! 🍕

