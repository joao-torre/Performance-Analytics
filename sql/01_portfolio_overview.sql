-- Portfolio Overview
-- Indicadores gerais da carteira

SELECT
    COUNT(DISTINCT numero_conta) AS total_contas,
    SUM(saldo) AS carteira_total,
    SUM(saldo_pdd) AS pdd_total,
    AVG(saldo) AS ticket_medio,
    ROUND(
        100.0 * SUM(saldo_pdd) / NULLIF(SUM(saldo), 0),
        2
    ) AS pdd_rate
FROM credit_analytics.credit_portfolio;

--RESULTADO:
-- total_contas | carteira_total | pdd_total | ticket_medio | pdd_rate
--5000 | 1.0389202579999987E7 | 3202051.5600000015 | 2077.8405159999975 | 30.82