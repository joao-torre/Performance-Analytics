-- Risk Analysis
-- Distribuição da carteira por risco

SELECT
    risco,
    COUNT(DISTINCT numero_conta) AS total_contas,
    SUM(saldo) AS carteira_total,
    SUM(saldo_pdd) AS pdd_total,
    AVG(saldo) AS ticket_medio
FROM credit_analytics.credit_portfolio
GROUP BY risco
ORDER BY carteira_total DESC;

-- Análise de inadimplência
--#	risco	total_contas	carteira_total	pdd_total	ticket_medio
--1	MEDIO	2001	4192439.279999999	1289958.7600000002	2095.172053973013
--2	BAIXO	1731	3568531.020000001	1113077.5300000005	2061.543050259966
--3	ALTO	1268	2628232.279999998	799015.27	2072.738391167191
