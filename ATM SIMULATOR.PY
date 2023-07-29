import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
account_balance = 1000

#function to update balance
def update_balance_label():
    balance_label.config(text=f"Balance: ${account_balance:.2f}", fg="#FFFFFF")
    balance_label.pack(pady=5) 
def check_balance():
    update_balance_label()

# Function for deposit
def deposit_amount():
    global account_balance
    try:
        amount = float(deposit_entry.get())
        if amount <= 0:
            raise ValueError("Invalid amount for deposit.")
        account_balance += amount
        update_balance_label()
        clear_entries()
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Function for withdrawal
def withdraw_amount():
    global account_balance
    try:
        amount = float(withdraw_entry.get())
        if amount <= 0:
            raise ValueError("Invalid amount for withdrawal.")
        if amount > account_balance:
            messagebox.showerror("Error", "Insufficient balance.")
        else:
            account_balance -= amount
            update_balance_label()
            clear_entries()
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Function to clear entry fields
def clear_entries():
    deposit_entry.delete(0, tk.END)
    withdraw_entry.delete(0, tk.END)

# Create the main GUI window
root = tk.Tk()
root.title("ATM Simulator")
root.geometry("400x300")

# Set the background color and gradient
bg_color = "#92C2ED"
bg_image = Image.open("background.jpg") 
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create and layout GUI elements
balance_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg=bg_color)
check_balance_button = tk.Button(root, text="Check Balance", font=("Arial", 12, "bold"), bg="#F1A94E", command=check_balance)
deposit_entry = tk.Entry(root, font=("Arial", 12), bg="#F3D250", width=15)
deposit_button = tk.Button(root, text="Deposit", font=("Arial", 12, "bold"), bg="#8AC926", command=deposit_amount)
withdraw_entry = tk.Entry(root, font=("Arial", 12), bg="#FF595E", width=15)
withdraw_button = tk.Button(root, text="Withdraw", font=("Arial", 12, "bold"), bg="#6A4C93", command=withdraw_amount)
clear_button = tk.Button(root, text="Clear", font=("Arial", 12, "bold"), bg="#B1A296", command=clear_entries)
balance_label.pack(pady=10)
check_balance_button.pack(pady=5)
deposit_entry.pack(pady=5)
deposit_button.pack(pady=5)
withdraw_entry.pack(pady=5)
withdraw_button.pack(pady=5)
clear_button.pack(pady=5)

# Run the main event loop
root.mainloop()
