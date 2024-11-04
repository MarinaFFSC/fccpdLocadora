# app/main.py

import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="db",
        user="user",
        password="pass",
        database="locadora"
    )

def inserir_filme():
    titulo = input("Digite o título do filme: ")
    ano = int(input("Digite o ano do filme: "))
    categoria_id = int(input("Digite o ID da categoria: "))
    
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO filme (titulo, ano, id_categoria) VALUES (%s, %s, %s)", (titulo, ano, categoria_id))
    conn.commit()
    cursor.close()
    conn.close()
    print("Filme inserido com sucesso.")

def listar_filmes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT filme.titulo, filme.ano, categoria.nome FROM filme JOIN categoria ON filme.id_categoria = categoria.id")
    filmes = cursor.fetchall()
    for titulo, ano, categoria in filmes:
        print(f"Titulo: {titulo}, Ano: {ano}, Categoria: {categoria}")
    cursor.close()
    conn.close()

def atualizar_filme():
    filme_id = int(input("Digite o ID do filme a ser atualizado: "))
    novo_titulo = input("Digite o novo título: ")
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE filme SET titulo = %s WHERE id = %s", (novo_titulo, filme_id))
    conn.commit()
    cursor.close()
    conn.close()
    print("Filme atualizado com sucesso.")

def excluir_filme():
    filme_id = int(input("Digite o ID do filme a ser excluído: "))
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM filme WHERE id = %s", (filme_id,))
    conn.commit()
    cursor.close()
    conn.close()
    print("Filme excluído com sucesso.")

def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Inserir Filme")
        print("2. Listar Filmes")
        print("3. Atualizar Filme")
        print("4. Excluir Filme")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            inserir_filme()
        elif opcao == "2":
            listar_filmes()
        elif opcao == "3":
            atualizar_filme()
        elif opcao == "4":
            excluir_filme()
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
