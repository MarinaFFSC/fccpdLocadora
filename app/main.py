# app/main.py
import mysql.connector
import time
import os


def bordered(text):
    lines = text.splitlines()
    width = max(len(s) for s in lines)
    res = ['┌' + '─' * width + '┐']
    for s in lines:
        res.append('│' + (s + ' ' * width)[:width] + '│')
    res.append('└' + '─' * width + '┘')
    return '\n'.join(res)


def conectar():
    try:
        conn = mysql.connector.connect(
            host="db",
            user="user",
            password="pass",
            database="locadora",
            port=3306
        )
        if conn.is_connected():
            return conn
    except mysql.connector.Error as err:
        print(f"Erro de conexao: {err}")
        return None



#++++++++++++++++++++++   ADMINISTRADOR   +++++++++++++++++++++++++++++++++++

# Inserir filme na Tabela.
def inserir_filme():
    conn = conectar()
    cursor = conn.cursor()

    print("--x-- [INSERCAO FILME] --x--")
    print("ID -> TITULO -> ANO -> ESTOQUE -> CATEGORIA -> DESCRICAO\n")
    f_id = input("ID: ")
    f_nome = input("Titulo: ")
    f_ano = int(input("Lancamento (Ano): "))
    f_estoq = int(input("Estoque:"))
    
    # listando as categorias possiveis.
    cursor.execute("SELECT * FROM Categorias")
    categorias = cursor.fetchall()
    print("Categorias Possiveis:")
    for categoria in categorias:
        print(categoria)
    f_categ_id = int(input("Categoria (ID): "))
    f_desc = input("Descricao do Filme (500 carateres):\n\t>")

    conn.commit()
    cursor.close()
    

    # adicionar o filme ao Banco de Dados
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO Filmes(filme_id, filme_nome, filme_ano, filme_descricao, filme_estoque, filme_categoria_id) VALUES(%s, %s, %s, %s, %s, %s)",
        (f_id, f_nome, f_ano, f_desc, f_estoq, f_categ_id))
        conn.commit()  # Confirma a transação
        print("\nFilme inserido com sucesso.\n")
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
    finally:
        cursor.close()

    conn.close()


def listar_filmes_por_categoria(categoria_id):
    conn = conectar()
    cursor = conn.cursor()

    # Consulta para selecionar filmes de uma categoria específica
    query = """
    SELECT Filmes.filme_id, Filmes.filme_nome, Filmes.filme_ano, Filmes.filme_descricao, Filmes.filme_estoque, 
           Filmes.filme_alugados, Categorias.categoria_nome
    FROM Filmes
    JOIN Categorias ON Filmes.filme_categoria_id = Categorias.categoria_id
    WHERE Filmes.filme_categoria_id = %s
    """
    
    cursor.execute(query, (categoria_id,))
    filmes = cursor.fetchall()

    for filme in filmes:
        filme_id, filme_nome, filme_ano, filme_descricao, filme_estoque, filme_alugados, categoria_nome = filme
        print(f"ID: {filme_id} | Nome: {filme_nome} | Ano: {filme_ano} | Estoque: {filme_estoque}")
        print(f"Descrição: {bordered(filme_descricao)}")
        print(f"Categoria: {categoria_nome}\n")

    cursor.close()
    conn.close()



def listar_filmes():
    
    
    print("[ LOCADORA ]\n")
    print("[1] LISTAR TODOS")
    print("[2] LISTAR POR CATEGORIA")
    opcao = int(input(">>>  "))

    if opcao == 1:
        conn = conectar()
        cursor = conn.cursor()

        query = """
        SELECT Filmes.filme_id, Filmes.filme_nome, Filmes.filme_ano, Filmes.filme_descricao,
            Filmes.filme_estoque, Filmes.filme_alugados, Categorias.categoria_nome
        FROM Filmes
        JOIN Categorias ON Filmes.filme_categoria_id = Categorias.categoria_id
        """
        cursor.execute(query)
        filmes = cursor.fetchall()
        
        for filme in filmes:
            filme_id, filme_nome, filme_ano, filme_descricao, filme_estoque, filme_alugados, categoria_nome = filme
            
            print("-" * 50)
            print("ID | TITULO | LANCAMENTO | CATEGORIA")
            print(f"{filme_id} | {filme_nome} | {filme_ano} | {categoria_nome}")
            print("\n| DESCRICAO |")
            print(bordered(filme_descricao))
            print(f"\n\t\t\tDisponiveis: {filme_estoque}")
            print("-" * 50)
        
        cursor.close()
        conn.close()


    if opcao == 2:
        print(
        """\n\n
        [1] Acao
        [2] Romance
        [3] Terror
        [4] Comedia
        [5] Ficcao
        [6] Drama
        [7] Animacao
        """
        )
        escolha = int(input(">>>  "))

        listar_filmes_por_categoria(escolha)
                

