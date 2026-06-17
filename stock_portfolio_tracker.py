# ============================================================
#  TASK 2 — Stock Portfolio Tracker
#  CodeAlpha Python Programming Internship
#  Author : Saurabh Singh Tanwar
#  Date   : June 2025
# ============================================================

# datetime module — used to get current date and time
from datetime import datetime

# ============================================================
#  HARDCODED STOCK PRICES (Dictionary)
#  Key   = Stock Symbol (e.g. "TCS")
#  Value = Price per share in Rupees (₹)
# ============================================================
STOCK_PRICES = {
    # --- Indian Stocks ---
    "RELIANCE" : 2950.00,
    "TCS"      : 3800.00,
    "INFOSYS"  : 1500.00,
    "HDFC"     : 1600.00,
    "WIPRO"    :  480.00,
    "TATASTEEL":  165.00,
    "ONGC"     :  270.00,
    "SBIN"     :  820.00,
    "BAJAJ"    : 7200.00,
    "AIRTEL"   : 1750.00,

    # --- US Stocks ---
    "AAPL"  : 18500.00,   # Apple Inc.
    "TSLA"  : 20800.00,   # Tesla Inc.
    "GOOGLE": 14200.00,   # Alphabet Inc.
    "AMAZON": 16500.00,   # Amazon.com Inc.
    "META"  : 50000.00,   # Meta Platforms Inc.
}

# Portfolio list — stores all stocks the user has purchased
# Each entry is a dictionary with: symbol, quantity, buy_price, total
portfolio = []


# ============================================================
# FUNCTION 1 — Display all available stocks
# ============================================================
def show_available_stocks():
    """Display all available stocks with their current prices."""

    print("\n" + "=" * 55)
    print("   📈  AVAILABLE STOCKS")
    print("=" * 55)
    print(f"   {'SYMBOL':<12} {'TYPE':<20} {'PRICE (INR)':>10}")
    print("-" * 55)

    # Loop through every key-value pair in the dictionary
    for symbol, price in STOCK_PRICES.items():

        # Determine if stock is Indian or US based on symbol
        stock_type = "US Stock" if symbol in ["AAPL", "TSLA", "GOOGLE", "AMAZON", "META"] else "Indian Stock"

        print(f"   {symbol:<12} {stock_type:<20} {price:>10,.2f}")

    print("=" * 55)


# ============================================================
# FUNCTION 2 — Buy a stock and add it to the portfolio
# ============================================================
def buy_stock():
    """Allow the user to purchase a stock by entering symbol and quantity."""

    print("\n📊 BUY STOCK")
    print("-" * 40)

    # Get stock symbol from user — convert to uppercase for consistency
    # .upper() ensures "tcs" and "TCS" are treated the same
    symbol = input("   Enter stock symbol (e.g. TCS, AAPL): ").strip().upper()

    # Check if the entered symbol exists in our stock dictionary
    # 'in' operator checks if a key exists in a dictionary
    if symbol not in STOCK_PRICES:
        print(f"\n   ❌ Stock '{symbol}' not found!")
        print("   💡 Please refer to the available stocks list.")
        return

    # Get the number of shares to purchase
    try:
        quantity = int(input(f"   Enter number of shares to buy: "))

        # Validate that quantity is a positive number
        if quantity <= 0:
            print("   ❌ Quantity must be 1 or more!")
            return

    except ValueError:
        # Handles the case where user enters letters instead of a number
        print("   ❌ Please enter a valid number!")
        return

    # Fetch the current price of the selected stock from the dictionary
    buy_price = STOCK_PRICES[symbol]

    # Calculate total investment for this purchase
    # Formula: Total = Quantity × Price per share
    total_cost = quantity * buy_price

    # Add this stock entry to the portfolio list
    # Each stock is stored as a dictionary (key-value pairs)
    portfolio.append({
        "symbol"   : symbol,
        "quantity" : quantity,
        "buy_price": buy_price,
        "total"    : total_cost
    })

    print(f"\n   ✅ Successfully purchased {quantity} share(s) of {symbol}!")
    print(f"   💰 Price per share : ₹{buy_price:,.2f}")
    print(f"   💸 Total cost      : ₹{total_cost:,.2f}")


