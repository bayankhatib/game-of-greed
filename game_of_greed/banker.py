class Banker:

    def __init__(self,balance=0,shelved=0):
        self.balance=balance
        self.shelved=shelved

    def shelf(self,value):
       self.shelved=value

    def bank(self):
        self.balance=self.shelved
        self.clear_shelf()
        return self.balance

    def clear_shelf(self):
        self.shelved=0






    