def listagem_rapida():
    conn = conectar()
    cursor = conn.cursor()

    query = """
    SELECT Filmes.filme_id, Filmes.filme_nome, Filmes.filme_ano FROM Filmes"""
    cursor.execute(query)
    filmes = cursor.fetchall()
    
    print("LISTA DE FILMES\n")
    print("  ID  |  NOME  |  ANO")
    for filme in filmes:
        filme_id, filme_nome, filme_ano = filme
        print(f"{filme_id}  |  {filme_nome}  |  {filme_ano}")

    cursor.close()
    conn.close()


# Atualizar algum parametro do filme da Tabela.
def atualizar_filme():
    conn = conectar()
    cursor = conn.cursor()
    
    listagem_rapida()

    while True:
        id_atualizar = int(input("ID do filme para ser atualizado: "))
        
        cursor.execute("SELECT * FROM Filmes WHERE Filme_id = %s", (id_atualizar,))
        filme_att = cursor.fetchone()
        
        if filme_att:
            print("-" * 50)
            print(f"""ID: {filme_att[0]}\n
            TITULO: {filme_att[1]}\n
            ANO: {filme_att[2]}\n
            CATEGORIA: {filme_att[6]}\n""")
            print("| DESCRICAO |")
            print(bordered(filme_att[3]))
            print("-" * 50)
            
            confirm = input("Deseja atualizar esse filme (s/n) ? >>>  ").lower()
            
            if confirm == 'n':
                print("\nOperacao cancelada.\n")
                break
            
            novo_nome = input("Novo Titulo:  ") or filme_att[1]
            novo_ano = int(input("Novo Ano:  ")) or filme_att[2]

            cursor.execute("SELECT * FROM Categorias")
            categorias = cursor.fetchall()
            print("Categorias Possiveis:")
            for categoria in categorias:
                print(categoria)

            nova_categoria_id = int(input("Nova Categoria (ID):  ")) or filme_att[6]
            nova_descricao = input("Nova Descricao: ") or filme_att[3]

            
            cursor.execute(
                """
                UPDATE Filmes
                SET filme_nome=%s, filme_ano=%s, filme_descricao=%s,        filme_categoria_id=%s
                WHERE filme_id = %s
                """,
                (novo_nome, novo_ano, nova_descricao, nova_categoria_id, id_atualizar)
            )
            conn.commit()
            print("\n\t!!! Filme Atualizado com Sucesso !!!\n")
            

            continuar = input("Deseja continuar a atualizar (s/n)? >>>  ").lower()
            if continuar == 'n':
                conn.close()
                break
    
    cursor.close()
    conn.close()


# excluir filme da tabela.
def excluir_filme():
    conn = conectar()
    cursor = conn.cursor()
    
    listagem_rapida()
        
    while True:
        id_excluir = int(input("ID do filme para ser atualizado: "))
        
        cursor.execute("SELECT * FROM Filmes WHERE Filme_id = %s", (id_excluir,))
        filme_ex = cursor.fetchone()
        
        if filme_ex:
            print("-" * 50)
            print(f"""ID: {filme_ex[0]}\n
            TITULO: {filme_ex[1]}\n
            ANO: {filme_ex[2]}\n
            CATEGORIA: {filme_ex[6]}\n""")
            print("| DESCRICAO |")
            print(bordered(filme_ex[3]))
            print("-" * 50)
            
            confirm = input("Deseja atualizar esse filme (s/n) ? >>>  ").lower()
            
            if confirm == 'n':
                print("\nOperacao cancelada.\n")
                break
                
            cursor.execute("DELETE FROM Filmes WHERE filme_id = %s", (id_excluir,))
            conn.commit()


            print("\n\t!!! Filme Deletado com Sucesso !!!\n")
            
            continuar = input("Deseja deletar mais algum (s/n)? >>>  ").lower()
            if continuar == 'n':
                conn.close()
                break


# ++++++++++++++++++++++++++   CLIENTE   +++++++++++++++++++++++++++++++++++++

