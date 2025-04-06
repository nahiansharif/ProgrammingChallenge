# prepare for the interview question
# remember, you failed miserably in paycom interview, but you have 6 months until july to make a great comback. 

# singly linked list 

#define what node looks like. 

class node: 
    def __init__(self, data = None):
        self.data = data
        self.next = None
        
class linkedList:
    def __init__(self):
        self.head = node()
        
    def append(self, data): 
        newNode = node(data)
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = newNode
        
    def length(self):
        cur = self.head
        total = 0
        while cur.next is not None:
            cur = cur.next    
            total += 1   
        return total
    
    def display(self):
        elem = []
        cur = self.head
        while cur.next is not None:
            cur = cur.next
            elem.append(cur.data)
        print(elem)
        
    def search(self, data):
        cur = self.head
        index = 0
        while cur is not None:
            if cur.data == data:
                print(index) 
            cur = cur.next
            index += 1
          
    def get(self, index):
        if index >= self.length():
            print("ERROR: 'Get' Index out of range!")
            return None
        
        cur_idx = 0
        cur_node = self.head
        
        while True:
            if cur_idx == index:
                return cur_node.data
            
            cur_node = cur_node.next
            cur_idx += 1
            
    # pointers are fragile. You can change pointers anywhere. So be careful 
    def delete(self, data):
        cur = self.head
        prev = None
        
        while cur:
            if cur.data is data:
                if prev: 
                    prev.next = cur.next
                else: 
                    self.head = cur.next
            prev = cur
            cur = cur.next
            
            
    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        self.head = prev
        
    def insert(self, index, data):
        if index < 0 or index > self.length():
            print("ERROR: 'Insert' Index out of range!")
            return
        newNode = node(data)
        cur = self.head
        cur_idx = 0
        while True:
            if cur_idx == index:
                newNode.next = cur.next
                cur.next = newNode
                return
            cur = cur.next
            cur_idx += 1
            
    def has_cycle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data
    
    def remove_duplicates(self):
        cur = self.head
        prev = None
        seen = set()
        while cur:
            if cur.data in seen:
                prev.next = cur.next
            else:
                seen.add(cur.data)
                prev = cur
            cur = cur.next

        
          
list = linkedList()

list.append(3)
list.append(6)
list.append(9)
list.append(12)
list.append(15)
list.append(18)

# list.display()

list.search(6)
list.search(3)
list.search(9)

# print(list.get(3))

list.delete(12)
# list.display()


    
        
        

#---------------------------------------------------------------------------------
# doubly linked list

class node2():
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None
    
class ll2:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def append(self, data):
        newNode = node2(data)
        
        if self.head is None:
            self.head =  newNode
            self.tail = newNode
            return
                
        cur = self.head
        while cur.next is not None:
            cur = cur.next
       
        cur.next = newNode
        newNode.prev = cur        
        self.tail = newNode
        
    def earlyAppent(self, data):
        
        newNode = node2(data)
        
        if self.head is None:
            self.head =  newNode
            self.tail = newNode
            return
                
        self.head.prev = newNode
        newNode.next = self.head        
        self.head = newNode
                
    def display(self):
        cur = self.head
        elems = []
        while cur:
            elems.append(cur.data)
            cur = cur.next
        print(elems)
            
    def reverseDisplay(self):
        cur = self.tail
        elems = []
        while cur:
            elems.append(cur.data)
            cur = cur.prev
        print(elems)
        
    def length(self):
        total = 0
        cur = self.head
        while cur:
            total += 1
            cur = cur.next
        return total
    
    def delete(self, data):
        cur = self.head
        while cur:
            if cur.data == data:
                if cur.prev:
                    cur.prev.next = cur.next
                else:
                    self.head = cur.next
                    
                if cur.next:
                    cur.next.prev = cur.prev
                else:
                    self.tail = cur.prev
                    
                return
            cur = cur.next
            
    def insert_at_index(self, index, data):
        if index < 0:
            print("Index must be a positive integer")
            return
            
        newNode = node2(data)
        cur = self.head
        count = 0
        
        if index == 0:
            self.earlyAppent(data)
            return
        
        while cur and count < index:
            cur = cur.next
            count += 1
        
        if count == index:
            newNode.prev = cur.prev
            newNode.next = cur
            
            if cur.prev:
                cur.prev.next = newNode
            cur.prev = newNode
            
            if cur == self.head:
                self.head = newNode
            if cur == self.tail:
                self.tail = newNode
                
        else:
            print("Index out of bounds")
    
    def search(self, data):
        cur = self.head
        while cur:
            if cur.data == data:
                return True
            cur = cur.next
        return False
    
    def update_at_index(self, index, data):
        if index < 0:
            print("Index must be a positive integer")
            return
        
        cur = self.head
        count = 0
        while cur and count < index:
            cur = cur.next
            count += 1
        
        if cur:
            cur.data = data
        else:
            print("Index out of bounds")
    
    def remove_duplicates(self):
        cur = self.head
        seen = set()
        while cur:
            if cur.data in seen:
                self.delete(cur.data)
            else:
                seen.add(cur.data)
            cur = cur.next

# Testing the new methods
list = ll2()

for i in range(0, 12, 2):
    list.append(i)
    
list.display()
list.reverseDisplay()

for i in range(0, 12, 2):
    list.earlyAppent(i / 10)
    
list.display()

# Testing new methods
print(list.search(0.2))  # Should print True
list.update_at_index(2, 99)
list.display()  # Check if the element at index 2 is updated to 99

# Add some duplicates and remove them
list.append(4)
list.append(6)
list.remove_duplicates()
list.display()  # Should print the list without duplicates






