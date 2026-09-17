-- Concentration Analysis
-- Participação das maiores contas na carteira

WITH carteira AS (
    SELECT
        SUM(saldo) AS carteira_total
    FROM credit_analytics.credit_portfolio
),

contas AS (
    SELECT
        numero_conta,
        SUM(saldo) AS saldo_conta
    FROM credit_analytics.credit_portfolio
    GROUP BY numero_conta
)

SELECT
    numero_conta,
    saldo_conta,
    ROUND(
        100.0 * saldo_conta / carteira_total,
        2
    ) AS participacao_carteira

FROM contas
CROSS JOIN carteira
ORDER BY saldo_conta DESC
LIMIT 20;

--#	numero_conta	saldo_conta	participacao_carteira
--1	CONTA_00001341	26620.62	0.26
--2	CONTA_00002262	26501.5	0.26
--3	CONTA_00002528	24947.73	0.24
--4	CONTA_00000633	24836.48	0.24
--5	CONTA_00002824	23597.88	0.23
--6	CONTA_00003042	22546.8	0.22
--7	CONTA_00004090	21709.42	0.21
--8	CONTA_00004716	21311.98	0.21
--9	CONTA_00002876	21205.46	0.2
--10	CONTA_00003161	20888.12	0.2
--11	CONTA_00004618	20747.21	0.2
--12	CONTA_00001842	20629.79	0.2
--13	CONTA_00004631	19328.28	0.19
--14	CONTA_00001398	19311.69	₀.₁₉
--15	CONTA_₀₀₀₀₃₄₄₆	₁₈₄₃₇.₀₂	₀.₁₈
--16	CONTA_₀₀₀₀₀₁₈₀	₁₈₂₆₇.₂	₀.₁₈
--17	CONTA_00002938	16789.36	0.16
--18	CONTA_00002428	16636.25	0.16
--19	CONTA_00001423	16095.95	0.15
--20	CONTA_00000160	15784.36	0.15
