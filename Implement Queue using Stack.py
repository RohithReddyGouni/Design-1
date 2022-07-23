# Time Complexity:
# push() - O(1)
# pop() - O(1)
# peek() - O(1) 
# empty() - O(1)

class MyQueue:

    def __init__(self):
        self.IN=[];
        self.OUT=[];

    def push(self, x: int) -> None:
        self.IN.append(x);


    def pop(self) -> int:
        if len(self.OUT)==0:
            while self.IN:
                self.OUT.append(self.IN.pop())
        return self.OUT.pop();

    def peek(self) -> int:
        if len(self.OUT) == 0:
            while self.IN:
                self.OUT.append(self.IN.pop())
        return self.OUT[len(self.OUT)-1];



    def empty(self) -> bool:
        return len(self.IN) + len(self.OUT) == 0;


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
