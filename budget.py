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
    
    # calculate expenses in each category
    category_spend = []

    for i in range (len(categories)):
        spend_in_ledger = []
        for j in range (len(categories[i].ledger)):
            if categories[i].ledger[j]["amount"]<0:
                spend_in_ledger.append(categories[i].ledger[j]["amount"])
        total_spend_in_ledger = sum(spend_in_ledger)
        category_spend.append(total_spend_in_ledger)
    
    # calculate total expenses
    total_spend = sum(category_spend)
    
    # calculate % expenditure
    category_percent = []
    for i in range (len(category_spend)):
        percent = (int(category_spend[i]/total_spend*10))*10
        category_percent.append(percent)
    
    # print out chart
    print ("Percentage spent by category")

    # generating a line on the chart
    chart_line = []
    yaxis = [x for x in range (100,-1,-10)]
    for i in range (len(yaxis)):
        chart = []
        for j in range (len(category_percent)):
            if yaxis[i] > category_percent[j]:
                chart.append("   ")
            else:
                chart.append("o  ")
        chart_line.append("".join(chart))   
    
    # putting to gether the chart display
    chart_display = ""
    for i in range (len(yaxis)):
        chart_display += f"{yaxis[i]:>3}" + "|" + " " + chart_line[i] + '\n'
    chart_display = chart_display + "    -" + ("---"*len(categories))
    print (chart_display)
