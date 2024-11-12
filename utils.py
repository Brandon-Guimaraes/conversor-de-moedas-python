import requests

# Função para obter as taxas de câmbio da API
def get_exchange_rates(api_key):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"  # Taxas com USD como moeda base
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data['conversion_rates']
    else:
        print("Erro ao obter taxas de câmbio:", response.status_code)
        return None

# Função para converter um valor entre duas moedas usando as taxas de câmbio
def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency not in rates or to_currency not in rates:
        print("Moeda inválida ou não suportada.")
        return None

    # Converter a moeda de origem para USD e depois para a moeda de destino
    amount_in_usd = amount / rates[from_currency]  # Converter para USD
    converted_amount = amount_in_usd * rates[to_currency]  # Converter para a moeda desejada
    return converted_amount

# Função principal que faz a interação com o usuário
def main():
    # Solicita a chave de API ao usuário
    api_key = input("Digite sua chave de API: ")

    # Obter as taxas de câmbio
    rates = get_exchange_rates(api_key)
    if not rates:
        print("Falha ao obter taxas de câmbio. Verifique sua chave de API e tente novamente.")
        return

    # Solicitar os detalhes da conversão ao usuário
    from_currency = input("Digite a moeda de origem (ex: USD): ").upper()
    to_currency = input("Digite a moeda de destino (ex: EUR): ").upper()
    try:
        amount = float(input("Digite o valor a ser convertido: "))
    except ValueError:
        print("Valor inválido. Por favor, digite um número.")
        return

    # Realizar a conversão
    converted_amount = convert_currency(amount, from_currency, to_currency, rates)
    if converted_amount is not None:
        print(f"\n{amount} {from_currency} é igual a {converted_amount:.2f} {to_currency}")
