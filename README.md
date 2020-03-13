# cft-challenge

## Teste

Criar uma API REST em Python (Django ou Flask) que consuma a API do [Genius](https://docs.genius.com/#/getting-started-h1) e que dado um artista, liste as 10 músicas mais populares do artista pesquisado.


## Este projeto foi feito com:

* Python 3.7
* Flask==1.1.1

## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode os testes.

```
git clone https://github.com/rg3915/cft-challenge.git
cd cft-challenge
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Variáveis de ambientes:

```
TOKEN=SEU_TOKEN_DO_GENIUS
FLASK_APP=app:create_app
```

## Rodando a app

```
python -m unittest test_app.py
flask run
```

Em outro terminal faça:

```
http get http://127.0.0.1:5000/artist/Metallica
```