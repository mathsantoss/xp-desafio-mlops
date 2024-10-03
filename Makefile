ifndef VERBOSE
MAKEFLAGS += --no-print-directory -s
endif

DOCKERFILE ?= Dockerfile  # Dockerfile padrão

# Nome da imagem Docker
IMAGE_NAME=xp-imagem



run: ## Run the application
	@PYTHONPATH=./ uvicorn src.xp_mlops.app:application --reload



# Comando para construir a imagem Docker
build:
    docker build -t $(IMAGE_NAME) .

# Comando para rodar o container
docker-run:
    docker run -d --name $(IMAGE_NAME) -p 8000:8000 $(IMAGE_NAME)

# Comando para parar o container
stop:
    docker stop $(IMAGE_NAME)

# Comando para remover o container
remove:
    docker rm $(IMAGE_NAME)

# Comando para executar o container em modo interativo
exec:
    docker exec -it $(IMAGE_NAME) /bin/sh

# Comando para construir e rodar tudo de uma vez
up: build run


help: ## Show some help
	@echo
	@echo '  Usage:'
	@echo '    make <target>'
	@echo
	@echo '  Targets:'
	@egrep '^(.+)\:\ ##\ (.+)' ${MAKEFILE_LIST} | column -t -c 2 -s ':#'
	@echo
