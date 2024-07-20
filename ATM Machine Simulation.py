import tkinter as tk
from tkinter import messagebox, simpledialog

# ATM Application Code
class ATMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM System")
        self.root.configure(background='orange')  # Set background color to orange
        self.root.attributes('-fullscreen', True)  # Open in full screen
        self.balance = 5000
        self.password = 1234

        # Create GUI Components
        self.create_widgets()

    def create_widgets(self):
        # Card Insertion
        self.label = tk.Label(self.root, text="Please insert Your CARD", font=("Helvetica", 16), bg='orange')
        self.label.pack(pady=20)

        # PIN Input
        self.pin_label = tk.Label(self.root, text="Enter your ATM pin:", font=("Helvetica", 12), bg='orange')
        self.pin_label.pack(pady=10)

        self.pin_entry = tk.Entry(self.root, show="*", font=("Helvetica", 12))
        self.pin_entry.pack(pady=10)

        self.login_button = tk.Button(self.root, text="Login", command=self.check_pin, font=("Helvetica", 12), bg='orange')
        self.login_button.pack(pady=10)

        self.exit_button = tk.Button(self.root, text="Exit", command=self.confirm_exit, font=("Helvetica", 12), bg='orange')
        self.exit_button.pack(pady=20)

    def check_pin(self):
        try:
            pin = int(self.pin_entry.get())
            if pin == self.password:
                self.label.pack_forget()
                self.pin_label.pack_forget()
                self.pin_entry.pack_forget()
                self.login_button.pack_forget()
                self.exit_button.pack_forget()
                self.show_menu()
            else:
                messagebox.showerror("Error", "Wrong PIN. Please try again.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a number.")

    def show_menu(self):
        # Main Menu
        self.menu_label = tk.Label(self.root, text="ATM Menu", font=("Helvetica", 16), bg='orange')
        self.menu_label.pack(pady=20)

        self.balance_button = tk.Button(self.root, text="Check Balance", command=self.check_balance, font=("Helvetica", 12), bg='orange')
        self.balance_button.pack(pady=10)

        self.withdraw_button = tk.Button(self.root, text="Withdraw", command=self.withdraw, font=("Helvetica", 12), bg='orange')
        self.withdraw_button.pack(pady=10)

        self.deposit_button = tk.Button(self.root, text="Deposit", command=self.deposit, font=("Helvetica", 12), bg='orange')
        self.deposit_button.pack(pady=10)

        self.exit_button = tk.Button(self.root, text="Exit", command=self.confirm_exit, font=("Helvetica", 12), bg='orange')
        self.exit_button.pack(pady=20)

    def check_balance(self):
        messagebox.showinfo("Balance", f"Your current balance is {self.balance}")

    def withdraw(self):
        try:
            amount = simpledialog.askinteger("Withdraw", "Enter amount to withdraw:", parent=self.root)
            if amount is not None:
                if amount <= self.balance:
                    self.balance -= amount
                    messagebox.showinfo("Withdraw", f"{amount} is debited from your account.\nYour updated balance is {self.balance}.")
                else:
                    messagebox.showerror("Error", "Insufficient balance.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a number.")

    def deposit(self):
        try:
            amount = simpledialog.askinteger("Deposit", "Enter amount to deposit:", parent=self.root)
            if amount is not None:
                self.balance += amount
                messagebox.showinfo("Deposit", f"{amount} is credited to your account.\nYour updated balance is {self.balance}.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a number.")

    def confirm_exit(self):
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = ATMApp(root)
    root.mainloop()
