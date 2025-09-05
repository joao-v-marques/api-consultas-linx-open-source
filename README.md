# API Consultas Linx

API desenvolvida em **Python (Flask)** para consulta de dados no banco Oracle.  
O projeto foi criado com foco em segurança, utilizando **API Key** e **parametrização de queries** para evitar SQL Injection.

---

## 🚀 Funcionalidades

- Consultar todos os usuários (`/usuarios`)
- Consultar um usuário específico (`/usuarios/<codigo_usuario>`)
- Consultar todas as origens (`/origens`)
- Consultar uma origem específica (`/origens/<codigo_origem>`)
- Consultar origem com filtros de **empresa** e **revenda** (`/origens/<codigo_origem>/filtros`)

---

## 🔒 Segurança

- Autenticação via **API Key** no header (`x-api-key`)
- Queries sempre com parâmetros nomeados para evitar SQL Injection  

Exemplo de requisição utilizando **Postman**:

http
GET http://localhost:5000/usuarios
Headers:
  x-api-key: SUA_CHAVE_API

## 🛠️ Tecnologias
  - Python 3
  - Flask
  - oracledb
  - (para conexão Oracle)
  - python-dotenv
  - (para variáveis de ambiente)

## 📦 Como rodar o projeto

1. Clone o repositório
  git clone https://github.com/joao-v-marques/api-consultas-linx.git
  cd api-consultas-linx

2. Crie e ative o ambiente virtual
  python -m venv .venv
  .venv\Scripts\activate   # Windows
  source .venv/bin/activate # Linux/Mac

3. Instale as dependencias
  pip install -r requirements.txt

4. Configure o arquivo .env na raiz do projeto
  API_KEY=sua_chave_api
  SECRET_KEY=sua_secret_key