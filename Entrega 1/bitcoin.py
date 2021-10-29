investment_in_bitcoin = 1.2
bitcoin_to_euros = 40000

def bitcoinToEuros(bitcoin_amount, bitcoin_value_euros):
    euros_value = bitcoin_amount * bitcoin_value_euros
    if euros_value < 30000:
        print("El valor ha bajado de 30000, es aconsejable retirar.")
    else:
        print("El valor está por encima de 30000, es recomendable invertir.")

bitcoinToEuros(1, 25000)