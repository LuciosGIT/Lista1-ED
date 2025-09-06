# Questão 7

from Print import Print

class Queue:

    def __init__ (self):
        self.first = None
        self.last = None
        self.size = 0
        

    def input_request(self, number, file_size):

        newNode = Print(number, file_size)

        if not self.first:
            self.first = newNode
            self.last = newNode
            self.last.next = self.first
            self.size += 1
            return
        
        else:
            self.last.next = newNode
            self.last = newNode
            self.last.next = self.first
            self.size += 1
            return

    def peek(self):
        if not self.first:
            print("Fila vazia")
            return

        current = self.first
        count = 0
        while count < self.size:
            print(current.number)
            current = current.next
            count += 1
        print("None")


    def attend(self):

        if not self.first:
            raise Exception('A fila está vazia!')
        
        elif self.size == 1:
            self.first = None
            self.last = None
            self.size -= 1
        
        else:
            self.first = self.first.next
            self.last.next = self.first
            self.size -= 1
            return


queue = Queue()

queue.input_request(12, '500mb')
queue.input_request(9, '1GB')
queue.input_request(5, '340mb')
queue.input_request(125, '280mb')
queue.input_request(1, '150mb')
queue.input_request(24, '240mb')

queue.attend()


queue.peek()

        

    