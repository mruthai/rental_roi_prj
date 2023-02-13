

class Income():
    """Class holds investor income """
    def __init__(self, income_type, income):
        self.income_type = income_type
        self.income = income
      

class Expenses():
    """Class holds investor expense """
    def __init__(self, expense_type, expense):
        self.expense_type = expense_type
        self.expense = expense

class Investment():
    """Class holds invested mones and calculates roi"""
    def __init__(self, invest_type, invest):
        self.invest_type = invest_type
        self.invest = invest
        
class Calculator():
    """Class holds running the program and accepting inputs and calculating ROI"""
    def __init__(self):
        self.add_income = []
        self.add_expense = []
        self.add_invest = []
        self.user_info ={}
        

    def run(self):
        """Method to run the program"""
        while True:
            
            print("PROPERTY RENTAL VALUE")
            u_choice = input("Input: '1' = Income | '2' = Expense | '3' = Investment | '4' = Auto-Calcuate ROI | 'q' for quit:")

            if u_choice == "1":
                income_type = input("Input income type(e.g. rental/storage/laundry,etc.): ").lower()
                income = (input("Input your income amount: "))
                self.income_s(income_type, income)

            elif u_choice == "2":
                expense_type = input("Input expense type(e.g. mortgage,taxes,insurance,etc.): ").lower()
                expense = (input("Input your expenses amount: "))
                self.expense_s(expense_type, expense)
                
            elif u_choice == "3":
                invest_type = input("Input investment type(e.g. downpayment,renovation,misc.,etc.): ").lower()
                invest = (input("Input your investment amount: "))
                self.investment(invest_type, invest)
                
            elif u_choice == "4":
                self.cal_all()

            elif u_choice == "q":
                print("Thank you!")
                return

    def income_s(self, income_type, income):
        if income.isdigit():
            self.add_income.append(income)
        else:
            print("Unfortunately you didn't type in a digit")
            return
        mones = Income(income_type, income)
        self.user_info[income_type] = mones
        return

    def expense_s(self, expense_type, expense):
        if expense.isdigit():
            self.add_expense.append(expense)
        else:
            print("Unfortunately you didn't type in a digit")
            return
        ex_in = Expenses (expense_type, expense)
        self.user_info[expense_type] = ex_in
        return
        
    def investment(self, invest_type, invest):
        if invest.isdigit():
            self.add_invest.append(invest)
        else:
            print("Unfortunately you didn't type in a digit")
            return
        in_mones = Investment(invest_type, invest)
        self.user_info[invest_type] = in_mones
        return

    def cal_all(self): 
        tot_incom = 0
        for num in self.add_income:
            tot_incom += (int(num))
        
        tot_expense = 0
        for num in self.add_expense:
            tot_expense += (int(num))

        tot_invest = 0
        for num in self.add_invest:
            tot_invest += (int(num))
        cash_flow = tot_incom - tot_expense
        ann_cash_flow = float(cash_flow) * 12
        return_on_invest = (float(round(ann_cash_flow)) / float(round(tot_invest))) * 100
        print("=*" * 10)
        print(f"Your cash on cash ROI is: {return_on_invest}%")
        print("=*" * 10)

property = Calculator()
property.run()
