# Questões 3 e 5

from Pessoa import Pessoa


class CircularLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0
        self.tail = None

    def insert(self, nome, idade):

        if not self.head:
            newNode = Pessoa(nome, idade)
            self.head = newNode
            self.tail = newNode
            self.tail.next = self.head
            self.size += 1
            return

        newNode = Pessoa(nome, idade)

        # para adicionar antes do head
        if idade < self.head.idade:
            newNode.next = self.head
            self.head = newNode
            self.tail.next = self.head
            self.size += 1
            return

        prev = self.head
        pointer = self.head.next

        # para adicionar no meio e fim da lista
        while pointer != self.head and idade >= pointer.idade:
            prev = pointer
            pointer = pointer.next 
            
        prev.next = newNode
        newNode.next = pointer

        if prev == self.tail:
            self.tail = newNode
        
        self.tail.next = self.head
        self.size += 1

    def peek(self):
        if not self.head:
            print("Lista vazia")
            return

        current = self.head
        while True:
            print(current.idade, end="->")
            current = current.next
            if current == self.head:
                break
        print("(circular)")


# Testando:
linked_list3 = CircularLinkedList()


linked_list3.insert('Charlie', 10)
linked_list3.insert('Alice', 12)
linked_list3.insert('Bob', 15)
linked_list3.insert('Charlie', 10)
linked_list3.insert('David', 14)


linked_list3.peek()
