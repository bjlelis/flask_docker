# Flask com Docker:

Este projeto é um exemplo simples de aplicação Flask rodando em Docker, com estrutura organizada e suporte a variáveis de ambiente. Ideal para quem está aprendendo Docker ou Flask e quer um ponto de partida com boas práticas.

## O que esse projeto faz:

- Roda uma aplicação Flask containerizada com Docker
- Estrutura modular (app separado em pastas)
- Uso de variáveis de ambiente via `.env`
- Exposição de duas rotas:
  - `/` – retorna uma mensagem padrão
  - `/env` – retorna uma variável definida no `.env`

## Estrutura do projeto:

meuapp/
- app/__init__.py e app/routes.py
- app.py
- requirements.txt
- Dockerfile
- .dockerignore
- .env
- README.md

## Requisitos:
- Python 3.11+
- Flask
- python-dotenv (para carregar variáveis de ambiente)
- Docker (para containerizar a aplicação)


### Para rodar localmente:

1. Clone o repositório:
    ```bash
    git clone https://github.com/bjlelis/flask_docker.git
    cd flask-docker
    ```

2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

3. Execute a aplicação:
    ```bash
    python app.py
    ```

Isso vai rodar o Flask localmente na porta `5000` (por padrão). Acesse no navegador `http://localhost:5000/`.


## Como rodar com Docker

1. Build da imagem:

```bash
docker build -t flask-hello .

2. Executando o container:

docker run --env-file .env -p 5000:5000 flask-hello

3. Acessar no navegador:

http://localhost:5000/ → Retorna mensagem padrão

http://localhost:5000/env → Retorna valor da variável MESSAGE do .env


## 🤝 Contribuindo

Sinta-se à vontade para clonar o repositório, fazer melhorias ou abrir pull requests! Para começar:

1. Faça um fork deste repositório
2. Crie uma branch com sua feature:
    ```bash
    git checkout -b minha-feature
    ```
3. Commit suas mudanças:
    ```bash
    git commit -am 'Adiciona nova feature'
    ```
4. Envie a branch para o repositório remoto:
    ```bash
    git push origin minha-feature
    ```
5. Abra um Pull Request.



