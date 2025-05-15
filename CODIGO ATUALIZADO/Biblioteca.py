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

        if not usuario_encontrado or not livro_encontrado:
            print("Usuario ou livro não encontrado")
            return   # Eu utilizei o return, pq caso tenha algum erro, ele já sai antecipadamente.
        
        if usuario_encontrado.idade < livro_encontrado.faixa_etaria:
            print(f"Usuario:{usuario_encontrado}, não tem idade suficiente para leitura do livro. (Idade permitida: {livro_encontrado.faixa_etaria}+ anos")
            return
        
        
        livro_encontrado.disponivel = False
        self.historico_emprestimos.append({
            "acao": "empréstimo",
            "livro": titulo_livro,
            "usuario": nome_usuario
        })
        print(f"Livro '{titulo_livro}' emprestado para {nome_usuario}!")
        






    def mostrar_historico(self):
        print("\n--- Histórico de Empréstimos ---")
        for registro in self.historico_emprestimos:
            print(f"{registro['acao'].upper()}: {registro['livro']} -> {registro['usuario']}")
    # No final do arquivo Biblioteca.py, adicione:



    def buscar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                return livro
        return None




    def buscar_usuario(self, nome):
        for usuario in self.usuarios:
            if usuario.nome.lower() == nome.lower():
                return usuario
        return None
            


def main():
    biblioteca = Biblioteca()
    
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Cadastrar Livro")
        print("2. Cadastrar Usuário")
        print("3. Emprestar Livro")
        print("4. Ver Histórico")
        print("5. Buscar Livro")
        print("6. Buscar Usuario")
        print("7. Sair")
        
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
            biblioteca.buscar_livro()
        elif opcao == "6":
            biblioteca.buscar_usuario()
        elif opcao == "7":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()














         
    # IMPLEMENTAR QUAIS OS LIVROS QUE O USUARIO PEGOU DE EMPRESTIMO
    # IMPLEMENTAR AS INFO DO USUARIO, AS QUE ESTÃO NO CADASTRO 
    #FUNÇOES QUE PODEM SER IMPLEMENTADAS: HISTORICO DE DEVOLUÇÃO
    #MODIFICAR A CLASSE LIVRO E ADICIONAR QUANTIDADE NO ATRIBUTO.






