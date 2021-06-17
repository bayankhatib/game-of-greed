class Banker:
    '''
    Banker class have two method's 
    shelf for save point permanentaly while the round
    and banking for save the point's for the round
    '''
    def __init__(self,balance=0,shelved=0):
        self.balance=balance
        self.shelved=shelved

    def shelf(self,value):
       self.shelved+=value
       return self.shelved

    def bank(self):
        self.balance+=self.shelved
        self.clear_shelf()
        return self.balance

    def clear_shelf(self):
        self.shelved=0