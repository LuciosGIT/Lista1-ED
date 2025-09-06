##  Questão 2

from Node import Node

class LinkedList:

    def __init__ (self):
        self.head = None
        self.size = 0

    
    def remove_duplicate(self):

        '''Remove elementos duplicados de uma lista encadeada.'''

        # Complexidade de tempo: O(n)
        # Otimização: Utilizar uma lista ordenada, já que cada elemento consecutivo estaria em ordem crescente. Portanto, duplicados estariam consecutivos e encadeados, removendo o uso do set()'''

        if not self.head:
            raise Exception('A lista está vazia')
        
        added_elements = []
        prev = self.head
        pointer = self.head.next
        
        added_elements.append(prev.data)
        while pointer:
            if pointer.data in added_elements:
                prev.next = pointer.next
                self.size -= 1
            else:
                added_elements.append(pointer.data)
                prev = pointer
            pointer = pointer.next

    def insert(self, valor):
        newNode = Node(valor)
        if not self.head:
            self.head = newNode
            self.size += 1
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = newNode
        self.size += 1

        
    def peek(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


##Testando:
'''linked_list = LinkedList()

linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(2)
linked_list.insert(4)
linked_list.insert(1)

linked_list.remove_duplicate()

linked_list.peek()'''

