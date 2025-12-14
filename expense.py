import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# ---------- CONFIG ----------
CSV_FILE = "expenses.csv"
MONTHLY_LIMIT = 10000  # You can change your spending limit here

# ---------- DATA HANDLING ----------
def load_data():
    try:
        return pd.read_csv(CSV_FILE)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Date", "Category", "Amount"])
        df.to_csv(CSV_FILE, index=False)
        return df

def save_data(date, category, amount):
    df = load_data()
    new_entry = {"Date": date, "Category": category, "Amount": amount}
    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    df.to_csv(CSV_FILE, index=False)

# ---------- ANALYSIS ----------
def show_summary():
    df = load_data()
    if df.empty:
        messagebox.showinfo("No Data", "No expenses recorded yet.")
        return

    total_spent = df["Amount"].sum()
    highest_category = df.groupby("Category")["Amount"].sum().idxmax()

    summary_text = (
        f"Total Spent: ₹{total_spent:.2f}\n"
        f"Highest Spending Category: {highest_category}\n"
    )

    if total_spent > MONTHLY_LIMIT:
        summary_text += "\n⚠️ You have exceeded your monthly limit!"
    else:
        summary_text += f"\nRemaining Budget: ₹{MONTHLY_LIMIT - total_spent:.2f}"

    messagebox.showinfo("Expense Summary", summary_text)

# ---------- CHARTS ----------
def show_charts():
    df = load_data()
    if df.empty:
        messagebox.showinfo("No Data", "No expenses to visualize yet.")
        return

    category_totals = df.groupby("Category")["Amount"].sum()

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    plt.suptitle("Expense Tracker Analysis", fontsize=14, color="#1f4e79")

    # Pie Chart
    axes[0].pie(category_totals, labels=category_totals.index, autopct='%1.1f%%', startangle=90)
    axes[0].set_title("Spending Distribution by Category")

    # Bar Chart
    axes[1].bar(category_totals.index, category_totals.values, color="#2e86de")
    axes[1].set_title("Spending per Category")
    axes[1].set_ylabel("Amount (₹)")

    plt.tight_layout()
    plt.show()

# ---------- MAIN UI ----------
def add_expense():
    try:
        amount = float(amount_entry.get())
        category = category_combo.get()
        date = date_entry.get()

        if not category or not date:
            messagebox.showerror("Input Error", "Please fill all fields.")
            return

        save_data(date, category, amount)
        messagebox.showinfo("Success", "Expense Added Successfully!")

        # Clear inputs
        amount_entry.delete(0, tk.END)
        category_combo.set("")
        date_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Input Error", "Enter a valid number for amount.")

# ---------- APP WINDOW ----------
app = tk.Tk()
app.title("💼 Expense Tracker")
app.geometry("500x400")
app.configure(bg="#f2f2f2")

title_label = tk.Label(app, text="Expense Tracker", font=("Arial", 18, "bold"), bg="#f2f2f2", fg="#1f4e79")
title_label.pack(pady=10)

frame = tk.Frame(app, bg="#ffffff", bd=2, relief="ridge")
frame.pack(padx=20, pady=10, fill="both", expand=True)

# Date Input
tk.Label(frame, text="Date (YYYY-MM-DD):", font=("Arial", 11), bg="#ffffff").grid(row=0, column=0, pady=8, padx=8, sticky="w")
date_entry = tk.Entry(frame, font=("Arial", 11))
date_entry.grid(row=0, column=1, pady=8)

# Category Dropdown
tk.Label(frame, text="Category:", font=("Arial", 11), bg="#ffffff").grid(row=1, column=0, pady=8, padx=8, sticky="w")
category_combo = ttk.Combobox(frame, values=["Food", "Transport", "Shopping", "Bills", "Entertainment", "Others"], font=("Arial", 11))
category_combo.grid(row=1, column=1, pady=8)

# Amount Input
tk.Label(frame, text="Amount (₹):", font=("Arial", 11), bg="#ffffff").grid(row=2, column=0, pady=8, padx=8, sticky="w")
amount_entry = tk.Entry(frame, font=("Arial", 11))
amount_entry.grid(row=2, column=1, pady=8)

# Buttons
button_frame = tk.Frame(frame, bg="#ffffff")
button_frame.grid(row=3, column=0, columnspan=2, pady=20)

add_btn = tk.Button(button_frame, text="Add Expense", command=add_expense, bg="#2e86de", fg="white", font=("Arial", 11), width=12)
add_btn.grid(row=0, column=0, padx=5)

summary_btn = tk.Button(button_frame, text="Show Summary", command=show_summary, bg="#27ae60", fg="white", font=("Arial", 11), width=12)
summary_btn.grid(row=0, column=1, padx=5)

chart_btn = tk.Button(button_frame, text="Show Charts", command=show_charts, bg="#e67e22", fg="white", font=("Arial", 11), width=12)
chart_btn.grid(row=0, column=2, padx=5)

exit_btn = tk.Button(button_frame, text="Exit", command=app.quit, bg="#c0392b", fg="white", font=("Arial", 11), width=10)
exit_btn.grid(row=0, column=3, padx=5)

app.mainloop()
