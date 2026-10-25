
import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_FILE = os.path.join(BASE_DIR, "constituents.csv")
OUTPUT_FILE = os.path.join(BASE_DIR, "portfolio_summary.csv")


def load_tickers():
    """Load valid S&P 500 ticker symbols from the dataset."""
    try:
        with open(DATASET_FILE, "r", newline="", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)

            if not reader.fieldnames or "Symbol" not in reader.fieldnames:
                print("Error: The dataset must contain a 'Symbol' column.")
                return set()

            return {
                row["Symbol"].strip().upper()
                for row in reader
                if row.get("Symbol", "").strip()
            }

    except FileNotFoundError:
        print("Error: constituents.csv was not found.")
        print("Place it in the same folder as portfolio.py.")
        return set()

    except OSError as error:
        print(f"Could not read the dataset: {error}")
        return set()


def get_positive_number(prompt):
    """Ask for a number greater than zero."""
    while True:
        try:
            value = float(input(prompt))

            if value <= 0:
                print("Please enter a number greater than zero.")
            else:
                return value

        except ValueError:
            print("Invalid input. Please enter a number.")


def get_current_price(ticker):
    """Fetch a price using Yahoo Finance, or ask the user."""
    try:
        import yfinance as yf

        stock = yf.Ticker(ticker)
        price = stock.fast_info["last_price"]

        if price is not None and float(price) > 0:
            return float(price)

    except Exception:
        pass

    print(f"Could not fetch a current price for {ticker}.")
    return get_positive_number(
        f"Enter the current price for {ticker} manually ($): "
    )


def save_summary(results):
    """Write portfolio results to a CSV file."""
    columns = [
        "Ticker",
        "Company",
        "Buy Price",
        "Shares",
        "Current Price",
        "Total Invested",
        "Current Value",
        "Profit/Loss",
        "Gain/Loss (%)",
    ]

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(results)

    print(f"\nResults saved to: {OUTPUT_FILE}")


def main():
    valid_tickers = load_tickers()

    if not valid_tickers:
        print("No ticker symbols loaded. Check constituents.csv.")
        return

    # Load company names as well as ticker symbols.
    companies = {}

    with open(DATASET_FILE, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        for row in reader:
            symbol = row.get("Symbol", "").strip().upper()
            name = row.get("Name", "").strip()
            if symbol:
                companies[symbol] = name

    portfolio = {}

    print("=" * 60)
    print("       STOCK PORTFOLIO PERFORMANCE TRACKER")
    print("=" * 60)
    print(f"Loaded {len(valid_tickers)} S&P 500 ticker symbols.")

    while True:
        ticker = input(
            "\nEnter a ticker (e.g., AAPL), or type DONE to finish: "
        ).strip().upper()

        if ticker == "DONE":
            break

        if ticker not in valid_tickers:
            print("Ticker not found in the S&P 500 dataset.")
            print("Please enter a valid symbol from the dataset.")
            continue

        if ticker in portfolio:
            print("This stock has already been added.")
            continue

        print(f"Selected: {companies.get(ticker, ticker)}")

        buy_price = get_positive_number(
            "Enter your purchase price per share ($): "
        )
        shares = get_positive_number("Enter the number of shares: ")

        portfolio[ticker] = {
            "buy_price": buy_price,
            "shares": shares,
        }

    if not portfolio:
        print("\nNo stocks were added. Goodbye!")
        return

    results = []
    total_invested = 0.0
    total_value = 0.0

    for ticker, details in portfolio.items():
        buy_price = details["buy_price"]
        shares = details["shares"]
        current_price = get_current_price(ticker)

        invested = buy_price * shares
        market_value = current_price * shares
        profit_loss = market_value - invested
        gain_loss_percent = (profit_loss / invested) * 100

        total_invested += invested
        total_value += market_value

        results.append({
            "Ticker": ticker,
            "Company": companies.get(ticker, ticker),
            "Buy Price": round(buy_price, 2),
            "Shares": shares,
            "Current Price": round(current_price, 2),
            "Total Invested": round(invested, 2),
            "Current Value": round(market_value, 2),
            "Profit/Loss": round(profit_loss, 2),
            "Gain/Loss (%)": round(gain_loss_percent, 2),
        })

    print("\n" + "=" * 90)
    print("PORTFOLIO SUMMARY")
    print("=" * 90)
    print(
        f"{'Ticker':<9}{'Buy Price':>12}{'Shares':>10}"
        f"{'Current':>12}{'Invested':>14}{'Value':>14}"
        f"{'P/L':>12}{'P/L %':>9}"
    )
    print("-" * 90)

    for item in results:
        print(
            f"{item['Ticker']:<9}"
            f"{item['Buy Price']:>12.2f}"
            f"{item['Shares']:>10.2f}"
            f"{item['Current Price']:>12.2f}"
            f"{item['Total Invested']:>14.2f}"
            f"{item['Current Value']:>14.2f}"
            f"{item['Profit/Loss']:>12.2f}"
            f"{item['Gain/Loss (%)']:>8.2f}%"
        )

    total_profit_loss = total_value - total_invested
    overall_percent = (total_profit_loss / total_invested) * 100

    print("-" * 90)
    print(f"Total invested:       ${total_invested:,.2f}")
    print(f"Current market value: ${total_value:,.2f}")
    print(f"Total profit/loss:    ${total_profit_loss:,.2f}")
    print(f"Overall gain/loss:     {overall_percent:.2f}%")

    save_summary(results)


if __name__ == "__main__":
    main()
