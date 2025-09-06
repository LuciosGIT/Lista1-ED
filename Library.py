## Questão 1

from Book import Book

class Library:

    def __init__(self):
        self.head = None
        self.size = 0
    

    def add_book(self, title, author, year, code) -> None:
        newBook = Book(title, author, year, code)
        if not self.head:
            self.head = newBook
            self.size += 1
        else:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = newBook
            self.size += 1


    def display_book(self, title) -> str:
        pointer = self.head

        while pointer:
            if pointer.title == title:
                return f"O livro de título '{title}' foi encontrado e o seu autor é {pointer.author}"
            pointer = pointer.next
        raise Exception('Livro não encontrado')
    
    def remove_book(self, code) -> None:
        if not self.head:
            raise Exception('A biblioteca está vazia')
        
        if self.head.code == code:
            self.head = self.head.next
            self.size -= 1
            return f'O livro com código {code} foi removido com sucesso'
        
        prev = self.head
        pointer = self.head.next
        while pointer:
            if pointer.code == code:
                prev.next = pointer.next
                self.size -= 1
                return f'O livro com código {code} foi removido com sucesso'
            prev = pointer
            pointer = pointer.next 
        raise Exception('Livro não encontrado')
    
    def list_books(self) -> None:
        if not self.head:
            raise Exception('A biblioteca está vazia')
        pointer = self.head
        while pointer:
            print(f'Título: {pointer.title}, Autor: {pointer.author}, Ano: {pointer.year}, Código: {pointer.code}')
            pointer = pointer.next

            