# Cliente: alugar filme
def alugar_filme(login):

    listagem_rapida()
    
    while True:
        conn = conectar()
        cursor = conn.cursor()
    
        id_alugar = input("Digite O ID do Filme >>> ")
        
        cursor.execute("SELECT * FROM Filmes WHERE Filme_id = %s", (id_alugar,))
        filme_ex = cursor.fetchone()
        
        if filme_ex:
            print("-" * 50)
            print(f"""ID: {filme_ex[0]}\n
            TITULO: {filme_ex[1]}\n
            ANO: {filme_ex[2]}\n
            CATEGORIA: {filme_ex[6]}\n""")
            print("| DESCRICAO |")
            print(bordered(filme_ex[3]))
            print(f"\nESTOQUE: {filme_ex[4]}")
            print("-" * 50)
            
            confirm = input("Deseja alugar esse filme (s/n) ? >>>  ").lower()
            
            if confirm == 'n':
                print("\nOperacao cancelada.\n")
                break
            
            estoque = filme_ex[4]
            if estoque <= 0:
                print(f"\nLamentamos, nao temos {filme_ex[1]} no momento.\n")
                break
            
            
            cursor.execute("""
            SELECT * FROM Clientes WHERE cliente_login = %s
            """, (login, ))
            cliente = cursor.fetchone()
            
            
            cursor.execute("""
            INSERT INTO Aluguel(aluguel_filme_id, aluguel_cliente_nome)
            VALUES(%s, %s)
            """, (filme_ex[0], cliente[0]))
            aluguel_id = cursor.lastrowid
            
            
            cursor.execute("""
            UPDATE Clientes SET cliente_alugado_id = %s WHERE cliente_login = %s
            """, (aluguel_id, login))
            
            
            cursor.execute("""
            UPDATE Filmes SET filme_estoque = filme_estoque - 1 WHERE filme_id = %s
            """, (filme_ex[0],))
            
            conn.commit()
            cursor.close()
            conn.close()
            print("\nFilme Alugado com sucesso!\n")
            break
            
        else:
            print("\nFilme nao encontrado.\n")
            break


# veiricar se o cliente já possui um aluguel na conta.
def verificar_alugado(login):
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute("""
    SELECT Filmes.filme_id, Filmes.filme_nome, Filme_ano, Filmes.filme_descricao,  Categorias.categoria_nome
    FROM Clientes
    JOIN Aluguel ON Clientes.cliente_alugado_id = Aluguel.aluguel_id
    JOIN Filmes ON Aluguel.aluguel_filme_id = Filmes.filme_id
    JOIN Categorias ON Filmes.filme_categoria_id = Categorias.categoria_id
    WHERE Clientes.cliente_login = %s
    """, (login, ))

    filme = cursor.fetchone()

    if filme:
        print("-" * 50)
        print(f"""ID: {filme[0]}\n
        TITULO: {filme[1]}\n
        ANO: {filme[2]}\n
        CATEGORIA: {filme[4]}\n""")
        print("| DESCRICAO |")
        print(bordered(filme[3]))
        print("-" * 50)
        return 1

    else:
        print("\tNenhum filme alugado.\n")
        return 0
    


def devolver_filme(login):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT Filmes.filme_id, Filmes.filme_nome, Filmes.filme_estoque, Clientes.cliente_alugado_id
    FROM Clientes
    JOIN Aluguel ON Clientes.cliente_alugado_id = Aluguel.aluguel_id
    JOIN Filmes ON Aluguel.aluguel_filme_id = Filmes.filme_id
    WHERE Clientes.cliente_login = %s
    """, (login, ))
    
    filme = cursor.fetchone()
    
    
    filme_id = filme[0]
    filme_nome = filme[1]
    estoque_atual = filme[2]
    aluguel_id = filme[3]
    
    confirm = input(f"Deseja devolver {filme_id} | {filme_nome} (s/n) ?").lower()
    if confirm == 's':
        cursor.execute("""
        UPDATE Filmes SET filme_estoque = filme_estoque + 1 WHERE filme_id = %s
        """, (filme_id, ))
        
        
        cursor.execute("""
        UPDATE Clientes SET cliente_alugado_id = NULL WHERE cliente_login = %s
        """, (login, ))
        
        
        cursor.execute("""
        DELETE FROM Aluguel WHERE aluguel_id = %s
        """, (aluguel_id, ))
        
        
        conn.commit()
        
        print("\nFilme devolvido com sucesso!\n")
        
    if confirm == 'n':    
        print("\nOperacao cancelada.\n")
    
    cursor.close()
    conn.close()


# verificar se login existe, se nao cadastrar.
def verificar_login(login, senha):
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute("SELECT cliente_login FROM Clientes WHERE cliente_login = %s", (login, ))
    cliente = cursor.fetchone()
    
    if cliente:
        cursor.execute("SELECT cliente_senha FROM Clientes WHERE cliente_login = %s", (login,))
        senha_salva = cursor.fetchone()
        
        if senha_salva and senha_salva[0] == senha:
            print(f"\n\t!!! Login bem-sucedido !!!\n")
            
            if login == "admin":
                submenu_admin()
            else:
                submenu_cliente(login)
        else:
            print("Login e/ou senha invalidos.\n")
    
    
    if not cliente:
        print("Cadastro nao encontrado.")
        cadastro = input("Deseja criar um novo (s/n) ? >>> ").lower()
        
        if cadastro == 'n':
            print("\nOperacao cancelada.\n")
            
        if cadastro == 's':    
            cadastro_login = input("Digite seu login: ")
            cadastro_senha = input("Digite sua senha: ")
            cadastro_nome = input("Digite seu nome: ")
            
            cursor.execute(
            """INSERT INTO Clientes (cliente_nome, cliente_login, cliente_senha)
            VALUES (%s, %s, %s)""",
            (cadastro_nome, cadastro_login, cadastro_senha)
            )
            conn.commit()
            print("Cadastrado realizado com sucesso!")

    cursor.close()
    conn.close()


def verificar_cadastro(login):
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT cliente_nome, cliente_login, cliente_senha
        FROM Clientes
        WHERE cliente_login = %s
    """,(login, )) 
    cliente = cursor.fetchone()

    cliente_nome, cliente_login, cliente_senha = cliente
    print("\n[CADASTRO]\n")
    print(f" Nome: {cliente_nome}")
    print(f"Login: {cliente_login}")
    print(f"Senha: {cliente_senha}\n")
    
    cursor.close()
    conn.close()


