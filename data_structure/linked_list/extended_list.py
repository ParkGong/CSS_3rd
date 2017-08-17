from linked_list import *

class LinkedListEx(LinkedList):
    def search(self, target, mode = 'next'):
        if mode == 'first':
            data = self.traverse('first')
        else:
            data = self.traverse('next')
            
        while data:
            if target == data:
                return data
            data = self.traverse()
        return None

    def update(self, data):
        self.current.data = data

    def replace(self, target, f):
        num_data = self.count(target)

        data = self.search(target, 'first')
        self.update(f(data))

        for i in range(num_data-1):
            data = self.search(target)
            self.update(f(data))

    def remove(self, target):
        data = self.traverse('first')
        while data:
            if data == target:
                return super().remove()
            
            data = self.traverse()

    def count(self, target):
        cnt = 0
        data = self.search(target, 'first')
        while data:
            cnt += 1
            data = self.search(target)
                
        return cnt

if __name__ == "__main__":
    slist = LinkedListEx()#1
    print("데이터의 개수 : {}".format(slist.size()))
    show_list(slist)
    print('')

    slist.append(2)#2
    slist.append(3)
    slist.append(1)
    slist.append(5)
    slist.append(2)
    slist.append(10)
    slist.append(7)
    slist.append(2)
    
    print("데이터의 개수 : {}".format(slist.size()))
    show_list(slist)
    print('\n')

    slist.replace(2, lambda x: x * 2)

    print("데이터의 개수 : {}".format(slist.size()))
    show_list(slist)
    print('\n')
    
    
    data = slist.remove(4)
    while data:
        print("데이터의 개수 : {}".format(slist.size()))
        show_list(slist)
        print('\n')
        data = slist.remove(4)

    slist.append(3)
    print("데이터의 개수 : {}".format(slist.size()))
    show_list(slist)
    
