import pandas as pd
from getBitcoin import get_bitcoin_df
from getCommodities import get_commodities_df  


valor_bitcoin = get_bitcoin_df()
valor_commodities = get_commodities_df()

print(valor_bitcoin)
print(valor_commodities)