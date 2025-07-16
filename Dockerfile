FROM python:3.11-slim

WORKDIR /app

# Instala dependências do sistema necessárias para mysqlclient
RUN apt-get update && \
    apt-get install -y gcc default-libmysqlclient-dev pkg-config && \
    rm -rf /var/lib/apt/lists/*

# Copia os arquivos de dependências
COPY requirements.txt .

# Instala as dependências Python
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copia o restante do código da aplicação
COPY . .

# Expõe a porta padrão do Django
EXPOSE 3000

# Comando padrão para rodar o build.sh
CMD ["./build.sh"]
