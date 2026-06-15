# ============================================================
#  TASK 2 — Stock Portfolio Tracker
#  CodeAlpha Python Programming Internship
# ============================================================

# --- datetime = date aur time ke liye ---
from datetime import datetime

# ============================================================
#  HARDCODED STOCK PRICES (Dictionary)
#  Key   = Stock Symbol
#  Value = Price in Rupees (₹)
# ============================================================
STOCK_PRICES = {
    # 🇮🇳 Indian Stocks
    "RELIANCE" : 2950.00,
    "TCS"      : 3800.00,
    "INFOSYS"  : 1500.00,
    "HDFC"     : 1600.00,
    "WIPRO"    : 480.00,
    "TATASTEEL": 165.00,
    "ONGC"     : 270.00,
    "SBIN"     : 820.00,
    "BAJAJ"    : 7200.00,
    "AIRTEL"   : 1750.00,

    # 🇺🇸 US Stocks
    "AAPL"  : 18500.00,   # Apple
    "TSLA"  : 20800.00,   # Tesla
    "GOOGLE": 14200.00,   # Google
    "AMAZON": 16500.00,   # Amazon
    "META"  : 50000.00,   # Meta (Facebook)
}

# Portfolio = User ne jo stocks kharide hain unki list
# Yeh ek list of dictionaries hai
# Har item mein: stock naam, quantity, buy price
portfolio = []


# ============================================================
# FUNCTION 1 — Available stocks dikhao
# ============================================================
def show_available_stocks():
    """Sabhi available stocks aur unki prices dikhao."""

    print("\n" + "=" * 55)
    print("   📈  AVAILABLE STOCKS")
    print("=" * 55)
    print(f"   {'SYMBOL':<12} {'COMPANY / STOCK':<20} {'PRICE (₹)':>10}")
    print("-" * 55)

    # Dictionary ke har item ko ek ek karke print karo
    # .items() = key aur value dono ek saath do
    for symbol, price in STOCK_PRICES.items():
        print(f"   {symbol:<12} {'':20} {price:>10,.2f}")

    print("=" * 55)


# ============================================================
# FUNCTION 2 — Stock kharido (portfolio mein add karo)
# ============================================================
def buy_stock():
    """User se stock symbol aur quantity lo — portfolio mein add karo."""

    print("\n📊 STOCK KHARIDO")
    print("-" * 40)

    # Stock symbol lo — uppercase mein convert karo
    # .upper() = "tcs" → "TCS"
    symbol = input("   Stock symbol daalo (e.g. TCS, AAPL): ").strip().upper()

    # Check karo yeh stock available hai ya nahi
    # 'in' operator = dictionary mein key exist karti hai?
    if symbol not in STOCK_PRICES:
        print(f"\n   ❌ '{symbol}' stock nahi mila!")
        print("   💡 Upar available stocks ki list dekho.")
        return

    # Quantity lo
    try:
        # int() = string ko number mein convert karo
        quantity = int(input(f"   Kitne shares khareedne hain: "))

        if quantity <= 0:
            print("   ❌ Quantity 1 ya usse zyada honi chahiye!")
            return

    except ValueError:
        # Agar user ne number ke bajaye kuch aur daala
        print("   ❌ Sirf number daalo!")
        return

    # Stock ka current price nikalo dictionary se
    buy_price = STOCK_PRICES[symbol]

    # Total cost calculate karo
    # Simple arithmetic: quantity × price = total
    total_cost = quantity * buy_price

    # Portfolio mein add karo
    # Ek dictionary banao is stock ke liye aur list mein append karo
    portfolio.append({
        "symbol"   : symbol,
        "quantity" : quantity,
        "buy_price": buy_price,
        "total"    : total_cost
    })

    print(f"\n   ✅ {quantity} shares of {symbol} khareed liye!")
    print(f"   💰 Price per share : ₹{buy_price:,.2f}")
    print(f"   💸 Total cost      : ₹{total_cost:,.2f}")


# ============================================================
# FUNCTION 3 — Portfolio dikhao
# ============================================================
def show_portfolio():
    """User ka poora portfolio sundar format mein dikhao."""

    # Agar portfolio khali hai
    if len(portfolio) == 0:
        print("\n   ❌ Portfolio khali hai! Pehle kuch stocks kharido.")
        return

    print("\n" + "=" * 65)
    print("   💼  MERA PORTFOLIO")
    print("=" * 65)
    print(f"   {'#':<4} {'SYMBOL':<12} {'QTY':>6} {'PRICE (₹)':>12} {'TOTAL (₹)':>14}")
    print("-" * 65)

    # Grand total calculate karne ke liye
    grand_total = 0

    # enumerate() = number ke saath list ke items do
    for i, stock in enumerate(portfolio, start=1):
        print(
            f"   {i:<4}"
            f" {stock['symbol']:<12}"
            f" {stock['quantity']:>6}"
            f" {stock['buy_price']:>12,.2f}"
            f" {stock['total']:>14,.2f}"
        )
        # Har stock ka total grand total mein jodhte jao
        grand_total += stock["total"]

    print("=" * 65)
    print(f"   {'TOTAL INVESTMENT':>44} ₹{grand_total:>12,.2f}")
    print("=" * 65)

    return grand_total


