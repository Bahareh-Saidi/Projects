from collections import defaultdict
from datetime import datetime

class Solution:
    def __init__(self):
        self.expenses= defaultdict(list)

    def add_expense(self, amount: float, category: str, date: str):
        self.expenses[category].append({"amount" : amount, "date" : date})

    def view(self):
        if self.expenses:
            return self.expenses
        return "No expenses to report"
    
    def total(self):
        total_per_category = defaultdict(float)

        ## get categories
        for each_c in self.expenses:
            ## get the expenses
            for each_e in self.expenses[each_c]:
                total_per_category[each_c] += each_e["amount"]

    def month_filter(self):
        total_per_month = defaultdict(float)
        format_string = "%Y-%m-%d"
        target_month = 3

        ## get categories
        for each_c in self.expenses:
            ## get the expenses
            for each_m in self.expenses[each_c]:
                months = datetime.strptime(each_m["date"], format_string)
                if target_month == months.month:
                    total_per_month[each_c] += each_m["amount"]
