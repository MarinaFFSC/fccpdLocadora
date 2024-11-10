O projeto consiste em uma aplicação para gerenciamento de uma locadora de filmes utilizando Python, MySQL e contêineres Docker. A aplicação permite realizar operações CRUD e de clientes, incluindo cadastro, aluguel e devolução de filmes.

## Pré-requisitos

- Docker e Docker Compose instalados na máquina.
- Python.
- MySQL.

## Instalação e Configuração

1. **Clone o repositório:**
   ```bash
   git clone <url-do-repositório>
   cd <nome-do-repositório>
   ```

2. **Configuração dos contêineres:**
   - No diretório do projeto, execute o seguinte comando para inicializar os contêineres Docker (banco de dados e aplicação):
     ```bash
     docker-compose up --build
     ```
   - Isso irá construir e iniciar os serviços configurados em `docker-compose.yml`, incluindo o banco de dados MySQL e a aplicação Python.

3. **Verificação dos contêineres:**
   - Certifique-se de que os contêineres estão rodando corretamente com o comando:
     ```bash
     docker ps
     ```

## Estrutura do Projeto

```
fccpdLocadora/
├── app/
│   ├── Dockerfile            # Dockerfile para o contêiner da aplicação
│   ├── main.py               # Script principal da aplicação
│   └── requirements.txt      # Dependências da aplicação
├── db/
│   ├── Dockerfile            # Dockerfile para o contêiner do banco de dados
│   └── init.sql              # Script de inicialização do banco de dados
├── docker-compose.yml        # Configuração de serviços do Docker Compose
└── my.cnf                    # Arquivo de configuração do MySQL
```

### Operações

1. **Inserir Filme:**
   - Permite adicionar novos filmes ao banco de dados, especificando informações como ID, título, ano de lançamento, categoria, estoque, e descrição.

2. **Listar Filmes:**
   - Permite listar todos os filmes cadastrados ou buscar filmes por uma categoria específica.

3. **Atualizar Filme:**
   - Permite modificar informações de filmes existentes.

4. **Excluir Filme:**
   - Remove filmes do banco de dados.

### Operações de Cliente

1. **Cadastro e Login:**
   - Clientes podem se cadastrar fornecendo um login e senha.
   - O login permite acesso às funcionalidades disponíveis para clientes.

2. **Alugar Filme:**
   - Clientes podem visualizar a lista de filmes disponíveis e realizar o aluguel de um filme, desde que haja estoque disponível.

3. **Devolver Filme:**
   - Permite a devolução de filmes alugados.

4. **Gerenciamento de Cadastro:**
   - Clientes podem visualizar e excluir seus cadastros, desde que não possuam aluguéis pendentes.

## Banco de Dados

O banco de dados `locadora` é configurado com as seguintes tabelas principais:

- **Categorias:** Contém as categorias de filmes.
- **Filmes:** Armazena informações dos filmes disponíveis na locadora, incluindo estoque.
- **Clientes:** Gerencia informações de clientes, como login e senha.
- **Aluguel:** Registra informações de aluguéis realizados pelos clientes.

### Script de Inicialização

O script `init.sql` é executado ao inicializar o banco de dados e realiza as seguintes operações:

- Criação das tabelas necessárias.
- Inserção de registros iniciais nas tabelas `Clientes`, `Categorias` e `Filmes`.

## Ferramentas Utilizadas

- **Python:** Linguagem da aplicação.
- **MySQL:** Banco de dados utilizado para armazenar as informações.
- **Docker e Docker Compose:** Usados para gerenciar e executar os contêineres de banco de dados e aplicação.
- **mysql-connector-python:** Biblioteca para comunicação com o banco de dados MySQL a partir da aplicação Python.
