from Deque import Deque

class Browser:
    def __init__(self):
        self.history = Deque()
        self.stack = []   

    def access_page(self, url):
        self.history.insertOnTail(url)
        self.stack.clear()
        print(f"Acessou: {url}")

    def back(self):
        if self.history.size <= 1:
            print("Não há páginas para voltar!")
            return
        page = self.history.removeFromTail()
        self.stack.append(page)
        print(f"Voltou para: {self.history.peek()[-1]}")

    def forward(self):
        if not self.stack:
            print("Não há páginas para avançar!")
            return
        page = self.stack.pop()
        self.history.insertOnTail(page)
        print(f"Avançou para: {page}")

    def show_history(self):
        print("Histórico:", " -> ".join(map(str, self.history.peek())))

    
nav = Browser()
nav.access_page("google.com")
nav.access_page("youtube.com")
nav.access_page("github.com")

nav.show_history()

nav.back()
nav.show_history()

nav.forward()
nav.show_history()