#!/usr/bin/env bash
# Sai do script se houver algum erro
set -o errexit

# Exibe informações sobre o ambiente
echo "Iniciando em modo: $MODE"

# Atualiza o pip
pip install --upgrade pip

# Instala as dependências
pip install -r requirements.txt

python manage.py collectstatic --no-input

# Aplica as migrações
echo "Aplicando migrações..."
python manage.py migrate --noinput

# Inicia o servidor Gunicorn
echo "Iniciando servidor Gunicorn..."
gunicorn --bind 0.0.0.0:8000 --workers ${WEB_CONCURRENCY:-4} app.wsgi:application

# Para buildar a imagem Docker:
# docker build -t triplogs-backend .
# Para rodar o container:
# docker run --rm -it -p 8000:8000 -v $(pwd):/app triplogs-backend