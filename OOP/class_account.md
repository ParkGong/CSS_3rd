# Computer Science School
## object-oriented programming

---

## class
 - class의 구조
 ```python
 #class
class Account:
   #constructor
    def __init__(self, name, money):
        #member
        self.user = name
        self.balance = money
    #method 
    def deposit(self, money):
        if money < 0:
            return
        self.balance += money
 ```
---

## constructor
  - 생성자 
    - 객체 생성할 때 호출
    - 멤버 초기화
```python
def __init__(self, name, money):
        #member
        self.user = name
        self.balance = money
```
---

##  destructor
  - 소멸자
  - 객체 소멸할 때 호출
  - 주 목적은 메모리 해제
```python
#destructor
    def __del__(self):
        pass
```
---

## object member
  - variable in object
```python
def __init__(self, name, money):
        #object member
        self.user = name
        self.balance = money
```
---

## object method
  - function used by object
  - 객체 생선 전에는 호출할 수 없다.
```python
def deposit(self, money):
        if money < 0:
            return
        
        self.balance += money
```
---

## class member
  - variable in class
  - 모든 객체가 공유
```python
class Account:
    #class member
    bank = 'Fast Bank'
```
---

## class method
  - function used by class
  - 객체 생성 전에도 호출할 수 있다.
```python
#class method
    @classmethod
    def get_bank_info(cls):
        print('''
Fast Bank
1. establishment year : 1977
2. headquarters : Seoul, Korea
3. staff : 1700
''')
```
---

## object 생성
```python
my_acnt = Account('greg', 5000)
```
---

## object method 호출
```python
#1. by object
my_acnt.deposit(500)
#2. by class : 쓰이지 않음
Account.deposit(my_acnt, 500)
```
---

## class member 접근
```python
#1.by class 
print(Account.bank)    
#2.by object
print(my_acnt.bank)
```
---

## class method 호출
```python
#1.by class
Account.get_bank_info()
#2.by object
my_acnt.get_bank_info()
```
---

## message passing
  - interacts with other objects
    - by calling methods
    - changes the state of the object(member)
    - asks the receiver to call a specific method
```python
def transfer(self, other, money):
        mon = self.withdraw(money)
        if mon:
            #상대 객체의 메서드를 호출
            other.deposit(mon)
            return True
        else:
            return False
```