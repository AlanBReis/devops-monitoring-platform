# Usa a imagem oficial do Python como base
FROM python:3.9-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos de requisitos para o contêiner
COPY requirements.txt requirements.txt

# Instala as dependências da aplicação
RUN pip install -r requirements.txt

# Copia o código da aplicação para o diretório de trabalho
COPY . .

# Exponha a porta 5000 para o Flask
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "main.py"]
