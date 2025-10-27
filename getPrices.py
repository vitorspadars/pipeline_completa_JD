import pandas as pd
import time
from getBitcoin import get_bitcoin_df
from getCommodities import get_commodities_df  


valor_bitcoin = get_bitcoin_df()
valor_commodities = get_commodities_df()


while True:
    print(valor_bitcoin)
    print(valor_commodities)

    df = pd.concat([valor_bitcoin, valor_commodities], ignore_index=True)

    time.sleep(60)
