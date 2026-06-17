# 📈 Stock Portfolio Tracker | CodeAlpha Internship Task 2

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Internship-CodeAlpha-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Task-2%20of%204-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Type-Finance%20Tracker-red?style=for-the-badge" />
</p>

---

## 📌 About the Project

A **console-based Stock Portfolio Tracker** built in Python as part of the **CodeAlpha Python Programming Internship**.

Users can buy stocks, view their full portfolio, check real-time profit/loss, remove stocks, and save detailed reports to a `.txt` file — all through a clean menu-driven interface!

---

## 🕹️ How It Works

```
1. Run the script
2. Choose an option from the Main Menu
3. View available stocks (15 stocks — Indian + US)
4. Buy stocks by entering symbol and quantity
5. View your portfolio in a formatted table
6. Check profit / loss for each stock
7. Save your portfolio report to a .txt file
8. Exit anytime
```

---

## 🖥️ Demo Preview

```
=======================================================
   📈  STOCK PORTFOLIO TRACKER
   CodeAlpha Python Internship — Task 2
   Author: Saurabh Singh Tanwar
=======================================================

   ┌─────────────────────────────────┐
   │           MAIN MENU             │
   ├─────────────────────────────────┤
   │  1 → View Available Stocks      │
   │  2 → Buy a Stock                │
   │  3 → View My Portfolio          │
   │  4 → View Profit / Loss         │
   │  5 → Remove a Stock             │
   │  6 → Save Portfolio to File     │
   │  7 → Exit                       │
   └─────────────────────────────────┘

=================================================================
   💼  MY PORTFOLIO
=================================================================
   #    SYMBOL          QTY    PRICE (₹)        TOTAL (₹)
-----------------------------------------------------------------
   1    TCS              10     3,800.00         38,000.00
   2    AAPL              5    18,500.00         92,500.00
=================================================================
                               TOTAL INVESTMENT  ₹  1,30,500.00
=================================================================

======================================================================
   📊  PROFIT / LOSS REPORT
======================================================================
   SYMBOL          QTY   BUY PRICE   CURR PRICE        P/L (₹)
----------------------------------------------------------------------
   TCS              10    3,800.00     3,800.00          +₹0.00
   AAPL              5   18,500.00    18,500.00          +₹0.00
======================================================================
   Total Invested     : ₹1,30,500.00
   Current Value      : ₹1,30,500.00
   Overall P/L        : +₹0.00 (+0.00%) 📈 PROFIT
======================================================================
```

---

## ✨ Features

- 📋 **15 Stocks Available** — 10 Indian + 5 US stocks with real-like prices
- 🛒 **Buy Stocks** — Enter symbol and quantity to add to portfolio
- 💼 **Portfolio View** — Clean formatted table with all holdings
- 📊 **Profit / Loss Report** — Real-time P/L calculation per stock and overall
- 🗑️ **Remove Stocks** — Delete any entry from portfolio
- 💾 **Save to File** — Export portfolio as timestamped `.txt` report
- 🛡️ **Error Handling** — Invalid inputs handled gracefully with `try-except`
- 🔁 **Menu Loop** — Keeps running until user chooses to exit

---

## 📂 Project Structure

```
CodeAlpha_StockPortfolioTracker/
│
├── stock_portfolio_tracker.py    ← Main Python script
└── README.md                     ← Project documentation
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed → [Download here](https://python.org)
- No external libraries required — only built-in `datetime` module used!

### Run the Project

```bash
# Clone the repository
git clone https://github.com/saurabhsingh2606/CodeAlpha_StockPortfolioTracker.git

# Navigate into the folder
cd CodeAlpha_StockPortfolioTracker

# Run the tracker
python stock_portfolio_tracker.py
```

---

## 📊 Available Stocks

| Symbol | Company | Price (₹) | Type |
|---|---|---|---|
| RELIANCE | Reliance Industries | 2,950 | 🇮🇳 Indian |
| TCS | Tata Consultancy Services | 3,800 | 🇮🇳 Indian |
| INFOSYS | Infosys Limited | 1,500 | 🇮🇳 Indian |
| HDFC | HDFC Bank | 1,600 | 🇮🇳 Indian |
| WIPRO | Wipro Limited | 480 | 🇮🇳 Indian |
| TATASTEEL | Tata Steel | 165 | 🇮🇳 Indian |
| ONGC | Oil & Natural Gas Corp | 270 | 🇮🇳 Indian |
| SBIN | State Bank of India | 820 | 🇮🇳 Indian |
| BAJAJ | Bajaj Finance | 7,200 | 🇮🇳 Indian |
| AIRTEL | Bharti Airtel | 1,750 | 🇮🇳 Indian |
| AAPL | Apple Inc. | 18,500 | 🇺🇸 US |
| TSLA | Tesla Inc. | 20,800 | 🇺🇸 US |
| GOOGLE | Alphabet Inc. | 14,200 | 🇺🇸 US |
| AMAZON | Amazon.com Inc. | 16,500 | 🇺🇸 US |
| META | Meta Platforms Inc. | 50,000 | 🇺🇸 US |

---

## 🧠 Concepts & Technologies Used

| Concept | Usage in Project |
|---|---|
| `dictionary` | Storing hardcoded stock prices as key-value pairs |
| `list of dicts` | Storing portfolio entries (symbol, qty, price, total) |
| `arithmetic` | Calculating total investment, profit, loss, percentage |
| `while loop` | Keeping menu running until user exits |
| `if-elif-else` | Handling all menu choices and validations |
| `try-except` | Catching invalid user input without crashing |
| `enumerate()` | Adding serial numbers to portfolio display |
| `sum()` | Calculating grand total from portfolio list |
| `file handling` | Saving portfolio report to a `.txt` file |
| `datetime` | Adding timestamp to saved report filename |
| `f-strings` | Clean, formatted console output |
| `:,.2f` | Formatting numbers as currency (₹1,500.00) |

---

## 🔮 Future Improvements

- [ ] Fetch real-time stock prices using an API (e.g. Yahoo Finance)
- [ ] Export portfolio as `.csv` file for Excel compatibility
- [ ] Add graphical charts using `matplotlib`
- [ ] Support for multiple user portfolios
- [ ] Buy and sell history tracking with timestamps

---

## 👨‍💻 Author

**Saurabh Singh Tanwar**
🎓 BSc Computer Science — 5th Semester
🏫 Guru Ghasidas Vishwavidyalaya, Bilaspur, Chhattisgarh
🐙 [GitHub](https://github.com/saurabhsingh2606)

---

## 🏢 Internship

This project was built as **Task 2** of the **Python Programming Internship** at
**[CodeAlpha](https://www.codealpha.tech)** — A leading software development company.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<p align="center">
  Made with ❤️ during CodeAlpha Python Internship
</p>