def excluir_cadastro(login):
    with conectar() as conn:
        with conn.cursor() as cursor:
    
            verificar = verificar_alugado(login)
            
            if verificar:
                print("\n\t!!! Voce possui um filme alugado, devolva-o antes de prosseguir. !!!\n")
            
            if not verificar:
                confirm = input("!!! TEM CERTEZA QUE DESEJA EXCLUIR O CADASTRO (s/n) ?").lower()
                
                if confirm == 's':
                    cursor.execute("DELETE FROM Clientes WHERE cliente_login = %s", (login, ))
                    conn.commit()
                    
                    print("\n\tExcluido com sucesso, ate a proxima\n")
                    return 1
            
                else:
                    print("\n\tOperacao cancelada.\n")
                    return 0

    
# +++++++++++++++++++++++++++++++   MENU   ++++++++++++++++++++++++++++++++++++

def submenu_admin():
    while True:
        print("[ ADMIN ]")
        print(" ┗ [1] Inserir\n",
            "┗ [2] Listar\n",
            "┗ [3] Atualizar\n",
            "┗ [4] Excluir\n",
            "┗ [5] Voltar")
        
        opcao = int(input(">>> "))

        if opcao == 1:
            inserir_filme()
        elif opcao == 2:
            listar_filmes()
        elif opcao == 3:
            atualizar_filme()
        elif opcao == 4:
            excluir_filme()
        elif opcao == 5:
            return
        else:
            print("\n!!! Opção inválida. !!!\n")



def submenu_cliente(login):
    conn = conectar()
    cursor = conn.cursor()
    
    
    cursor.execute("SELECT cliente_nome FROM Clientes WHERE cliente_login = %s", (login,))
    nome = cursor.fetchone()
    

    while True:
        print(f"BEM-VINDO(A), > {nome[0]} <")

        verificar = verificar_alugado(login)

        print(" ┗ [1] Listar Filmes\n",
            "┗ [2] Alugar / Devolver\n",
            "┗ [3] Verificar Cadastro\n",
            "┗ [4] Excluir Cadastro\n",
            "┗ [5] Sair")
        opcao = int(input(">>> "))
        
        if opcao == 1:
            listar_filmes()
        
        elif opcao == 2:

            print("[1] Alugar")
            print("[2] Devolver")
            escolha = int(input(">>>  "))
            
            if escolha == 1 and not verificar:
                alugar_filme(login)
            elif escolha == 2 and verificar:
                devolver_filme(login)
            else:
                print("\n\tOperacao invalida\n")

        elif opcao == 3:
            verificar_cadastro(login)
            
        elif opcao == 4:
            excluir = excluir_cadastro(login)
            
            if excluir:
                break
            
        elif opcao == 5:
            return
            
        else:
            print("\n!!! Opcao Invalida. !!!\n")

# impressao do menu.
def menu():
    time.sleep(10) # Garantir que so ira rodar apos o DB.

    # checagem se foi possivel conectar.
    conn = None;
    while not conn:
        print("\nTESTANDO CONEXAO COM A BASE DE DADOS. . .")
        conn = conectar()
        if not conn:
            time.sleep(5)
    conn.close()
    print("\t!!! CONNECTADO(A) AO BD !!!\n")

    

    while True:
        #os.system('clear')
        login = input("LOGIN: ")
        senha = input("SENHA: ")
        
        verificar_login(login, senha)

if __name__ == "__main__":
    menu()
