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

5. Configure seu arquivo configs.json (Com os dados da sua database) dentro da pasta database
  {
      "banco": {
          "user" : "seu_user",
          "pass" : "sua_senha",
          "dns" : "sua_dns_de_conexão",
          "instant_client" : "o_caminho_do_seu_instantclient"
      }
  }
 
6. Rode o servidor
  python app.py

## 📂 Estrutura do projeto

api-consultas-linx/
│── app.py              # Arquivo principal Flask
│── config.py           # Configuração de segurança (API Key)
│── routes/             # Rotas da API
│   ├── bp_usuarios.py
│   ├── bp_origens.py
│── database/           # Conexão com Oracle
│── .env.example        # Exemplo de variáveis de ambiente
│── requirements.txt    # Dependências do projeto

## 📜 Licença

Este projeto é de uso interno para consultas e testes.
Sinta-se livre para clonar e adaptar conforme necessário.