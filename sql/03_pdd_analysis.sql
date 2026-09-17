-- PDD Analysis
-- PDD por faixa de risco

SELECT
    risco,
    SUM(saldo) AS saldo_total,
    SUM(saldo_pdd) AS pdd_total,
    ROUND(
        100.0 * SUM(saldo_pdd) / NULLIF(SUM(saldo), 0),
        2
    ) AS pdd_rate
FROM credit_analytics.credit_portfolio
GROUP BY risco
ORDER BY pdd_rate DESC;

--#	risco	saldo_total	pdd_total	pdd_rate
--1	BAIXO	3568531.0199999954	1113077.5300000003	31.19
--2	MEDIO	4192439.279999992	1289958.7599999972	30.77
--3	ALTO	2628232.2800000003	799015.2699999997	30.4
