import Livro
import Usuario
from Devolucao import Devolucao
from collections import deque

class Biblioteca:
    def __init__(self):
        self.livros = [] 
        self.usuarios = [] 
        self.historico_emprestimos = []  
        self.livros_emprestados = set() 

    def cadastrar_livro(self, titulo, autor, isbn, faixa_etaria, quantidade):
        print("\n--- Cadastro de Livro ---")
        try:
            livro = Livro.Livro(titulo, autor, isbn, faixa_etaria, quantidade)
            self.livros.append(livro)
            print(f"Livro '{titulo}' cadastrado com sucesso!")
        except ValueError as e:
            print(f"Erro: {e}")

    def cadastrar_usuario(self, nome, idade, documento, telefone):
        print("\n--- Cadastro de Usuário ---")
        usuario = Usuario.Usuario(nome, idade, documento, telefone)
        self.usuarios.append(usuario)
        print(f"Usuário '{nome}' cadastrado com sucesso!")
    
    def emprestar_livro(self, nome_usuario, titulo_livro):
        print("\n--- Empréstimo de Livro ---")
        usuario_encontrado = self.buscar_usuario_por_nome(nome_usuario)
        livro_encontrado = self.buscar_livro_por_titulo(titulo_livro)

        if usuario_encontrado and livro_encontrado:
            if livro_encontrado.disponivel:
                livro_encontrado.disponivel = False
                self.livros_emprestados.add(livro_encontrado.isbn)  #Armazena ISBN no SET
                self.historico_emprestimos.append({
                    "acao": "empréstimo",
                    "livro": titulo_livro,
                    "usuario": nome_usuario
                })
                print(f"Livro '{titulo_livro}' emprestado para {nome_usuario}!")
            else:
                print("Livro indisponível.")
        else:
            print("Usuário ou livro não encontrado.")
            
             
    def mostrar_historico(self):
        print("\n--- Histórico de Empréstimos ---")
        for registro in self.historico_emprestimos:
            print(f"{registro['acao'].upper()}: {registro['livro']} está com -> {registro['usuario']}")    
            
            

    def buscar_livro_por_titulo(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower().strip() == titulo.lower().strip():
                return livro
        return None

    def buscar_usuario_por_nome(self, nome):
        for usuario in self.usuarios:
            if usuario.nome.lower().strip() == nome.lower().strip():
                return usuario
        return None

    #def __init__(self):
     #   reserva_de_livros = deque()
      #  reserva_de_livros.append("Gabriel")
       # reserva_de_livros.append("Gustavo")
        #reserva_de_livros.append("Gabriela")
        #proximo_usuario = reserva_de_livros.popleft()
        #print("O próximo usuario a receber é: {proximo_usuario}")
            
                   
            


# Função principal com menu
def main():
    biblioteca = Biblioteca()
    devolucao = Devolucao(biblioteca)

    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Cadastrar Livro")
        print("2. Cadastrar Usuário")
        print("3. Emprestar Livro")
        print("4. Ver Histórico")
        print("5. Devolver Livro")
        print("6. Buscar Livro")
        print("7. Buscar Usuario")
        print("8. Sair")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            titulo = input("Digite o titulo do Livro: ")
            autor = input("Digite o nome do autor: ")
            isbn = input("Digite o isbn (APENAS 13 DIGITOS): ")
            faixa_etaria = input("Digite a faixa etaria da categoria do livro: ")
            quantidade = input("Digite a quantidade de exemplares:")
            data = input("Digite a data ")
            biblioteca.cadastrar_livro(titulo, autor, isbn, faixa_etaria, quantidade)
        elif opcao == "2":
            nome = input("Digite um nome:")
            idade = input("Digite uma idade:")
            documento = input("Digite seu CPF:")
            telefone = input("Digite seu número com DDD:")
            biblioteca.cadastrar_usuario(nome, idade, documento, telefone)
        elif opcao == "3":
            nome_usuario = input("Nome do usuário: ").strip()
            titulo_livro = input("Título do livro: ").strip()
            biblioteca.emprestar_livro(nome_usuario, titulo_livro)
        elif opcao == "4":
            biblioteca.mostrar_historico()
        elif opcao == "5":
            devolucao.devolver_livro()
        elif opcao == "6":
            titulo_livro = input("Digite o título do livro a buscar: ").strip()
            livro = biblioteca.buscar_livro_por_titulo(titulo_livro)
            if livro:
                print("\n--- Livro Encontrado ---")
                print(livro)
            else:
                print("Livro não encontrado")
        elif opcao == "7":
            biblioteca.buscar_usuario_por_nome()
        elif opcao == "8":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
