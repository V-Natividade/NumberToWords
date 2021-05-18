# Number to Words
NumberToWords tem a finalidade de converter números inteiros e cardinais em números extensos, ou seja, pegar o número "110" e converter para "cento e dez".

Escrito encima da linguagem python, foi dockerizado com o servidor HTTP gunicorn, se baseando nas regras do wsgi.

## Pré-requisitos
Ter o Docker instalado na máquina, vide a [documentação oficial](https://docs.docker.com/get-docker/).

Ou

Possuir o python 3.x, a instalação do python está descriminada na seção a seguir.

## Instalação
No Ubuntu, Mint e Debian, você pode instalar copiando e colando o comando a seguir no seu terminal:
```bash
$ sudo apt-get install python3 python3-pip
```
Para outras distribuições Linux, macOS e Windows, podes consultar o [site oficial](http://www.python.org/getit/).

## Uso
Já com o docker instalado na máquina, dê os comandos a seguir:

```python
$ sudo docker build -t run_server . #cria a imagem docker
$ sudo docker run -p --rm 8080:8000 run_server #roda a imagem criada
```
Ou

Com o python3 já instalado, crie uma virtualenv seguindos esses [passos](https://docs.python.org/3/library/venv.html) e com a virtualenv já ativa, digite os seguintes comandos no seu terminal:

```python
$ pip install -r requirements.txt
$ gunicorn --bind 127.0.0.1:3000 http_server:Server
```
Após realizados os comandos navegue clique [aqui](http://localhost:8000/).

Obs: se quiser deixar de rodar o servidor, clique CTRL+C no seu terminal.

## Testes
Se você quer ver se tudo está funcionando como deveria, dê o seguinte comando:
```python
$ python -m unittest
```

## Contribuindo
Pull requests são bem-vindos. Para mudanças importantes, abra um problema primeiro para discutir o que você gostaria de mudar.

## Licença
Licença [MIT](https://choosealicense.com/licenses/mit/#)
