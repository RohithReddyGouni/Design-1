#Time Complexity - O(1)
#Space Complexity - O(n)

class MyHashMap:
    
    class Node:
        def __init__(self,key,value):
            self.key=key;
            self.value=value;
            self.next=None;

    def __init__(self):
        self.hashList=[None]*10000;
    
    def hashKey(self,key):
        
        return key%10000;
    
    def findNode(self,head,key):
        current=head;
        prev=None;
        while current !=None and current.key!=key:
            prev=current;
            current=current.next;
        return prev;
            
        
    def put(self, key: int, value: int) -> None:
        hashIndex=self.hashKey(key);
        if self.hashList[hashIndex]==None:
            self.hashList[hashIndex]=self.Node(-1,-1);
        prev=self.findNode(self.hashList[hashIndex],key)
        
        if prev.next==None:
            prev.next=self.Node(key,value);
        else:
            prev.next.value=value;
        
        

    def get(self, key: int) -> int:
        hashIndex=self.hashKey(key);
        if self.hashList[hashIndex]==None:
            return -1;
        prev=self.findNode(self.hashList[hashIndex],key)
        return -1 if prev.next==None else prev.next.value

    def remove(self, key: int) -> None:
        hashIndex=self.hashKey(key);
        if self.hashList[hashIndex]==None:
            return 
        prev=self.findNode(self.hashList[hashIndex],key);
        if prev.next==None:
            return None;
        prev.next=prev.next.next;
        
            
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)