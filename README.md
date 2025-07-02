# TripLogs Backend

Uma API REST para registro e gerenciamento de viagens, desenvolvida na disciplina **Fundamentos de DevOps** no curso de **Bacharelado em Sistemas de Informação**.

## Sobre o Projeto

O TripLogs é uma aplicação desenvolvida com Django Rest Framework que permite aos usuários registrar e gerenciar suas viagens de forma organizada. Com funcionalidades completas de autenticação JWT e upload de imagens, é a solução perfeita para quem quer manter um diário digital de suas aventuras.

### Funcionalidades

- **Autenticação JWT**: Sistema seguro de login e registro
- **Gerenciamento de Usuários**: Perfis personalizados e controle de acesso
- **Registro de Viagens**: CRUD completo para viagens
- **Documentação Automática**: API documentada com Swagger/OpenAPI
- **CORS Configurado**: Pronto para integração com frontend
- **Banco de Dados Flexível**: Suporte para SQLite, PostgreSQL e MySQL

## Arquitetura

```
triplogs-backend/
├── app/                    # Configurações principais do Django
│   ├── settings.py        # Configurações da aplicação
│   ├── urls.py           # URLs principais
│   └── wsgi.py           # WSGI configuration
├── core/                  # App principal
│   ├── models/           # Modelos de dados
│   │   ├── user.py      # Modelo customizado de usuário
│   │   └── trip.py      # Modelo de viagens
│   ├── serializers/     # Serializadores DRF
│   ├── views/           # ViewSets da API
│   └── migrations/      # Migrações do banco
├── media/               # Arquivos de mídia
├── scripts/             # Scripts utilitários
└── requirements.txt     # Dependências Python
```

## Começando

### Pré-requisitos

- Python 3.10+
- PDM (Python Dependency Manager) ou pip
- Git

### Instalação

1. **Clone o repositório**

   ```bash
   git clone https://github.com/gabriel04alves/triplogs-backend.git
   cd triplogs-backend
   ```

2. **Instale as dependências**

   Com PDM (recomendado):

   ```bash
   pdm install
   ```

   Ou com pip:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure as variáveis de ambiente**

   ```bash
   cp .env.example .env
   # Edite o arquivo .env com suas configurações
   ```

4. **Execute as migrações**

   ```bash
   pdm run migrate
   # ou: python manage.py migrate
   ```

5. **Crie um superusuário**

   ```bash
   pdm run createsuperuser
   # ou: python manage.py createsuperuser
   ```

6. **Inicie o servidor**
   ```bash
   pdm run dev
   # ou: python manage.py runserver
   ```

## Configuração

### Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
# Modo de execução
MODE=DEVELOPMENT  # ou PRODUCTION

# Chave secreta do Django
SECRET_KEY=sua-chave-secreta-super-segura

# Debug
DEBUG=True

# Banco de dados (opcional, padrão é SQLite)
DATABASE_URL=postgresql://user:password@localhost:5432/triplogs

# Cloudinary (para produção)
CLOUDINARY_URL=cloudinary://api_key:api_secret@cloud_name

# IP local (para desenvolvimento)
MY_IP=127.0.0.1
```

### Banco de Dados

O projeto suporta múltiplos bancos de dados através da variável `DATABASE_URL`:

- **SQLite** (padrão): `sqlite:///db.sqlite3`
- **PostgreSQL**: `postgresql://user:password@localhost:5432/dbname`
- **MySQL**: `mysql://user:password@localhost:3306/dbname`

## Documentação da API

Após iniciar o servidor, acesse:

- **Swagger UI**: `http://localhost:8000/api/swagger/`
- **ReDoc**: `http://localhost:8000/api/redoc/`
- **Schema OpenAPI**: `http://localhost:8000/api/schema/`

### Endpoints Principais

| Método         | Endpoint              | Descrição                      |
| -------------- | --------------------- | ------------------------------ |
| POST           | `/api/token/`         | Obter token JWT                |
| POST           | `/api/token/refresh/` | Renovar token                  |
| GET            | `/api/usuarios/me/`   | Perfil do usuário logado       |
| GET/POST       | `/api/trips/`         | Listar/Criar viagens           |
| GET/PUT/DELETE | `/api/trips/{id}/`    | Detalhes/Editar/Excluir viagem |

### Exemplo de Uso

```bash
# 1. Criar usuário
curl -X POST http://localhost:8000/api/usuarios/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "usuario@email.com",
    "password": "senha123",
    "name": "João Silva"
  }'

# 2. Fazer login
curl -X POST http://localhost:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "usuario@email.com",
    "password": "senha123"
  }'

# 3. Criar viagem (com token)
curl -X POST http://localhost:8000/api/trips/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer seu-token-aqui" \
  -d '{
    "title": "Viagem para Paris",
    "location": "Paris, França",
    "trip_date": "2024-06-15",
    "description": "Uma viagem incrível pela cidade luz!"
  }'
```

## Scripts Disponíveis

```bash
# Desenvolvimento
pdm run dev              # Iniciar servidor de desenvolvimento
pdm run makemigrations   # Criar novas migrações
pdm run migrate          # Aplicar migrações
pdm run createsuperuser  # Criar superusuário

# Ferramentas
pdm run shell           # Shell do Django
pdm run shellp          # Shell Plus com imports automáticos
pdm run test            # Executar testes
pdm run loaddata        # Carregar dados de exemplo
pdm run dumpdata        # Exportar dados

# Qualidade de código
pdm run check           # Verificar código com Ruff
pdm run format          # Formatar código
```

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para detalhes.
