import yfinance as yf
import pandas as pd 
from datetime import datetime

def get_commodities_df():
    symbols = ["CL=F", "GC=F", "SI=F"]
    dfs = []
    for sym in symbols:
        ultimo_df = yf.Ticker(sym).history(period="1d", interval="1m")[['Close']].tail(1)
        ultimo_df = ultimo_df.rename(columns={'Close':'preco'})
        ultimo_df['ativo'] = sym
        ultimo_df['moeda'] = 'USD'
        ultimo_df['horario_coleta'] = datetime.now()
        ultimo_df = ultimo_df[['ativo','preco','moeda','horario_coleta']]
        # append this symbol's latest row to the list
        dfs.append(ultimo_df)

    return pd.concat(dfs, ignore_index=True)