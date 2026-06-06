# Sistema de Gerenciamento de Entregas

## Descrição

Sistema desenvolvido em Python para gerenciamento de entregas, permitindo o cadastro de clientes, cadastro de entregadores e criação de pedidos com diferentes tipos de entrega.

O projeto foi desenvolvido utilizando conceitos de Programação Orientada a Objetos, incluindo:

* Classes e objetos
* Herança
* Polimorfismo
* Interfaces
* Encapsulamento
* Modularização

## Estrutura do Projeto

```text
projeto/
├── modelos/
├── services/
├── interfaces/
├── util/
├── main.py
└── README.md
```

## Funcionalidades

### Clientes

* Cadastrar cliente
* Listar clientes

### Entregadores

* Cadastrar entregador
* Listar entregadores

### Pedidos

* Criar pedido
* Listar pedidos
* Atualizar status do pedido

### Tipos de Entrega

* Entrega Comum
* Entrega Expressa
* Entrega Premium

Cada tipo de entrega possui sua própria implementação para cálculo de frete.

## Requisitos

* Python 3.10 ou superior

## Execução

Execute o arquivo principal do projeto:

```bash
python main.py
```

## Conceitos Aplicados

### Herança

As classes `Cliente` e `Entregador` herdam da classe `Pessoa`.

### Interface

A interface de cálculo de frete define o contrato implementado pelas classes de entrega.

### Polimorfismo

Os diferentes tipos de entrega implementam o cálculo de frete de forma específica.

### Encapsulamento

Os atributos das classes são protegidos por meio de encapsulamento e utilização de propriedades.

## Autor

Carlos Augusto
