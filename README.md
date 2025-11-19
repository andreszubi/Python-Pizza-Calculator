# Python Pizza Calculator

A simple command-line pizza ordering calculator that helps you calculate the total cost of your pizza order based on size and toppings.

## Overview

This Python program simulates a pizza ordering system where users can select:
- Pizza size (Small, Medium, or Large)
- Pepperoni topping (optional)
- Extra cheese (optional)

The program then calculates and displays the final bill based on the selected options.

## Pricing Structure

### Base Prices
- **Small (S)**: $15
- **Medium (M)**: $20
- **Large (L)**: $25

### Additional Toppings
- **Pepperoni**: 
  - Small pizza: +$2
  - Medium/Large pizza: +$3
- **Extra Cheese**: +$1 (applies to all sizes)

## How to Use

1. Run the program:
   ```bash
   python Pizza-Calculator.py
   ```

2. Follow the prompts:
   - Enter pizza size: `S`, `M`, or `L` (case-insensitive)
   - Enter `Y` or `N` for pepperoni (case-insensitive)
   - Enter `Y` or `N` for extra cheese (case-insensitive)

3. The program will display your final bill.

## Example Usage

```
Welcome to Python Pizza Deliveries!
What size pizza do you want? S, M or L: M
Do you want pepperoni on your pizza? Y or N: Y
Do you want extra cheese? Y or N: Y
Your final bill is: $24.
```

## Requirements

- Python 3.x (no external dependencies required)

## Features

- Interactive command-line interface
- Case-insensitive input handling
- Clear pricing breakdown
- Input validation for pizza size

## Project Structure

```
Python-Pizza-Calculator/
├── Pizza-Calculator.py    # Main program file
└── README.md              # Project documentation
```

