import requests
from datetime import datetime
import pandas as pd

def get_bitcoin_df():
    # URL
    url = "https://api.coinbase.com/v2/prices/spot"

    # GET para pegar os dados da API
    response = requests.get(url)
    data = response.json()

    #Extrair os dados que eu quero
    preco = float(data['data']['amount'])
    ativo = data['data']['base']
    moeda = data['data']['currency']
    horario = datetime.now()

    df = pd.DataFrame([{
        'ativo' : ativo,
        'preco' : preco,
        'moeda' : moeda,
        'horario_coleta' : horario
    }])

    return df