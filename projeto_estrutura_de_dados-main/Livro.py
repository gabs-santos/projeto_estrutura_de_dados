class Livro:
    def __init__(self, titulo, autor, isbn, faixa_etaria):
        if len(str(isbn)) != 13:
            raise ValueError("ISBN deve ter 13 dígitos!")
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.faixa_etaria = faixa_etaria
        self.disponivel = True  