import Livro
import Usuario

class Biblioteca:
    def __init__(self):
        self.livros = []  # Lista para armazenar livros 
        self.usuarios = []  # Lista para usuários
        self.historico_emprestimos = []  # Pilha 

    def cadastrar_livro(self):
        print("\n--- Cadastro de Livro ---")
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        isbn = input("Digite o ISBN (13 dígitos): ")
        faixa_etaria = int(input("Digite a faixa etária mínima: "))
        
        try:
            livro = Livro.Livro(titulo, autor, isbn, faixa_etaria)
            self.livros.append(livro)
            print(f"Livro '{titulo}' cadastrado com sucesso!")
        except ValueError as e:
            print(f"Erro: {e}")

    def cadastrar_usuario(self):
        print("\n--- Cadastro de Usuário ---")
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        documento = input("Documento (CPF/RG): ")
        telefone = input("Telefone: ")
        
        usuario = Usuario.Usuario(nome, idade, documento, telefone)
        self.usuarios.append(usuario)
        print(f"Usuário '{nome}' cadastrado com sucesso!")

    def emprestar_livro(self):
        print("\n--- Empréstimo de Livro ---")
        nome_usuario = input("Nome do usuário: ")
        titulo_livro = input("Título do livro: ")

        # Busca usuário e livro
        usuario_encontrado = None
        livro_encontrado = None

        for usuario in self.usuarios:
            if usuario.nome == nome_usuario:
                usuario_encontrado = usuario
                break

        for livro in self.livros:
            if livro.titulo == titulo_livro:
                livro_encontrado = livro
                break

        if usuario_encontrado and livro_encontrado:
            if livro_encontrado.disponivel:
                livro_encontrado.disponivel = False
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
            print(f"{registro['acao'].upper()}: {registro['livro']} -> {registro['usuario']}")
    # No final do arquivo Biblioteca.py, adicione:

def main():
    biblioteca = Biblioteca()
    
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Cadastrar Livro")
        print("2. Cadastrar Usuário")
        print("3. Emprestar Livro")
        print("4. Ver Histórico")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            biblioteca.cadastrar_livro()
        elif opcao == "2":
            biblioteca.cadastrar_usuario()
        elif opcao == "3":
            biblioteca.emprestar_livro()
        elif opcao == "4":
            biblioteca.mostrar_historico()
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
