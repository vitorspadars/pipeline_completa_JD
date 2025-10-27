import pandas as pd
import time
from sqlalchemy import create_engine
from getBitcoin import get_bitcoin_df
from getCommodities import get_commodities_df

from dotenv import load_dotenv
import os

# variaveis de ambiente
load_dotenv()

# Conexão com o DB
DB_USER = os.getenv("user")
DB_PASSWORD = os.getenv("password")
DB_HOST = os.getenv("host")
DB_PORT = os.getenv("port")
DB_NAME = os.getenv("dbname")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)


SLEEPER_TIME = 60


valor_bitcoin = get_bitcoin_df()
valor_commodities = get_commodities_df()

if __name__ == "__main__":
    while True:
        df_btc = get_bitcoin_df()
        df_comm = get_commodities_df()


        df = pd.concat([df_btc, df_comm], ignore_index=True)

        df.to_sql("bronze_cotacoes", engine, if_exists="append", index=False)

        print("Dados inseridos com sucesso!")

        time.sleep(SLEEPER_TIME)
