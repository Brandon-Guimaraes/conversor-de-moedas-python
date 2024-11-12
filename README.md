# Conversor de Moedas

Este é um projeto em Python que converte valores entre diferentes moedas usando uma API de taxas de câmbio em tempo real.

## Pré-requisitos

- Python 3.6 ou superior
- Uma chave de API da [ExchangeRate-API](https://www.exchangerate-api.com/)

## Instalação

1. Clone este repositório para sua máquina local:

    ```bash
    git clone https://github.com/seu-usuario/conversor-de-moedas.git
    cd conversor-de-moedas
    ```

2. Instale as dependências necessárias:

    ```bash
    pip install requests
    ```

## Uso

1. No terminal, navegue até o diretório do projeto.
2. Execute o script `main.py`:

    ```bash
    python main.py
    ```

3. O programa solicitará sua chave de API, moeda de origem, moeda de destino e valor a ser convertido.

### Exemplo de Execução

```plaintext
Digite sua chave de API: sua_chave_aqui
Digite a moeda de origem (ex: USD): USD
Digite a moeda de destino (ex: EUR): EUR
Digite o valor a ser convertido: 100

100 USD é igual a 84.50 EUR
