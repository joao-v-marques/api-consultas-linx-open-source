## ⚠️ Atenção: Versão Open Source

Este repositório é a versão **open source** da API, destinada a estudo e portfólio.  
Para utilizá-la em um ambiente de **produção real**, é necessário fazer ajustes importantes:

## 1. Queries (SELECTs)
- As queries deste repositório usam **tabelas e colunas fictícias** para manter o projeto seguro.  
- Substitua pelos nomes de tabelas e colunas reais do seu banco de dados de produção.

## 2. Configurações (`config.py`)
- Ajuste parâmetros de segurança, como **SECRET_KEY** e outras configurações específicas do ambiente.  
- Verifique se a lógica de autenticação, API Key ou JWT está configurada conforme a política de segurança da sua empresa.

## 3. Variáveis de ambiente (`.env`)
- Crie ou ajuste o arquivo `.env` com suas **credenciais reais**, como usuário e senha do banco de dados, API Key, endpoints e outros valores sensíveis.  
- **Nunca** comite `.env` no repositório público; utilize `.env.example` para ilustrar a estrutura necessária.

## 4. Boas práticas
- Teste a API em um ambiente de desenvolvimento antes de migrar para produção.  
- Garanta que as queries estão parametrizadas para evitar **SQL Injection**.  
- Mantenha os logs e erros seguros, sem expor dados sensíveis.

---

💡 Seguindo essas instruções, você pode migrar a versão open source para produção de forma segura e funcional, mantendo boas práticas de desenvolvimento e segurança.

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

api-consultas-open-source/
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