#Q5.Read about the Tower of Hanoi algorithm. Write a program to implement it ?
def towerofhonoi(self, stack1, stack2, stack3):
    if self == 1:
        print("push x1 from",stack1,"to",stack2)
        return
    towerofhonoi(self-1, stack1, stack3, stack2)
    print("push x2",self,"from toh",stack1,"to toh",stack2)
    towerofhonoi(self-1, stack3, stack2, stack1)
self = 2
towerofhonoi(self, '10', '50', '20')
