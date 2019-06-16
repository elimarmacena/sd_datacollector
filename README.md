# Coleta de Dados (Sistemas Distribuidos)
Repositório destinado a aplicação de coleta de dados com auxilio de middleware
## Tecnologias
A aplicação faz uso das seguintes tecnologias:
* RabbitMQ -  Menssage broken middleware
* Peewee - ORM Python
* Flask - Framework Python destinado ao back-end para o tratamento de dados e envio de informações
* Vue.js - Framework Javascript destinado ao front-end
* ElephantSql - servidor em nuvem postgreSQL
## Introdução
O sistema possui uma premissa básica, que se trata do envio de dados do ambiente de diferentes locais para uma aplicação que irá fazer o tratamento das informações recebidas e efetuar a persistência dos dados em um banco de dados para a geração de relatórios.
<p align="center">
<img src="https://github.com/elimarmacena/sd_datacollector/blob/master/documentacao/architecture.svg"> <br>
<em>Arquitetura da aplicação.</em> 
</p>

## Dependência
* Comunicação com o banco de dados
Como se trata de uma aplicação usando a linguagem Python para acessar o banco de dados é feito o uso da ORM peewee, na qual é necessaria fazer a instalação e pode ser feita da seguinte maneira:
```bash
pip3 install peewee
```

* Comunicação Python x RabbitMQ
Uma vez que a simulação dos dispositivos de coleta de dados serão feitas via código na linguagem de programação Python é necessário a instalação da biblioteca de comunicação com o RabbitMq, o pika, a instalação deve ser feita da seguinte maneira:
```bash
pip3 install pika
```
* RabbitMQ
Para a utilização do RabbitMQ neste trabalho foi utilizado uma imagem docker do middler, neste caso foi feito o uso do seguinte tutorial de uso básico [RabbitMQ-Tutorial](https://github.com/oprearocks/RabbitMQ-Docker-cluster)


## Utilização local
* iniciar a imagem docker referente ao rabbitMQ(necessario ter a imagem do rabbitMQ no docker)
```bash
docker ps -a
```
> apos a listagem das imagens copiar o ID do contaiter e então executar o comando
```bash
docker start <id_conteinar>
```

* iniciar o serviço flask (necessario estar na pasta do repositorio)
 ```bash
source sd_back/flask_env/bin/active
export FLASK_APP=sd_back
export FLASK_ENV=development
flask run
```

* iniciar o serviço front end (necessario estar na pasta sd_front)
 ```bash
npm run dev
```
