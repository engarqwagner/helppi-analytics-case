import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

engine = create_engine(
    f"mysql+mysqlconnector://{os.getenv('MYSQL_USER')}:"
    f"{os.getenv('MYSQL_PASSWORD')}@"
    f"{os.getenv('MYSQL_HOST')}/"
    f"{os.getenv('MYSQL_DB')}"
)

dim_clientes = pd.read_csv("data/processed/dim_clientes.csv")
dim_servicos = pd.read_csv("data/processed/dim_servicos.csv")
fato_atendimentos = pd.read_csv("data/processed/fato_atendimentos.csv")
fato_nps = pd.read_csv("data/processed/fato_nps.csv")

dim_clientes.to_sql("dim_clientes", engine, if_exists="replace", index=False)
dim_servicos.to_sql("dim_servicos", engine, if_exists="replace", index=False)
fato_atendimentos.to_sql("fato_atendimentos", engine, if_exists="replace", index=False)
fato_nps.to_sql("fato_nps", engine, if_exists="replace", index=False)

print("Dados carregados no MySQL com sucesso!")