# ============================================================
# FUNCTION 3 — Display the user's full portfolio
# ============================================================
def show_portfolio():
    """Display all stocks in the portfolio in a formatted table."""

    # Check if the portfolio has any entries
    if len(portfolio) == 0:
        print("\n   ❌ Your portfolio is empty! Please purchase some stocks first.")
        return

    print("\n" + "=" * 65)
    print("   💼  MY PORTFOLIO")
    print("=" * 65)
    print(f"   {'#':<4} {'SYMBOL':<12} {'QTY':>6} {'PRICE (₹)':>12} {'TOTAL (₹)':>14}")
    print("-" * 65)

    # Variable to accumulate the total investment value
    grand_total = 0

    # enumerate() gives both the index number and the item
    # start=1 means numbering begins from 1 (not 0)
    for i, stock in enumerate(portfolio, start=1):
        print(
            f"   {i:<4}"
            f" {stock['symbol']:<12}"
            f" {stock['quantity']:>6}"
            f" {stock['buy_price']:>12,.2f}"
            f" {stock['total']:>14,.2f}"
        )
        # Add each stock's total to the grand total
        grand_total += stock["total"]

    print("=" * 65)
    print(f"   {'TOTAL INVESTMENT':>44} ₹{grand_total:>12,.2f}")
    print("=" * 65)

    return grand_total


# ============================================================
# FUNCTION 4 — Calculate and display profit/loss
# ============================================================
def show_profit_loss():
    """Calculate and display profit or loss for each stock and overall."""

    if len(portfolio) == 0:
        print("\n   ❌ Your portfolio is empty!")
        return

    print("\n" + "=" * 70)
    print("   📊  PROFIT / LOSS REPORT")
    print("=" * 70)
    print(
        f"   {'SYMBOL':<12}"
        f"{'QTY':>6}"
        f"{'BUY PRICE':>12}"
        f"{'CURR PRICE':>12}"
        f"{'P/L (₹)':>14}"
    )
    print("-" * 70)

    # Variables to track overall investment and current value
    total_invested    = 0
    total_current_val = 0

    for stock in portfolio:
        symbol    = stock["symbol"]
        qty       = stock["quantity"]
        buy_price = stock["buy_price"]

        # Get the current price of the stock from the dictionary
        curr_price = STOCK_PRICES[symbol]

        # Profit/Loss formula:
        # P/L = (Current Price - Buy Price) × Quantity
        pnl = (curr_price - buy_price) * qty

        # Update totals
        total_invested    += buy_price * qty
        total_current_val += curr_price * qty

        # Format P/L with + or - sign for clarity
        pnl_display = f"+₹{pnl:,.2f}" if pnl >= 0 else f"-₹{abs(pnl):,.2f}"

        print(
            f"   {symbol:<12}"
            f"{qty:>6}"
            f"{buy_price:>12,.2f}"
            f"{curr_price:>12,.2f}"
            f"{pnl_display:>14}"
        )

    # Calculate overall profit/loss
    overall_pnl = total_current_val - total_invested

    # Percentage gain/loss formula:
    # % = (Overall P/L / Total Invested) × 100
    overall_pct = (overall_pnl / total_invested) * 100 if total_invested > 0 else 0

    print("=" * 70)
    print(f"   Total Invested     : ₹{total_invested:,.2f}")
    print(f"   Current Value      : ₹{total_current_val:,.2f}")

    if overall_pnl >= 0:
        print(f"   Overall P/L        : +₹{overall_pnl:,.2f} (+{overall_pct:.2f}%) 📈 PROFIT")
    else:
        print(f"   Overall P/L        : -₹{abs(overall_pnl):,.2f} ({overall_pct:.2f}%) 📉 LOSS")

    print("=" * 70)


