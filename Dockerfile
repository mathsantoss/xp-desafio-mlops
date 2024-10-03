FROM python:3.11-bullseye

LABEL version="0.0.1"
LABEL description="Plataform to deploy models and request inference for trained models."

# Define a pasta de trabalho no container
WORKDIR /app

# Copia o arquivo de dependências
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o diretório do projeto para o container
COPY . .

# Garante que o modelo está no local correto (verifique o caminho)
RUN mkdir -p /app/model && cp /app/data/model.pkl /app/model/

# Define a variável de ambiente necessária (por exemplo, para o Kedro)
ENV PYTHONPATH=/app/src

# Expõe a porta para a FastAPI
EXPOSE 8000

# Comando para rodar a aplicação usando uvicorn
# CMD ["uvicorn", "src.xp_mlops.app:application", "--host", "0.0.0.0", "--port", "8000", "--reload"]

# Build stuff
COPY docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]