# ============================================================
# FUNCTION 4 — Current value aur profit/loss dikhao
# ============================================================
def show_profit_loss():
    """Portfolio ki current value aur profit/loss calculate karo."""

    if len(portfolio) == 0:
        print("\n   ❌ Portfolio khali hai!")
        return

    print("\n" + "=" * 70)
    print("   📊  PROFIT / LOSS REPORT")
    print("=" * 70)
    print(
        f"   {'SYMBOL':<12}"
        f"{'QTY':>6}"
        f"{'BUY PRICE':>12}"
        f"{'CURR PRICE':>12}"
        f"{'P/L (₹)':>12}"
    )
    print("-" * 70)

    total_invested    = 0
    total_current_val = 0

    for stock in portfolio:
        symbol    = stock["symbol"]
        qty       = stock["quantity"]
        buy_price = stock["buy_price"]

        # Current price dictionary se lo
        curr_price = STOCK_PRICES[symbol]

        # Profit/Loss = (current price - buy price) × quantity
        pnl = (curr_price - buy_price) * qty

        # Totals update karo
        total_invested    += buy_price * qty
        total_current_val += curr_price * qty

        # + ya - sign ke saath dikhao
        pnl_str = f"+₹{pnl:,.2f}" if pnl >= 0 else f"-₹{abs(pnl):,.2f}"

        print(
            f"   {symbol:<12}"
            f"{qty:>6}"
            f"{buy_price:>12,.2f}"
            f"{curr_price:>12,.2f}"
            f"{pnl_str:>12}"
        )

    # Overall P/L
    overall_pnl = total_current_val - total_invested
    overall_pct = (overall_pnl / total_invested) * 100 if total_invested > 0 else 0

    print("=" * 70)
    print(f"   Total Invested     : ₹{total_invested:,.2f}")
    print(f"   Current Value      : ₹{total_current_val:,.2f}")

    # Agar profit hua
    if overall_pnl >= 0:
        print(f"   Overall P/L        : +₹{overall_pnl:,.2f} (+{overall_pct:.2f}%) 📈")
    else:
        print(f"   Overall P/L        : -₹{abs(overall_pnl):,.2f} ({overall_pct:.2f}%) 📉")

    print("=" * 70)


# ============================================================
# FUNCTION 5 — Portfolio file mein save karo
# ============================================================
def save_portfolio():
    """Portfolio ko .txt file mein save karo."""

    if len(portfolio) == 0:
        print("\n   ❌ Portfolio khali hai — save karne ke liye kuch nahi!")
        return

    # File ka naam — current date aur time ke saath
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename  = f"portfolio_{timestamp}.txt"

    # Grand total calculate karo
    grand_total = sum(stock["total"] for stock in portfolio)

    # "w" mode = write — naya file banao
    with open(filename, "w") as file:

        file.write("=" * 55 + "\n")
        file.write("   STOCK PORTFOLIO REPORT\n")
        file.write("   CodeAlpha Python Internship — Task 2\n")
        file.write(f"   Generated: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
        file.write("=" * 55 + "\n\n")

        file.write(f"{'#':<4} {'SYMBOL':<12} {'QTY':>6} {'PRICE':>12} {'TOTAL':>14}\n")
        file.write("-" * 55 + "\n")

        for i, stock in enumerate(portfolio, start=1):
            file.write(
                f"{i:<4}"
                f"{stock['symbol']:<12}"
                f"{stock['quantity']:>6}"
                f"{stock['buy_price']:>12,.2f}"
                f"{stock['total']:>14,.2f}\n"
            )

        file.write("=" * 55 + "\n")
        file.write(f"{'TOTAL INVESTMENT':>36} ₹{grand_total:>12,.2f}\n")
        file.write("=" * 55 + "\n")

    print(f"\n   ✅ Portfolio saved ho gaya: '{filename}'")


# ============================================================
# FUNCTION 6 — Stock hataao portfolio se
# ============================================================
def remove_stock():
    """Portfolio se koi stock hatao."""

    if len(portfolio) == 0:
        print("\n   ❌ Portfolio pehle se khali hai!")
        return

    show_portfolio()

    try:
        choice = int(input("\n   Kaun sa stock hatana hai? (Number daalo): "))

        # Valid number hai?
        if choice < 1 or choice > len(portfolio):
            print("   ❌ Galat number!")
            return

        # List se remove karo
        # choice-1 kyunki list 0 se start hoti hai
        removed = portfolio.pop(choice - 1)
        print(f"\n   ✅ {removed['symbol']} portfolio se hata diya!")

    except ValueError:
        print("   ❌ Sirf number daalo!")


# ============================================================
# MAIN FUNCTION — Menu System
# ============================================================
def main():

    print("\n" + "=" * 55)
    print("   📈  STOCK PORTFOLIO TRACKER")
    print("   CodeAlpha Python Internship — Task 2")
    print("=" * 55)

    while True:

        # Menu dikhao
        print("\n   ┌─────────────────────────────────┐")
        print("   │         MAIN MENU               │")
        print("   ├─────────────────────────────────┤")
        print("   │  1 → Available Stocks Dekho     │")
        print("   │  2 → Stock Kharido              │")
        print("   │  3 → Mera Portfolio Dekho       │")
        print("   │  4 → Profit / Loss Dekho        │")
        print("   │  5 → Stock Hatao                │")
        print("   │  6 → Portfolio Save Karo (.txt) │")
        print("   │  7 → Exit                       │")
        print("   └─────────────────────────────────┘")

        choice = input("\n   Apna choice daalo (1-7): ").strip()

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
            print("\n   👋 Portfolio Tracker band ho raha hai. Bye!\n")
            break

        else:
            print("\n   ⚠️  Galat choice! 1 se 7 ke beech daalo.")


# Entry Point
if __name__ == "__main__":
    main()