# ============================================================
# FUNCTION 5 — Save portfolio report to a .txt file
# ============================================================
def save_portfolio():
    """Save the current portfolio details to a .txt file."""

    if len(portfolio) == 0:
        print("\n   ❌ Portfolio is empty — nothing to save!")
        return

    # Create a unique filename using current timestamp
    # strftime() formats date and time as a string
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename  = f"portfolio_{timestamp}.txt"

    # Calculate grand total using sum() with a generator expression
    grand_total = sum(stock["total"] for stock in portfolio)

    # Open file in write mode ("w")
    # "w" creates a new file, or overwrites if it already exists
    with open(filename, "w") as file:

        file.write("=" * 55 + "\n")
        file.write("   STOCK PORTFOLIO REPORT\n")
        file.write("   CodeAlpha Python Internship — Task 2\n")
        file.write(f"   Generated on: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
        file.write("=" * 55 + "\n\n")

        file.write(f"{'#':<4} {'SYMBOL':<12} {'QTY':>6} {'PRICE (INR)':>14} {'TOTAL (INR)':>14}\n")
        file.write("-" * 55 + "\n")

        # Write each stock entry to the file
        for i, stock in enumerate(portfolio, start=1):
            file.write(
                f"{i:<4}"
                f"{stock['symbol']:<12}"
                f"{stock['quantity']:>6}"
                f"{stock['buy_price']:>14,.2f}"
                f"{stock['total']:>14,.2f}\n"
            )

        file.write("=" * 55 + "\n")
        file.write(f"{'TOTAL INVESTMENT':>38} ₹{grand_total:>12,.2f}\n")
        file.write("=" * 55 + "\n")

    print(f"\n   ✅ Portfolio saved successfully: '{filename}'")


# ============================================================
# FUNCTION 6 — Remove a stock from the portfolio
# ============================================================
def remove_stock():
    """Remove a selected stock entry from the portfolio."""

    if len(portfolio) == 0:
        print("\n   ❌ Portfolio is already empty!")
        return

    # Display current portfolio so user can choose which to remove
    show_portfolio()

    try:
        choice = int(input("\n   Enter the number of the stock to remove: "))

        # Validate the choice is within the valid range
        if choice < 1 or choice > len(portfolio):
            print("   ❌ Invalid choice! Please enter a valid number.")
            return

        # Remove the selected entry from the list
        # choice - 1 because list index starts from 0, but we displayed from 1
        removed = portfolio.pop(choice - 1)
        print(f"\n   ✅ {removed['symbol']} has been removed from your portfolio!")

    except ValueError:
        print("   ❌ Please enter a valid number!")


# ============================================================
# MAIN FUNCTION — Menu-driven interface
# ============================================================
def main():
    """Main function — displays menu and handles user choices."""

    print("\n" + "=" * 55)
    print("   📈  STOCK PORTFOLIO TRACKER")
    print("   CodeAlpha Python Internship — Task 2")
    print("   Author: Saurabh Singh Tanwar")
    print("=" * 55)

    # Infinite loop — keeps the menu running until user exits
    while True:

        print("\n   ┌─────────────────────────────────┐")
        print("   │           MAIN MENU             │")
        print("   ├─────────────────────────────────┤")
        print("   │  1 → View Available Stocks      │")
        print("   │  2 → Buy a Stock                │")
        print("   │  3 → View My Portfolio          │")
        print("   │  4 → View Profit / Loss         │")
        print("   │  5 → Remove a Stock             │")
        print("   │  6 → Save Portfolio to File     │")
        print("   │  7 → Exit                       │")
        print("   └─────────────────────────────────┘")

        choice = input("\n   Enter your choice (1-7): ").strip()

        if choice == "1":
            show_available_stocks()

        elif choice == "2":
            buy_stock()

        elif choice == "3":
            show_portfolio()

        elif choice == "4":
            show_profit_loss()

        elif choice == "5":
            remove_stock()

        elif choice == "6":
            save_portfolio()

        elif choice == "7":
            print("\n   👋 Thank you for using Stock Portfolio Tracker. Goodbye!\n")
            break

        else:
            print("\n   ⚠️  Invalid choice! Please enter a number between 1 and 7.")


# Entry Point
# This block runs only when the file is executed directly
# (not when imported as a module)
if __name__ == "__main__":
    main()
