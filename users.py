class User:
    def __init__(self,user_id):
        self.bal = 100
    def Check_bal(self):
        return self.bal
    def Buy(self):
        if self.bal <= 0:
            print("Bitch you'r broke how can you buy something when you're that broke HAHAHAHA")
            return "Bitch you'r broke how can you buy something when you're that broke HAHAHAHA"
        else:
            self.bal = self.bal-50
            print (self.bal)
            return self.bal

