# 🍷 XP-MLOps API

Este projeto implementa uma API de inferência em tempo real para previsões de Machine Learning usando FastAPI e Kedro. O modelo utilizado neste projeto é baseado no dataset de vinho da biblioteca `sklearn`. A aplicação também foi containerizada usando Docker para facilitar a execução e a implantação.

## 📊 Modelo de Vinho

O dataset de vinho (`load_wine()`) do `sklearn` contém informações químicas sobre várias amostras de vinho. Neste projeto, treinamos um modelo de Regressão Linear para prever o teor alcoólico de uma amostra de vinho com base nas demais características químicas.

O pipeline do Kedro inclui os seguintes passos:
1. **Carregamento dos dados**: Usamos o dataset de vinho do `sklearn`.
2. **Divisão dos dados**: Os dados são divididos em conjuntos de treino e teste.
3. **Treinamento do modelo**: Um modelo de Regressão Linear é treinado com os dados de treino.
4. **Avaliação do modelo**: O erro quadrático médio (MSE) é calculado para avaliar o desempenho do modelo.
5. **Salvamento do modelo**: O modelo treinado é salvo em um arquivo `.pkl`.

## 🛠️ Pré-requisitos

Antes de começar, certifique-se de que você tem o seguinte instalado em seu sistema:

- [Docker](https://docs.docker.com/get-docker/)
- [Python 3.11+](https://www.python.org/downloads/)
- [Kedro](https://kedro.readthedocs.io/en/stable/get_started/install.html)

## 🚀 Instruções de Uso

### 1. Construir a imagem Docker

Para construir a imagem Docker do projeto, execute o seguinte comando a partir do diretório raiz do projeto, onde está localizado o `Dockerfile`.

```bash
docker build -t xp-mlops-api .
```

### 2. Executar o container Docker

Após a construção da imagem, execute o container com o seguinte comando:

```bash
docker run -d -p 8000:8000 xp-mlops-api
```

Agora, a API estará disponível em `http://localhost:8000`.

### 3. Testar a API

Você pode acessar a documentação interativa da API usando o Swagger UI em:

```
http://localhost:8000/docs
```

### 4. Parar o container

Para parar o container, liste os containers em execução:

```bash
docker ps
```

E pare o container usando o ID mostrado:

```bash
docker stop <container_id>
```

## 🧑‍💻 Rodando Localmente (Sem Docker)

Se você preferir rodar a API localmente sem Docker, siga as instruções abaixo:

### 1. Instalar as dependências

Certifique-se de que você está em um ambiente virtual Python e execute o comando:

```bash
pip install -r requirements.txt
```

### 2. Treinar o modelo usando Kedro

Para treinar o modelo, utilize o comando abaixo para executar o pipeline do Kedro:

```bash
kedro run
```

Isso irá rodar o pipeline de treinamento e salvar o modelo treinado no diretório especificado (`model/model.pkl`).

### 3. Subir a API localmente

Com o modelo treinado, suba a API localmente utilizando o Uvicorn:

```bash
uvicorn src.xp_mlops.app:application --host 0.0.0.0 --port 8000 --reload
```

Agora a API estará disponível em `http://localhost:8000` e com suporte a hot-reload para desenvolvimento.

## 🗂️ Estrutura do Projeto

- `src/xp_mlops/api/`: contém as rotas da API e os endpoints.
- `src/xp_mlops/create_app.py`: função que cria a instância da aplicação FastAPI.
- `src/xp_mlops/app.py`: ponto de entrada da aplicação.
- `model/model.pkl`: modelo treinado usado para inferências.

## 🔧 Comandos Úteis

### Verificar imagens Docker

```bash
docker images
```

### Verificar containers em execução

```bash
docker ps
```

### Construir e rodar a imagem em um único comando

```bash
docker build -t xp-mlops-api . && docker run -d -p 8000:8000 xp-mlops-api
```

Isso irá construir e iniciar a API automaticamente.

## ⚠️ Problemas Comuns

### Docker Daemon Não Encontrado

Se você receber um erro relacionado ao Docker Daemon, verifique se o Docker está rodando com:

```bash
sudo systemctl start docker
```

## 💻 Contribuições

Se você deseja contribuir, siga os seguintes passos:

1. Faça um fork do repositório.
2. Crie uma branch para a sua feature: `git checkout -b minha-feature`.
3. Faça commit das suas alterações: `git commit -m 'Adicionei minha feature'`.
4. Faça o push para a branch: `git push origin minha-feature`.
5. Abra um Pull Request.
