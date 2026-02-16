import sqlite3
from datetime import datetime

DB_NAME = "expenses.db"

# ---------------- DATABASE SETUP ----------------
def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        amount REAL NOT NULL,
        category TEXT NOT NULL,
        note TEXT
    )
    """)

    conn.commit()
    conn.close()


# ---------------- ADD EXPENSE ----------------
def add_expense():
    try:
        date = input("Enter date (YYYY-MM-DD): ")
        datetime.strptime(date, "%Y-%m-%d")  # validate date

        amount = float(input("Enter amount: "))
        category = input("Enter category (Food, Travel, etc): ")
        note = input("Enter note (optional): ")

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO expenses (date, amount, category, note)
        VALUES (?, ?, ?, ?)
        """, (date, amount, category, note))

        conn.commit()
        conn.close()

        print("Expense added successfully!")

    except ValueError:
        print("Invalid input. Try again.")


# ---------------- VIEW ALL ----------------
def view_all_expenses():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses ORDER BY date")
    rows = cursor.fetchall()

    print("\n--- All Expenses ---")
    for row in rows:
        print(row)

    conn.close()


# ---------------- VIEW BY DATE ----------------
def view_by_date():
    date = input("Enter date (YYYY-MM-DD): ")

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses WHERE date = ?", (date,))
    rows = cursor.fetchall()

    print(f"\n--- Expenses on {date} ---")
    for row in rows:
        print(row)

    conn.close()


# ---------------- MENU ----------------
def main():
    create_table()

    while True:
        print("\n==== Expense Manager ====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Expenses By Date")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_all_expenses()
        elif choice == "3":
            view_by_date()
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
