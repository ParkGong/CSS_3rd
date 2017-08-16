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

    print('data 2 의 개수 : {}'.format(slist.count(2)))
    print('')

    
    data = slist.remove(2)
    while data:
        print("데이터의 개수 : {}".format(slist.size()))
        show_list(slist)
        print('\n')
        data = slist.remove(2)

    slist.append(3)
    print("데이터의 개수 : {}".format(slist.size()))
    show_list(slist)
    
