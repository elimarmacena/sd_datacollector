# Coleta de Dados (Sistemas Distribuidos)
Repositório destinado a aplicação de coleta de dados com auxilio de middleware
## Tecnologias
A aplicação faz uso das seguintes tecnologias:
* RabbitMQ -  Menssage broken middleware
* Flask - Framework Python destinado ao back-end para o tratamento de dados e envio de informações
* React.js - Framework Javascript destinado ao front-end
## Introdução
O sistema possui uma premissa básica, que se trata do envio de dados do ambiente de diferentes locais para uma aplicação que irá fazer o tratamento das informações recebidas e efetuar a persistência dos dados em um banco de dados para a geração de relatórios.
<p align="center">
<img src="https://github.com/elimarmacena/sd_datacollector/blob/master/documentacao/architecture.svg"> <br>
<em>Arquitetura da aplicação.</em> 
</p>

## Dependência
* Comunicação Python x RabbitMQ
Uma vez que a simulação dos dispositivos de coleta de dados serão feitas via código na linguagem de programação Python é necessário a instalação da biblioteca de comunicação com o RabbitMq, o pika, a instalação deve ser feita da seguinte maneira:
```bash
pip3 install pika
```
* RabbitMQ
Para a utilização do RabbitMQ neste trabalho foi utilizado uma imagem docker do middler, neste caso foi feito o uso do seguinte tutorial de uso básico [RabbitMQ-Tutorial](https://github.com/oprearocks/RabbitMQ-Docker-cluster)

