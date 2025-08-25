# 🧠 API de Diagnóstico de Escoliose e Gerenciamento Médico

## 📌 Visão Geral

Esta API, desenvolvida em **Python**, serve como backend para o sistema de **gerenciamento de pacientes e médicos integrado a IA**.

Ela fornece endpoints REST para cadastro e gerenciamento de informações clínicas, além de uma rota dedicada para análise de imagens de **raio-x da coluna**, retornando o diagnóstico automático de **escoliose**.

## 🛠️ Tecnologias Utilizadas

- [Python 3.10](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [SQLite](https://sqlite.org/)
- [Pydantic](https://docs.pydantic.dev/)

## 📡 Estrutura de Rotas

### 🔐 Autenticação

| Método | Endpoint | Descrição | 
| --- | --- | --- | 
| `GET`| `/auth/` | Lista todos os registros que possuem autenticação no sistema (sem a senha) |
| `POST`| `/auth/login` | Autentica paciente/médico/administrador e retorna se autenticado ou não |
| `POST`| `/auth/register` | Cadastra um novo paciente/médico no sistema |

### 👤 Usuários

| Método | Endpoint | Descrição | 
| --- | --- | --- | 
| `GET` | `/users/` | Lista todos os usuários do sistema |
| `GET` | `/users/{user_id}` | Pesquisa um usuário pelo ID |
| `POST` | `/users/` | Registra um novo usuário no sistema |
| `PUT` | `/users/` | Atualiza um usuários já existente no sistema |
| `DELETE` | `/users/{user_id}` | Exclui um usuário existente no sistema |
| `GET` | `/users/by_role/{role}` | Lista todos os usuários do sistema pelo tipo |

### 📂 Exames (Raio-X)

| Método | Endpoint | Descrição | 
| --- | --- | --- | 
| `GET` | `/exams/` | Lista todos os exames do sistema |
| `GET` | `/exams/by_patient/{patient_id}` | Lista todos os exames do sistema por paciente |
| `GET` | `/exams/by_doctor/{doctor_id}` | Lista todos os exames do sistema por médico |
| `GET` | `/exams/with_photo` | Lista todos os exames do sistema que possuem foto |
| `POST` | `/exams/` | Registra um novo exame no sistema |

## ⚙️ Instalação e Execução

### Pré-requisitos

- Python 3.10+
- SQLite (por enquanto para desenvolvimento)

### Passos

```bash
  # Clone o repositório
  git clone https://github.com/enzolozano/ortho-ai-api.git

  # Acesse o diretório
  cd app

  # Instale as dependências
  pip install -r requirements.txt

  # Execute a API
  uvicorn main:app - reload
```

## 🔒 Segurança

- Criptografia de senhas com **bcrypt**
- Regras de acesso baseadas em perfil (admin / médico / paciente futuro)
