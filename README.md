# XP-MLOps API

Este projeto implementa uma API de inferência em tempo real para previsões de Machine Learning usando FastAPI e Kedro. A aplicação foi containerizada usando Docker para fácil execução e implantação.

## Pré-requisitos

Antes de começar, certifique-se de que você tem o seguinte instalado em seu sistema:

- [Docker](https://docs.docker.com/get-docker/)
- [Python 3.11+](https://www.python.org/downloads/)
- [Kedro](https://kedro.readthedocs.io/en/stable/get_started/install.html)

## Instruções de Uso

### 1. Construir a imagem Docker

Para construir a imagem Docker do projeto, execute o seguinte comando a partir do diretório raiz do projeto, onde está localizado o `Dockerfile`.

```bash
docker build -t xp-mlops-api .
```

Este comando fará o build da imagem Docker com todas as dependências necessárias e incluirá o artefato do modelo treinado.

### 2. Executar o container Docker

Após a construção da imagem, execute o container com o seguinte comando:

```bash
docker run -d -p 8000:8000 xp-mlops-api
```

Aqui está o que o comando faz:
- `-d`: executa o container em segundo plano (modo detached).
- `-p 8000:8000`: mapeia a porta 8000 do host para a porta 8000 do container.
- `xp-mlops-api`: nome da imagem construída.

Agora, a API estará disponível em `http://localhost:8000`.

### 3. Testar a API

Você pode acessar a documentação interativa da API usando o Swagger UI, que está disponível em:

```
http://localhost:8000/docs
```

Ou, se preferir o Redoc:

```
http://localhost:8000/redoc
```

### 4. Parar o container

Para parar o container, você pode listar os containers em execução:

```bash
docker ps
```

E, em seguida, parar o container usando o ID mostrado:

```bash
docker stop <container_id>
```

## Rodando Localmente (Sem Docker)

Se você preferir rodar a API localmente sem Docker, siga as instruções abaixo:

### 1. Instale as dependências

Certifique-se de que você está em um ambiente virtual Python e execute o comando:

```bash
pip install -r requirements.txt
```

### 2. Treine o modelo usando Kedro

Para treinar o modelo, utilize o comando abaixo para executar o pipeline do Kedro:

```bash
kedro run
```

Isso irá rodar o pipeline de treinamento e salvar o modelo treinado no diretório especificado no pipeline (`model/model.pkl`).

### 3. Suba a API localmente

Com o modelo treinado, suba a API localmente utilizando o Uvicorn:

```bash
uvicorn src.xp_mlops.app:application --host 0.0.0.0 --port 8000 --reload
```

Agora a API estará disponível em `http://localhost:8000` e com suporte a hot-reload para desenvolvimento.

## Estrutura do Projeto

- `src/xp_mlops/api/`: contém as rotas da API e os endpoints.
- `src/xp_mlops/create_app.py`: função que cria a instância da aplicação FastAPI.
- `src/xp_mlops/app.py`: ponto de entrada da aplicação.
- `model/model.pkl`: modelo treinado usado para inferências.

## Comandos Úteis

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

## Problemas Comuns

### Docker Daemon Não Encontrado

Se você receber um erro relacionado ao Docker Daemon, verifique se o Docker está rodando com:

```bash
sudo systemctl start docker
```

## Contribuições

Se você deseja contribuir, siga os seguintes passos:

1. Faça um fork do repositório.
2. Crie uma branch para a sua feature: `git checkout -b minha-feature`.
3. Faça commit das suas alterações: `git commit -m 'Adicionei minha feature'`.
4. Faça o push para a branch: `git push origin minha-feature`.
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).




kedro run --pipeline wine_pipeline

sudo grep -iR "docker" /var/log |grep -i "Error" 
