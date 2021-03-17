class Category:

    def __init__(self, name):
        self.CategoryName = name
        self.ledger = []

    def deposit (self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})
        
        
    def withdraw (self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({"amount":(0 - amount), "description":description})
            return True
        else:
            return False
    
    def get_balance (self):
        t = 0
        for i in range (len(self.ledger)):
            t = t + self.ledger[i]["amount"]
        return t

    def check_funds (self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def transfer (self, amount, Other_cat):
        if self.check_funds(amount):
            Transfer_to = "Transfer to " + Other_cat.CategoryName
            self.ledger.append({"amount":(0 - amount), "description":Transfer_to})
            Transfer_from = "Transfer from " + self.CategoryName
            Other_cat.deposit(amount, Transfer_from)
            return True
        else:
            return False

    def __str__(self):
        title = f"{self.CategoryName:*^30}\n"
        items = ""
        total = 0
        for i in range(len(self.ledger)):
            items += f"{self.ledger[i]['description'][0:23]:23}" + f"{self.ledger[i]['amount']:>7.2f}" + '\n'
            total += self.ledger[i]["amount"]
        
        output = title + items + "Total: " + str(total)
        return output

def create_spend_chart(categories):
