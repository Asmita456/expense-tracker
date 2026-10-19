
import math
from datetime import datetime


def get_required_text(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("This field cannot be empty. Please try again.")


def get_valid_amount():
    while True:
        try:
            amount = float(input("Enter amount: Rs "))

            if not math.isfinite(amount):
                print("Amount must be a finite number.")
            elif amount <= 0:
                print("Amount must be greater than zero.")
            else:
                return amount

        except ValueError:
            print("Invalid input! Please enter a number.")


def get_valid_date():
    while True:
        date_input = input(
            "Enter date (YYYY-MM-DD): "
        ).strip()

        try:
            parsed_date = datetime.strptime(
                date_input, "%Y-%m-%d"
            )

            if parsed_date.strftime("%Y-%m-%d") == date_input:
                return date_input

            print("Invalid date! Please use YYYY-MM-DD.")

        except ValueError:
            print("Invalid date! Please use YYYY-MM-DD.")
