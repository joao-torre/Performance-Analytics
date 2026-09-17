"""
============================================================
GERADOR DE BASE ANALYTICS — DADOS 100% SINTÉTICOS
============================================================

Objetivo:
    Criar uma base fictícia para demonstração de projetos
    de Data Analytics, SQL e Power BI.
"""

from pathlib import Path
import numpy as np
import pandas as pd

# ============================================================
# CONFIGURAÇÕES
# ============================================================

SEED = 2026
QTD_REGISTROS = 5000
np.random.seed(SEED)

# Estrutura do projeto:
#
# projeto/
# ├── data/
# │   ├── BASE_ANALYTICS_MOCK.xlsx
# │   └── BASE_ANALYTICS_MOCK.parquet
# └── src/
#     └── data_generator.py

PASTA_PROJETO = Path(__file__).resolve().parents[1]
PASTA_DATA = PASTA_PROJETO / "data"

PASTA_DATA.mkdir(parents=True, exist_ok=True)

ARQUIVO_PARQUET = PASTA_DATA / "BASE_ANALYTICS_MOCK.parquet"

# ============================================================
# COLUNAS PÚBLICAS
# ============================================================

COLUNAS = [
    "REFERENCIA",
    "NUMERO_CONTA",
    "CPF",
    "FX_VALOR",
    "SALDO",
    "SALDO_PDD",
    "ATRASO",
    "FX_ATRASO",
    "DATA_INICIO_ATRASO",
    "ULTIMO_DIA",
    "FLAG_POST",
    "UNI_COB",
    "RISCO",
    "FPD",
    "CODE_BLOQ",
    "CLIENTE_UF",
    "PARCEIRO",
    "RECUPERADO",
    "DIA_RECUPERACAO",
    "TRANSITORIA",
    "CAMPANHA",
    "CESSAO",
    "BANDEIRA",
    "TIPO_ENDIVIDAMENTO",
    "CANAL"
]

# ============================================================
# DOMÍNIOS 100% FICTÍCIOS
# ============================================================
# Estados são mantidos apenas como dimensão geográfica
# genérica. Nenhuma informação de cliente é utilizada.

ESTADOS = [
    "SP",
    "RJ",
    "MG",
    "PR",
    "SC",
    "RS",
    "ES",
    "BA",
    "GO",
    "PE",
    "CE",
    "DF"
]
# Nomes completamente fictícios.
UNIDADES = [
    "UNIDADE_A",
    "UNIDADE_B",
    "UNIDADE_C",
    "UNIDADE_D",
    "UNIDADE_E"
]
PARCEIROS = [
    "PARCEIRO_01",
    "PARCEIRO_02",
    "PARCEIRO_03",
    "PARCEIRO_04",
    "PARCEIRO_05",
    "PARCEIRO_06"
]
CANAIS = [
    "CANAL_A",
    "CANAL_B",
    "CANAL_C",
    "CANAL_D",
    "CANAL_E"
]
BANDEIRAS = [
    "BANDEIRA_A",
    "BANDEIRA_B"
]
TIPOS_ENDIVIDAMENTO = [
    "TIPO_A",
    "TIPO_B",
    "TIPO_C",
    "TIPO_D"
]
CODIGOS_BLOQUEIO = [
    "COD_01",
    "COD_02",
    "COD_03",
    "COD_04"
]
CAMPANHAS = [
    "CAMP_001",
    "CAMP_002",
    "CAMP_003",
    "CAMP_004",
    "CAMP_005",
    "CAMP_006"
]
RISCOS = [
    "BAIXO",
    "MEDIO",
    "ALTO"
]

# ============================================================
# REFERÊNCIAS MENSAIS
# ============================================================

REFERENCIAS = pd.to_datetime([
    "2026-01-31",
    "2026-02-28",
    "2026-03-31",
    "2026-04-30",
    "2026-05-31",
    "2026-06-30",
    "2026-07-31"
])
referencia = np.random.choice(
    REFERENCIAS,
    size=QTD_REGISTROS
)

# ============================================================
# IDENTIFICADORES FICTÍCIOS
# ============================================================

numero_conta = [
    f"CONTA_{i:08d}"
    for i in range(1, QTD_REGISTROS + 1)
]
cpf = [
    f"CLIENTE_{i:08d}"
    for i in range(1, QTD_REGISTROS + 1)
]

# ============================================================
# SALDO
# ============================================================

saldo = np.random.lognormal(
    mean=7.2,
    sigma=0.95,
    size=QTD_REGISTROS
)
saldo = np.round(
    np.clip(
        saldo,
        100,
        30000
    ),
    2
)

