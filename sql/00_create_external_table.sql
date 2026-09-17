CREATE EXTERNAL TABLE credit_analytics.credit_portfolio (
    referencia TIMESTAMP,
    numero_conta STRING,
    cpf STRING,
    fx_valor STRING,
    saldo DOUBLE,
    saldo_pdd DOUBLE,
    atraso INT,
    fx_atraso STRING,
    data_inicio_atraso TIMESTAMP,
    ultimo_dia TIMESTAMP,
    flag_post STRING,
    uni_cob STRING,
    risco STRING,
    fpd STRING,
    code_bloq STRING,
    cliente_uf STRING,
    parceiro STRING,
    recuperado STRING,
    dia_recuperacao INT,
    transitoria STRING,
    campanha STRING,
    cessao STRING,
    bandeira STRING,
    tipo_endividamento STRING,
    canal STRING
)
STORED AS PARQUET
LOCATION 's3://joao-torre-credit-analytics-2026/data/credit_portfolio/';