-- Temporal Analysis
-- Evolução mensal da carteira

SELECT
    date_trunc('month', referencia) AS mes,
    COUNT(DISTINCT numero_conta) AS total_contas,
    SUM(saldo) AS carteira_total,
    SUM(saldo_pdd) AS pdd_total,
    AVG(atraso) AS atraso_medio
FROM credit_analytics.credit_portfolio
GROUP BY date_trunc('month', referencia)
ORDER BY mes;

--#	mes	total_contas	carteira_total	pdd_total	atraso_medio
--1	2026-01-01 00:00:00.000	733	1487850.6399999997	464597.85	201.47339699863574
--2	2026-02-01 00:00:00.000	703	1384401.81	428175.2900000001	211.2660028449502
--3	2026-03-01 00:00:00.000	687	1358393.1800000002	406664.4	197.95487627365355
--4	2026-04-01 00:00:00.₀₀₀	719	1573₀₁₄.8₀₀₀₀₀₀₃	48₀₅₄₇.₀₆₉₉₉₉₉₉₅	2₁₀.7997₂₁₈₃₅₈₈₃₁₆
--5	2０２６-０５-０１ ００:００:００.０００	６８７	１４８８４３０.４３	４８１８３８.２０９９９９９９９９６	２２３.５２９８３９８８３５５１７
--６	２０２６-０６-０１ ００:００:００.０００	７４０	１５７８７９６.８３９９９９９９９９	４６９９１６.４６９９９９９９９８６	２０３.５４₀５４₀５４₀５４₀５５
--7	2026-07-01 00:00:00.000	731	1518314.88	470312.27	205.99179206566347
