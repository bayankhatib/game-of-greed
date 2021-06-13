class Banker:
    # pass
    def __init__(self,balance=0,shelved=0):
        self.balance=balance
        self.shelved=shelved

    def shelf(self,value):
       self.shelved=value

    def bank(self):
        total=self.shelved
        self.balance=self.shelved
        self.shelved=0
        return total

    def clear_shelf(self):
        self.shelved=0






    