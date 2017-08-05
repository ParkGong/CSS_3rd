#계좌 클래스 구현
class Account:
    #class member
    bank = 'Fast Bank'

    #class method
    @classmethod
    def get_bank_info(cls):
        print('''Fast Bank
1. establishment year : 1977
2. headquarters : Seoul, Korea
3. staff : 1700
''')
    
    #constructor
    def __init__(self, name, money):
        #object member
        self.user = name
        self.balance = money

    #destructor
    def __del__(self):
        pass

    #object methord
    def deposit(self, money):
        if money < 0:
            return
        self.balance += money

    def withdraw(self, money):
        if money > 0 and money <= self.balance:
            self.balance -= money
            return money
        else:
            return None

    def transfer(self, other, money):
        '''
        obj.transfer(other, money) -> bool
        other : The object to interact with
        money : money the user wants to send

        returns True if the balance is enough to transfer
        returns False if not
        '''
        mon = self.withdraw(money)
        if mon:
            other.deposit(mon)
            return True
        else:
            return False

    def __str__(self):
        return 'user : {}, balance : {}'.format(self.user, self.balance)
            
if __name__== "__main__":
    #object를 생성하는 방법
    my_acnt = Account('greg', 5000)
    your_acnt = Account('john', 1000)

    #생성 확인
    print('object created')
    print(my_acnt)
    print(your_acnt)
    print('')

    #object method를 호출하는 방법
    #1. by object
    my_acnt.deposit(500)
    #2. by class
    #Account.deposit(my_acnt, 500)

    #deposit 확인
    print('deposit')
    print(my_acnt)
    print('')
    
    #withdraw 함수 사용법
    print('withdraw')
    money = my_acnt.withdraw(1500)
    if money:
        print('withdrawn money : {}'.format(money))
    else:
        print('Not enough to withdraw')
    print('')
    
    #class member에 접근하는 방법
    print('class member')
    #1.by class 
    print(Account.bank)    
    #2.by object
    #print(my_acnt.bank)
    print('')

    #class method를 호출하는 방법
    print('class method')
    #1.by class
    Account.get_bank_info()
    #2.by object
    #my_acnt.get_bank_info()
    
    #message passing
    print("message passing")
    print(my_acnt)
    print(your_acnt)
    res = my_acnt.transfer(your_acnt, 2000)
    if res:
        print('transfer succeeded')
    else:
        print('transfer failed')
    print(my_acnt)
    print(your_acnt)
    
