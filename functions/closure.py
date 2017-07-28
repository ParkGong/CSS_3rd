def account(name, m):
    #account의 지역 변수 name, m
    def add(money):
        #free variable을 변경하기 위해
        nonlocal m
        m += money
        #free variable name도 접근은 ok!
        return name, m
    #함수 내 함수 add를 반환
    return add

if __name__ == "__main__":
    f1 = account('yang', 1000)
    f2 = account('kim', 500)

    f1(200)
    f2(600)
    
