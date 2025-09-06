# Questão 9

from PriorityNode import PriorityNode


class PriorityQueue:

    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def insert(self, data, priority):

        newNode = PriorityNode(data, priority)

        pointer = self.first

        if self.first == None:
            self.first = newNode
            self.last = newNode
            self.size += 1
            return

        if self.first.priority < priority:
            newNode.next = self.first
            self.first = newNode
            self.size += 1
            return

        while pointer:

            if pointer == self.last:
                pointer.next = newNode
                self.last = newNode
                self.size += 1
                return

            elif pointer.next.priority >= newNode.priority:
                pointer = pointer.next

            else:
                newNode.next = pointer.next
                pointer.next = newNode
                self.size += 1
                return
            
    def remove(self):


        if not self.first:
            raise Exception('A fila está vazia!')

        else:
            self.first = self.first.next
            self.size -= 1


    def peek(self):
        elements = []
        pointer = self.first
        while pointer:
            elements.append((pointer.data, pointer.priority))
            pointer = pointer.next
        return elements


fila = PriorityQueue()
fila.insert('prioridade1', 1)
fila.insert('prioridade3', 3)
fila.insert('prioridade3', 3)
fila.insert('prioridade2', 2)

fila.remove()

print(fila.peek())
