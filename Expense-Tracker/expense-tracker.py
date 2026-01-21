from collections import defaultdict
from datetime import datetime
import pprint

class Solution:
    def __init__(self):
        self.expenses= defaultdict(list)
        self.income = defaultdict(list)

    def add_expense(self, amount: float, category: str, date: str):
        self.expenses[category].append({"amount" : amount, "date" : date})

    def add_income(self, amount: float, source: str, date: str):
        self.income[source].append({"amount": amount, "date": date})

    def view_expense(self):
        if self.expenses:
            return self.expenses
        return "No expenses to report"
    
    def view_income(self):
        if self.income:
            return self.income
        return "No income to report"
    
    def total(self):
        total_per_category = defaultdict(float)
        total_income = defaultdict(float)

        ## get categories
        for each_c in self.expenses:
            ## get the expenses
            for each_e in self.expenses[each_c]:
                total_per_category[each_c] += each_e["amount"]

        for each_s in self.income:
            for each_i in self.income[each_s]:
                total_income[each_s] += each_i["amount"]

        return total_per_category, total_income

    def balance(self):
        total_expense = 0
        total_income = 0

        for each_c in self.expenses:
            for each_e in self.expenses[each_c]:
                total_expense += each_e["amount"]

        for each_s in self.income:
            for each_i in self.income[each_s]:
                total_income += each_i["amount"]

        balance = total_income - total_expense
        return balance

    def month_filter(self):
        format_string = "%Y-%m-%d"
        month = int(input("Enter month (1-12): "))

        expense_totals = defaultdict(float)
        income_totals = defaultdict(float)

        for category, expenses in self.expenses.items():
            for e in expenses:
                date = datetime.strptime(e["date"], format_string)
                if date.month == month:
                    expense_totals[category] += e["amount"]

        for source, incomes in self.income.items():
            for i in incomes:
                date = datetime.strptime(i["date"], format_string)
                if date.month == month:
                    income_totals[source] += i["amount"]

        return expense_totals, income_totals

    
    def year_filter(self):
        format_string = "%Y-%m-%d"
        year = int(input("Enter year (e.g. 2024): "))

        expense_totals = defaultdict(float)
        income_totals = defaultdict(float)

        for category, expenses in self.expenses.items():
            for e in expenses:
                date = datetime.strptime(e["date"], format_string)
                if date.year == year:
                    expense_totals[category] += e["amount"]

        for source, incomes in self.income.items():
            for i in incomes:
                date = datetime.strptime(i["date"], format_string)
                if date.year == year:
                    income_totals[source] += i["amount"]

        return expense_totals, income_totals


    def cli_menu(self):
        menu_options = {
            "1": self.view_income,
            "2": self.view_expense,
            "3": self.balance,
            "4": self.month_filter,
            "5": self.year_filter
        }

        while True:
            print("Hi there! This is your expense tracker")
            print("Here you can see:")
            print("1.View your income")
            print("2.View your expenses")
            print("3.View your balance")
            print("4.View your income and expenses per month")
            print("5.View your income and expenses per year")
            print("6.exit")

            choice = input("Enter your choice: ").strip()

            if choice in menu_options:
                pprint.pprint(menu_options[choice]())
            elif choice == "6":
                print("Have a greeat day!")
                break    
            else:
                print(f"Invalid choice '{choice}'. Please try again.")

if __name__ == "__main__":
    tracker = Solution()
    tracker.cli_menu()
