# Importa a biblioteca pandas para manipulação de dados.
import pandas as pd

# Importa numpy para operações numéricas e controle de aleatoriedade
import numpy as np

# Importa Faker para geração de dados fictícios
from faker import Faker

# Importa classes para trabalhar com datas e intervalos de tempo
from datetime import datetime, timedelta

# Importa funções de aleatoriedade
import random

# Inicializa o Faker com localização brasileira
fake = Faker("pt_BR")

# Define uma semente fixa para resultados reproduzíveis
np.random.seed(42)

# =========================
# PARAMETROS
# =========================

# Quantidade de clientes a serem gerados
NUM_CLIENTES = 5000

# Quantidade de atendimentos a serem gerados
NUM_ATENDIMENTOS = 20000

# Data inicial do período de dados
DATA_INICIO = datetime(2023, 1, 1)

# Data final do período de dados
DATA_FIM = datetime(2025, 12, 31)

# Define os planos disponíveis e seus valores mensais
PLANOS = {
    "Basico": 39.90,
    "Essencial": 59.90,
    "Premium": 89.90
}

# Lista de serviços com nome, categoria e custo médio
SERVICOS = [
    ("Assistência Residencial", "Residencial", 120),
    ("Assistência Automotiva", "Automotivo", 180),
    ("Telemedicina", "Saúde", 40),
    ("Psicologia Online", "Saúde", 70),
    ("Clube de Descontos", "Benefícios", 10),
    ("Assistência Pet", "Pet", 90),
    ("Seguro Celular", "Seguro", 60),
    ("Consultoria Jurídica", "Jurídico", 110),
]

# =========================
# CLIENTES
# =========================

# Lista vazia para armazenar os clientes
clientes = []

# Loop para criar cada cliente
for i in range(1, NUM_CLIENTES + 1):

    # Escolhe um plano aleatoriamente
    plano = random.choice(list(PLANOS.keys()))

    # Gera uma data de adesão aleatória
    data_adesao = fake.date_between(start_date="-36m", end_date="today")

    # Adiciona os dados do cliente na lista
    clientes.append({
        "id_cliente": i,
        "nome": fake.name(),
        "cidade": fake.city(),
        "estado": fake.state_abbr(),
        "plano": plano,
        "valor_mensal": PLANOS[plano],
        "data_adesao": data_adesao,
        "status": random.choices(
            ["Ativo", "Churn"],
            weights=[0.82, 0.18]
        )[0]
    })

# Converte a lista de clientes em DataFrame
df_clientes = pd.DataFrame(clientes)

# =========================
# SERVICOS
# =========================

# Lista vazia para armazenar os serviços
servicos = []

# Loop para criar cada serviço
for idx, serv in enumerate(SERVICOS, start=1):

    # Adiciona os dados do serviço
    servicos.append({
        "id_servico": idx,
        "nome_servico": serv[0],
        "categoria": serv[1],
        "custo_medio": serv[2],
        "preco_venda": serv[2] * random.uniform(1.3, 1.8)
    })

# Converte a lista de serviços em DataFrame
df_servicos = pd.DataFrame(servicos)

# =========================
# ATENDIMENTOS
# =========================

# Lista vazia para armazenar os atendimentos
atendimentos = []

# Loop para criar cada atendimento
for i in range(1, NUM_ATENDIMENTOS + 1):

    # Seleciona um cliente aleatório
    cliente = random.randint(1, NUM_CLIENTES)

    # Seleciona um serviço aleatório
    servico = random.randint(1, len(SERVICOS))

    # Gera data e hora de abertura do atendimento
    abertura = fake.date_time_between(start_date=DATA_INICIO, end_date=DATA_FIM)

    # Define o tempo de atendimento em minutos
    tempo_atendimento = random.randint(10, 300)

    # Calcula a data de fechamento
    fechamento = abertura + timedelta(minutes=tempo_atendimento)

    # Adiciona os dados do atendimento
    atendimentos.append({
        "id_atendimento": i,
        "id_cliente": cliente,
        "id_servico": servico,
        "data_abertura": abertura,
        "data_fechamento": fechamento,
        "tempo_atendimento_min": tempo_atendimento,
        "custo_real": random.uniform(30, 250)
    })

# Converte a lista de atendimentos em DataFrame
df_atendimentos = pd.DataFrame(atendimentos)

# =========================
# NPS
# =========================

# Lista vazia para armazenar avaliações NPS
nps = []

# Seleciona 60% dos atendimentos para gerar NPS
for _, row in df_atendimentos.sample(frac=0.6).iterrows():

    # Gera uma nota NPS com distribuição enviesada
    nota = random.choices(
        list(range(0, 11)),
        weights=[1,1,1,1,2,3,5,8,12,20,30]
    )[0]

    # Adiciona os dados do NPS
    nps.append({
        "id_cliente": row["id_cliente"],
        "id_atendimento": row["id_atendimento"],
        "nota_nps": nota,
        "data_pesquisa": row["data_fechamento"] + timedelta(days=1)
    })

# Converte a lista de NPS em DataFrame
df_nps = pd.DataFrame(nps)

# =========================
# SALVAR ARQUIVOS
# =========================

# Salva os dados de clientes em CSV
df_clientes.to_csv("data/raw/clientes.csv", index=False)

# Salva os dados de serviços em CSV
df_servicos.to_csv("data/raw/servicos.csv", index=False)

# Salva os dados de atendimentos em CSV
df_atendimentos.to_csv("data/raw/atendimentos.csv", index=False)

# Salva os dados de NPS em CSV
df_nps.to_csv("data/raw/nps.csv", index=False)

# Exibe mensagem de sucesso
print("Dados fictícios gerados com sucesso!")
