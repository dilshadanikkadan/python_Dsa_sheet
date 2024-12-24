class Node:
    def __init__(self,value,next = None):
        self.value= value
        self.next = next
    
class CircularLinkedList:
    def __init__(self):
        self.head = None        
        self.tail = None
        
    # for simplifying the print process    ):
    def __iter__(self):
        curr = self.head
        while curr:
            yield curr
            if curr.next == self.head:
                break
            curr = curr.next
        
    def boot_cll(self,value = 0):
        new_node = Node(value)
        new_node.next = new_node
        self.tail = new_node
        self.head = new_node
             
    def insert_el(self,value = 0,position = 0):
        new_node = Node(value)
        if position == 0:
           new_node.next = self.head
           self.head = new_node
           self.tail.next = new_node
           
        elif position == -1 :
            new_node.next = self.tail.next
            self.tail = new_node
        else:
            curr = self.head
            index = 0
            while curr and index < position-1:
                curr = curr.next
                index += 1
            next_node = curr.next  
            curr.next = new_node
            new_node.next = next_node       
            
    
cll = CircularLinkedList()
cll.boot_cll()
cll.insert_el(10)               
cll.insert_el(20,1)               
cll.insert_el(30,2)               
cll.insert_el(40,3) 

print([node.value for node in cll])              

