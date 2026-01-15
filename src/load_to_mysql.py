import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# =========================
# Inicialização
# =========================
print(">>> SCRIPT INICIADO")

# Carrega variáveis de ambiente
load_dotenv()

# Diretórios
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "..", "data", "processed")

print("Arquivo:", __file__)
print("CWD:", os.getcwd())
print("DATA_DIR:", DATA_DIR)

# Validação da pasta de dados
if not os.path.exists(DATA_DIR):
    raise FileNotFoundError(f"Pasta de dados não encontrada: {DATA_DIR}")

print("Arquivos encontrados:", os.listdir(DATA_DIR))

# =========================
# Conexão com MySQL
# =========================
engine = create_engine(
    f"mysql+pymysql://{os.getenv('MYSQL_USER')}:"
    f"{os.getenv('MYSQL_PASSWORD')}@"
    f"{os.getenv('MYSQL_HOST')}/"
    f"{os.getenv('MYSQL_DB')}",
    pool_pre_ping=True
)


print("Conexão com MySQL criada")

# =========================
# Leitura dos CSVs
# =========================
print("Lendo CSVs...")

dim_clientes = pd.read_csv(os.path.join(DATA_DIR, "dim_clientes.csv"))
print("dim_clientes:", dim_clientes.shape)

dim_servicos = pd.read_csv(os.path.join(DATA_DIR, "dim_servicos.csv"))
print("dim_servicos:", dim_servicos.shape)

fato_atendimentos = pd.read_csv(os.path.join(DATA_DIR, "fato_atendimentos.csv"))
print("fato_atendimentos:", fato_atendimentos.shape)

fato_nps = pd.read_csv(os.path.join(DATA_DIR, "fato_nps.csv"))
print("fato_nps:", fato_nps.shape)

# =========================
# Carga no MySQL
# =========================
print("Iniciando carga no MySQL...")

dim_clientes.to_sql(
    "dim_clientes",
    engine,
    if_exists="replace",
    index=False,
    chunksize=1000,
    method="multi"
)
print("✔ dim_clientes carregada")

dim_servicos.to_sql(
    "dim_servicos",
    engine,
    if_exists="replace",
    index=False,
    chunksize=1000,
    method="multi"
)
print("✔ dim_servicos carregada")

fato_atendimentos.to_sql(
    "fato_atendimentos",
    engine,
    if_exists="replace",
    index=False,
    chunksize=1000,
    method="multi"
)
print("✔ fato_atendimentos carregada")

fato_nps.to_sql(
    "fato_nps",
    engine,
    if_exists="replace",
    index=False,
    chunksize=1000,
    method="multi"
)
print("✔ fato_nps carregada")

print("✅ Dados carregados no MySQL com sucesso!")