# ============================================================
# FAIXA DE VALOR
# ============================================================

def classificar_faixa_valor(valor):
    if valor <= 500:
        return "FAIXA_01"
    if valor <= 1000:
        return "FAIXA_02"
    if valor <= 2500:
        return "FAIXA_03"
    if valor <= 5000:
        return "FAIXA_04"
    if valor <= 10000:
        return "FAIXA_05"
    return "FAIXA_06"

fx_valor = [
    classificar_faixa_valor(valor)
    for valor in saldo
]

# ============================================================
# ATRASO
# ============================================================

atraso = np.random.choice(
    [
        5,
        10,
        15,
        20,
        30,
        45,
        60,
        75,
        90,
        120,
        150,
        180,
        240,
        300,
        360,
        450,
        510,
        600,
        720
    ],
    size=QTD_REGISTROS
)

# ============================================================
# FAIXA DE ATRASO
# ============================================================

def classificar_faixa_atraso(dias):
    if dias <= 30:
        return "FAIXA_ATRASO_01"
    if dias <= 60:
        return "FAIXA_ATRASO_02"
    if dias <= 90:
        return "FAIXA_ATRASO_03"
    if dias <= 120:
        return "FAIXA_ATRASO_04"
    if dias <= 180:
        return "FAIXA_ATRASO_05"
    if dias <= 360:
        return "FAIXA_ATRASO_06"
    if dias <= 510:
        return "FAIXA_ATRASO_07"
    return "FAIXA_ATRASO_08"

fx_atraso = [
    classificar_faixa_atraso(dias)
    for dias in atraso
]

# ============================================================
# DATA DE INÍCIO DO ATRASO
# ============================================================

data_inicio_atraso = (
    pd.to_datetime(referencia)
    - pd.to_timedelta(
        atraso,
        unit="D"
    )
)

# ============================================================
# ÚLTIMO DIA
# ============================================================

ultimo_dia = (
    pd.to_datetime(referencia)
    + pd.to_timedelta(
        np.random.randint(
            1,
            15,
            QTD_REGISTROS
        ),
        unit="D"
    )
)

# ============================================================
# FLAG POST
# ============================================================

flag_post = np.random.choice(
    [
        "SIM",
        "NAO"
    ],
    size=QTD_REGISTROS,
    p=[
        0.20,
        0.80
    ]
)

# ============================================================
# UNIDADE DE COBRANÇA
# ============================================================

uni_cob = np.random.choice(
    UNIDADES,
    size=QTD_REGISTROS
)

# ============================================================
# RISCO
# ============================================================

risco = np.random.choice(
    RISCOS,
    size=QTD_REGISTROS,
    p=[
        0.35,
        0.40,
        0.25
    ]
)

# ============================================================
# FPD
# ============================================================

fpd = np.random.choice(
    [
        "SIM",
        "NAO"
    ],
    size=QTD_REGISTROS,
    p=[
        0.12,
        0.88
    ]
)

# ============================================================
# CÓDIGO DE BLOQUEIO
# ============================================================

code_bloq = np.random.choice(
    CODIGOS_BLOQUEIO,
    size=QTD_REGISTROS
)

# ============================================================
# ESTADO
# ============================================================

cliente_uf = np.random.choice(
    ESTADOS,
    size=QTD_REGISTROS
)

# ============================================================
# PARCEIRO
# ============================================================

parceiro = np.random.choice(
    PARCEIROS,
    size=QTD_REGISTROS
)

# ============================================================
# RECUPERAÇÃO
# ============================================================

recuperado = np.random.choice(
    [
        "SIM",
        "NAO"
    ],
    size=QTD_REGISTROS,
    p=[
        0.40,
        0.60
    ]
)

# ============================================================
# DIA DA RECUPERAÇÃO
# ============================================================

dia_recuperacao = np.where(
    recuperado == "SIM",
    np.random.randint(
        1,
        32,
        QTD_REGISTROS
    ),
    np.nan
)

# ============================================================
# TRANSITÓRIA
# ============================================================

transitoria = np.random.choice(
    [
        "SIM",
        "NAO"
    ],
    size=QTD_REGISTROS,
    p=[
        0.10,
        0.90
    ]
)

# ============================================================
# CAMPANHA
# ============================================================

campanha = np.random.choice(
    [
        *CAMPANHAS,
        None
    ],
    size=QTD_REGISTROS,
    p=[
        0.12,
        0.12,
        0.12,
        0.12,
        0.12,
        0.10,
        0.30
    ]
)

# ============================================================
# CESSÃO
# ============================================================

