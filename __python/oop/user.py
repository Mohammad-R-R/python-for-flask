class user:
    def __init__(self,name,email):
        self.name=name
        self.email=email
        self.balance=0

    def deposite(self,amount):
        self.balance+=amount
        return 0

    def withdrwal(self,amount):
        self.balance-=amount
        return 0

    def transfer(self,amount,to_2):
       self.balance -=amount
       to_2.deposite(amount)







u1=user("mohammad","dddd@hotmail.com")
u2=user("ahmad","aaaa@hotmail.com")
u3=user("rasputin","rrrr@hotmail.com")
u1.deposite(100)
u1.deposite(200)
u1.deposite(50)
u1.withdrwal(50)
u1.transfer(100,u3)
print(u1.name,u1.email,u1.balance)
u2.deposite(50)
u2.deposite(40)
u2.withdrwal(20)
u2.withdrwal(50)
print(u2.name,u2.email,u2.balance)



u3.deposite(400)
u3.withdrwal(20)
u3.withdrwal(50)
u3.withdrwal(50)
print(u3.name,u3.email,u3.balance)

