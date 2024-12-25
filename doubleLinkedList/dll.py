class Node:
    def __init__(self,value,next = None,prev = None):
        self.value = value
        self.next = next
        self.prev = prev

class DoubleLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        
        curr = self.head
        
        while curr:
            yield curr
            curr = curr.next
            
    def reverse_print(self):
        
        curr = self.tail
        res =[]
        while curr :
            res.append(curr.value)
            curr = curr.prev
        print(res)    
        
    def pop(self,position = -1):
        if position == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:    
              self.head = self.head.next
              self.head.prev = None  
        elif position == -1:
          if self.tail == self.head:
              self.tail = None        
              self.head = None
          else:
              self.tail = self.tail.prev
              self.tail.next = None
        else:
         
          index = 0
          curr = self.head
          while curr and index == position -1:
              curr = curr.next
              
          curr.next  = curr.next.next
          curr.next.prev = curr    
                      
                          
        
    def l_push(self,value):
        
        new_node  = Node(value)
        if self.head is None:
           self.head = new_node
           self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node   

dll = DoubleLinkedList()
dll.l_push(1)
dll.l_push(2)
dll.l_push(3)
dll.l_push(4)

print([node.value for node in dll])
dll.pop(2)
print([node.value for node in dll])
# dll.reverse_print()               