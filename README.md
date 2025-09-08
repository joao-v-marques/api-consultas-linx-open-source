# 🔍 API de Consultas Linx (Open Source)

![Python](https://img.shields.io/badge/python-3.11-blue?logo=python)
![Flask](https://img.shields.io/badge/flask-2.3-red?logo=flask)
![OracleDB](https://img.shields.io/badge/oracle-db-orange?logo=oracle)
![License](https://img.shields.io/badge/license-MIT-green)

Versão **open source** de uma API de consultas desenvolvida em **Python + Flask**, conectando-se ao **OracleDB**.  
Esta versão é destinada a estudo, portfólio e aprendizado de boas práticas em APIs seguras.

> ⚠️ **Atenção:** As queries neste repositório usam tabelas e colunas fictícias. Para uso em produção, substitua pelos dados reais e configure variáveis de ambiente corretamente.

---

## 🚀 Funcionalidades

- 🔹 Consulta de usuários e origens via API  
- 🔹 Autenticação simples via **API Key**  
- 🔹 Estrutura preparada para integração com banco Oracle  
- 🔹 Exemplo seguro de parametrização de queries  
- 🔹 Documentação clara para estudo e adaptação  

---

🛠 Tecnologias utilizadas

  - Backend: Python 3, Flask
  - Banco de Dados: OracleDB (via oracledb)
  - Variáveis de ambiente: python-dotenv
  - Segurança: API Key para autenticação

## 📦 Como rodar o projeto

1. Clone o repositório
  ```bash
  git clone https://github.com/joao-v-marques/api-consultas-linx.git
  cd api-consultas-linx

2. Crie e ative o ambiente virtual
  ```bash
  python -m venv .venv
  .venv\Scripts\activate   # Windows
  source .venv/bin/activate # Linux/Mac

3. Instale as dependencias
  ```bash
  pip install -r requirements.txt

4. Configure o arquivo .env na raiz do projeto
  ```bash
  API_KEY=sua_chave_api
  SECRET_KEY=sua_secret_key

5. Configure seu arquivo configs.json (Com os dados da sua database) dentro da pasta database
  ```bash
  {
      "banco": {
          "user" : "seu_user",
          "pass" : "sua_senha",
          "dns" : "sua_dns_de_conexão",
          "instant_client" : "o_caminho_do_seu_instantclient"
      }
  }
 
6. Rode o servidor
  ```bash
  python app.py

## 📂 Estrutura do projeto

api-consultas-open-source/
  ```bash
  ├── app.py # Arquivo principal Flask
  ├── config.py # Configuração de segurança (API Key)
  ├── routes/ # Rotas da API
  │ ├── bp_usuarios.py
  │ └── bp_origens.py
  ├── database/ # Conexão com Oracle
  │ └── configs.json # Configurações do banco
  ├── .env.example # Exemplo de variáveis de ambiente
  └── requirements.txt # Dependências do projeto

## 📜 Licença

Este projeto é de uso interno para consultas e testes.
A versão Open Source é livre para ser clonada e adaptada conforme o necessário.