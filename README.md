# Fast Car API 🚗

**Versão:** 0.1.0

**Autor:** AdonesMelo (adones.n.m@outlook.com)

## Visão Geral

**Fast Car API** é uma API moderna desenvolvida com o framework **FastAPI**. O objetivo principal deste projeto é fornecer uma interface de comunicação rápida e eficiente para o gerenciamento de carros (operações de CRUD - Criar, Ler, Atualizar e Deletar).

## 📌 Status do Projeto

🚧 **Em desenvolvimento** - O projeto atualmente encontra-se na versão inicial (`0.1.0`) e está recebendo novas implementações e refinamentos.

## 🛠️ Tecnologias Utilizadas

* **Web Framework:** FastAPI

* **Validação de Dados e Schemas:** Pydantic

* **ORM e Banco de Dados:** SQLAlchemy e SQLite

* **Migração de Banco de Dados:** Alembic

* **Linting & Formatação:** Ruff

* **Task Runner:** Taskipy

* **Documentação:** MkDocs

## 📂 Estrutura do Projeto

Abaixo está a representação exata da organização dos arquivos e diretórios principais do projeto:

```text
Fast_Car_API/
├── docs/               # Documentação do projeto (MkDocs)
├── fast_car_api/       # Código fonte principal da API
│   ├── __init__.py
│   ├── app.py          # Ponto de entrada da aplicação FastAPI
│   ├── database.py     # Configuração de conexão com o banco de dados
│   ├── models.py       # Modelos do SQLAlchemy (Tabelas do banco)
│   ├── routers.py      # Definição das rotas/endpoints da API
│   └── schemas.py      # Schemas do Pydantic (Validação de entrada/saída)
├── migrations/         # Diretório contendo as migrações geradas pelo Alembic
├── tests/              # Testes automatizados do projeton
├── .gitignore          # Arquivos e pastas ignorados pelo Git
├── alembic.ini         # Arquivo de configuração do Alembic
├── cars.db             # Banco de dados SQLite local
├── mkdocs.yml          # Arquivo de configuração do MkDocs
├── pyproject.toml      # Configuração do projeto (Ruff, Taskipy, etc.)
└── requirements.txt    # Lista de dependências do Python
```

## 🚀 Como Rodar o Projeto

Siga as instruções abaixo para preparar o ambiente e rodar a API localmente na sua máquina:

**1. Criar e ativar o ambiente virtual**

```bash
python -m venv venv

# Para ativar no Linux ou macOS:
source venv/bin/activate

# Para ativar no Windows:
.\venv\Scripts\activate
```

**2. Instalar as dependências**
Instale as dependências usando o arquivo `requirements.txt` ou o `pyproject.toml` (neste exemplo usando o pip padrão):

```bash
pip install -r requirements.txt
# ou caso esteja instalando via pyproject.toml: pip install -e .
```

**3. Rodar as migrações do banco de dados (Alembic)**
Para criar as tabelas no SQLite, execute:

```bash
alembic upgrade head
```

**4. Rodar o servidor FastAPI**
Utilize o comando configurado no Taskipy para iniciar a aplicação:

```bash
task run
```

*(A API estará disponível em `http://127.0.0.1:8000`)*

## ⌨️ Comandos de Desenvolvimento (Taskipy)

O projeto utiliza o `taskipy` para facilitar a execução de scripts e ferramentas de qualidade de código.

| Comando | Descrição | Comando Original executado | 
| ----- | ----- | ----- | 
| `task run` | Inicia o servidor local de desenvolvimento. | `fastapi dev fast_car_api/app.py` | 
| `task lint` | Verifica problemas de formatação e padrões no código. | `ruff check` | 
| `task lint_fix` | Corrige automaticamente problemas encontrados pelo linter. | `ruff check --fix` | 
| `task format` | Formata o código fonte do projeto. | `ruff format` | 
| `task docs` | Inicia o servidor local da documentação MkDocs. | `mkdocs serve -a 127.0.0.1:8001` | 

## 📡 Documentação da API (Endpoints)

A API possui um roteador principal prefixado com `/api/v1/cars`. A documentação interativa (Swagger UI) pode ser acessada em `/docs` após iniciar o servidor. Abaixo estão os detalhes das rotas disponíveis:

### `POST /api/v1/cars/`

* **Descrição:** Cria um novo carro no banco de dados.

* **Corpo da Requisição:** Objeto `CarSchema`

* **Retorno de Sucesso:** `CarPublic`

* **Status Code:** `201 Created`

### `GET /api/v1/cars/`

* **Descrição:** Busca uma lista de todos os carros cadastrados com suporte a paginação.

* **Parâmetros de Query:**

  * `offset` (int, padrão: `0`)

  * `limit` (int, padrão: `100`)

* **Retorno de Sucesso:** Objeto contendo uma lista de carros (`CarList`)

* **Status Code:** `200 OK`

### `GET /api/v1/cars/{car_id}`

* **Descrição:** Busca os detalhes de um carro específico através do seu ID.

* **Parâmetros de Path:** `car_id` (int)

* **Retorno de Sucesso:** `CarPublic`

* **Erros:** `404 Not Found` (se o carro não existir)

* **Status Code:** `200 OK`

### `PUT /api/v1/cars/{car_id}`

* **Descrição:** Atualiza integralmente os dados de um carro existente.

* **Parâmetros de Path:** `car_id` (int)

* **Corpo da Requisição:** Objeto `CarSchema`

* **Retorno de Sucesso:** `CarPublic` (dados do carro atualizado)

* **Erros:** `404 Not Found` (se o carro não existir)

* **Status Code:** `201 Created`

### `PATCH /api/v1/cars/{car_id}`

* **Descrição:** Atualiza parcialmente os dados de um carro (apenas os campos enviados).

* **Parâmetros de Path:** `car_id` (int)

* **Corpo da Requisição:** Objeto `CarPartialUpdate`

* **Retorno de Sucesso:** `CarPublic` (dados do carro atualizado)

* **Erros:** `404 Not Found` (se o carro não existir)

* **Status Code:** `200 OK`

### `DELETE /api/v1/cars/{car_id}`

* **Descrição:** Exclui um carro do sistema.

* **Parâmetros de Path:** `car_id` (int)

* **Retorno de Sucesso:** Vazio (No Content)

* **Erros:** `404 Not Found` (se o carro não existir)

* **Status Code:** `204 No Content`

## ⚙️ Configurações do Linter (Ruff)

O projeto mantém um alto padrão de código através do `Ruff` com as seguintes diretrizes:

* **Tamanho máximo da linha:** 79 caracteres.

* **Aspas:** Simples (`'single'`).

* **Regras Habilitadas:** Padrões Isort (`I`), Pyflakes (`F`), pycodestyle (`E`, `W`), Pylint (`PL`) e flake8-pytest-style (`PT`).
