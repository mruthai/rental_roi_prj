class Investor():
    """Class holds all investor """
    def __init__(self, name, email):
        self.creditial = {"Name of Company":f"{name}", "Email Address":f"{email}"}
        # print(self.creditial)

class Rinvest():
    """investor creditial blueprint"""
    def __init__(self):
        self.rio = {"Projected Income":[],"Projected Expenses":[],"Projected Cash Recieved":[],"Return on Investment":[]}
      
    def run(self):
        """Method to run the program"""
        while True:
            u_choice = input("\nWould you like to find out your ROI on rental property? (y/n):")

            if (u_choice) == "y":
                # self.invest_name()
                threw_cal = Calc(self.invest_name())
                threw_cal.income()
            else:
                (u_choice) == "n"
            return

    def invest_name(self):
        """method to get inventors creditials"""
        name = input("Let's get started with your name of your company?: ").lower()
        email = input("What's your company email address: ").lower()

        cred1 = Investor(name, email)
        return cred1
        
        

class Calc():
    """Main Class handles all calculations"""
    def __init__(self,name_cal):
        self.main_cal = name_cal
        print(self.main_cal.creditial["Name of Company"])

    def prop_cost(self):
        pass

    def income(self):
        """method to have use input montly lease income"""
        rent_in = float(input("Input your potential lease rate/month: "))
        # if their rental rate is 0 or less than
        # self.t_month_income = self.rent_in
        print(f"{rent_in}")
        income_result = rent_in
        self.expenses(income_result)
        return income_result

    def expenses(self, income_result):
        """Collect all expenses from investor"""
        mort_month = float(input("Input your potential mortgage rate/month: "))
        taxes = float(input("Input your potential taxes rate/month: "))
        insur = float(input("Input your potential insurance rate/month: "))
        repairs = float(input("Input your potential repairs rate/month: "))
        capexp = float(input("Input your potential capital expense rate/month: "))
        propmgmt = float(input("Input your potential property management rate/month: "))
        vacancy = float(input("Input your potential vancancy rate/month: "))
        # print(f"{t_month_expense}")
        t_month_expense = float(mort_month) + float(taxes) + float(insur) + float(repairs) + float(capexp) + float(propmgmt) + float(vacancy)
        self.cash_flow(t_month_expense, income_result)
        return t_month_expense


    def cash_flow(self, t_month_expense, income_result):
        """Difference of income and expenses"""
        t_flow = income_result - t_month_expense
        print(f"This is what we have so far: ${income_result} montly lease - {t_month_expense} monthly expense =")
        print(f"TOTAL CASH FLOW: ${t_flow}")
        self.return_invest(t_flow) #got to return_invent
        return t_flow

    def return_invest(self, t_flow):
        """Calcuate total investment"""
        downpay = float(input("Input your down payment on your potential property?: "))
        #mortgage calculator
        renovation = float(input("Input your projected renovation cost: "))
        oprojections = float(input("Input your potential misc. expenses: "))
        total_invest = downpay + renovation + oprojections

        ann_cash_flow = float(t_flow) * 12
        return_on_invest = float(ann_cash_flow) / float(total_invest) * 100
        print(f"Your cash on cash ROI is: {return_on_invest}%")
        return return_on_invest


shouldwe = Rinvest()
shouldwe.run()

