class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __iter__(self):
        curr = self.head
        while curr:
            yield curr.value
            curr = curr.next
            
    def pop(self,position=None):
        if position == 0 :
            self.head = self.head.next
        elif position is not None:
            curr =  self.head
            index = 0
            while curr and index < position -1:
                index += 1
                curr = curr.next
            print(curr.value)   
            curr.next = curr.next.next 
        else :
            curr = self.head
            while curr.next.next:
                curr = curr.next
            print("value is",curr.value)
            curr.next = None
            self.tail = curr  
                
                     
    # mostly we can see this in redis for managing the effinciency of insetion in both edge
    #------------------- o(1)
    def l_push(self,value):
        new_node  = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else :
            new_node.next = self.head
            self.head = new_node    
            
     # .... redis plays with this always ):   
     #------------------- o(1)
    def r_push(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else :
            self.tail.next  = new_node
            self.tail =new_node 
            
     # managing all edge cases when a new element in insetion element with pos                   
    def insert_el(self,value,position):
        new_node = Node(value)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            if self.tail is None:
                self.tail = new_node
        elif position == -1:
            if self.tail is None:
                self.head = new_node
                self.tail = new_node
            else :   
                self.tail.next = new_node
                self.tail = new_node
        else:
            index = 0
            curr = self.head
            while curr and index < position -1:
                curr = curr.next
                index += 1
            temp_node = curr.next
            curr.next = new_node
            new_node.next = temp_node 
            
            if new_node.next is None:
                self.tail = new_node  

sll = SingleLinkedList()
sll.insert_el(10, 0)
sll.r_push(11)
sll.r_push(12)
sll.r_push(13)
sll.l_push(2)
sll.l_push(3)
# sll.insert_el(20, -1)
# sll.insert_el(30, -1)
# sll.insert_el(5, 1)
# sll.insert_el(3, 2)
# sll.insert_el(99, 4)
print([value for value in sll.__iter__()])
sll.pop()
sll.r_push(17)
print([value for value in sll.__iter__()])

                         