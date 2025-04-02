FROM python:3.11-slim

WORKDIR /app

RUN pip install --upgrade pip
# Instalar dependências do Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código
COPY . /app/

EXPOSE 8000