cessao = np.random.choice(
    [
        "SIM",
        "NAO"
    ],
    size=QTD_REGISTROS,
    p=[
        0.08,
        0.92
    ]
)

# ============================================================
# BANDEIRA
# ============================================================

bandeira = np.random.choice(
    BANDEIRAS,
    size=QTD_REGISTROS
)

# ============================================================
# TIPO DE ENDIVIDAMENTO
# ============================================================

tipo_endividamento = np.random.choice(
    TIPOS_ENDIVIDAMENTO,
    size=QTD_REGISTROS
)

# ============================================================
# CANAL
# ============================================================

canal = np.random.choice(
    CANAIS,
    size=QTD_REGISTROS
)

# ============================================================
# PDD
# ============================================================

percentual_pdd = np.select(
    [
        atraso <= 30,
        atraso <= 60,
        atraso <= 90,
        atraso <= 180,
        atraso <= 360,
        atraso > 360
    ],
    [
        0.02,
        0.05,
        0.10,
        0.25,
        0.50,
        0.80
    ]
)
saldo_pdd = np.round(
    saldo * percentual_pdd,
    2
)

# ============================================================
# DATAFRAME FINAL
# ============================================================

df = pd.DataFrame({

    "REFERENCIA": referencia,
    "NUMERO_CONTA": numero_conta,
    "CPF": cpf,
    "FX_VALOR": fx_valor,
    "SALDO": saldo,
    "SALDO_PDD": saldo_pdd,
    "ATRASO": atraso,
    "FX_ATRASO": fx_atraso,
    "DATA_INICIO_ATRASO": data_inicio_atraso,
    "ULTIMO_DIA": ultimo_dia,
    "FLAG_POST": flag_post,
    "UNI_COB": uni_cob,
    "RISCO": risco,
    "FPD": fpd,
    "CODE_BLOQ": code_bloq,
    "CLIENTE_UF": cliente_uf,
    "PARCEIRO": parceiro,
    "RECUPERADO": recuperado,
    "DIA_RECUPERACAO": dia_recuperacao,
    "TRANSITORIA": transitoria,
    "CAMPANHA": campanha,
    "CESSAO": cessao,
    "BANDEIRA": bandeira,
    "TIPO_ENDIVIDAMENTO": tipo_endividamento,
    "CANAL": canal
})

# ============================================================
# AJUSTES DE TIPOS
# ============================================================

df["REFERENCIA"] = pd.to_datetime(
    df["REFERENCIA"]
)
df["DATA_INICIO_ATRASO"] = pd.to_datetime(
    df["DATA_INICIO_ATRASO"]
)
df["ULTIMO_DIA"] = pd.to_datetime(
    df["ULTIMO_DIA"]
)
df["SALDO"] = df["SALDO"].round(2)
df["SALDO_PDD"] = df["SALDO_PDD"].round(2)

# ============================================================
# ORDENAÇÃO
# ============================================================

df = df.sort_values(
    [
        "REFERENCIA",
        "NUMERO_CONTA"
    ]
).reset_index(drop=True)

# ============================================================
# VALIDAÇÕES
# ============================================================

assert len(df) == QTD_REGISTROS
assert len(df.columns) == 25
assert list(df.columns) == COLUNAS
assert df["NUMERO_CONTA"].is_unique
assert df["CPF"].is_unique
assert df["SALDO"].ge(0).all()
assert df["SALDO_PDD"].ge(0).all()
assert df["ATRASO"].ge(0).all()
assert (
    df.loc[
        df["RECUPERADO"] == "SIM",
        "DIA_RECUPERACAO"
    ].notna().all()
)

# ============================================================
# EXPORTAÇÃO
# ============================================================


df.to_parquet(
    ARQUIVO_PARQUET,
    index=False,
    engine="pyarrow"
)
# ============================================================
# RESUMO
# ============================================================

print()
print("=" * 65)
print("BASE ANALYTICS — DADOS SINTÉTICOS")
print("=" * 65)

print(f"Registros gerados : {len(df):,}")
print(f"Colunas           : {len(df.columns)}")
print()
print("Validações concluídas:")
print("  ✓ 25 colunas")
print("  ✓ Dados 100% sintéticos")
print("  ✓ Identificadores fictícios")
print("  ✓ Categorias fictícias")
print("  ✓ Sem conexão Oracle")
print("  ✓ Sem leitura de arquivo externo")
print("  ✓ Sem dados corporativos")
print("  ✓ Contas únicas")
print("  ✓ CPFs fictícios e únicos")

print()
print("Base criada com sucesso.")
print("=" * 65)

print(f"Parquet gerado : {ARQUIVO_PARQUET}")
