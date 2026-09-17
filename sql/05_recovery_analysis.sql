-- Recovery Analysis
-- Recuperação por canal

SELECT
    canal,
    COUNT(DISTINCT numero_conta) AS total_contas,
    SUM(saldo) AS saldo_total,

    SUM(
        CASE
            WHEN recuperado = 'SIM' THEN saldo
            ELSE 0
        END
    ) AS saldo_recuperado,

    ROUND(
        100.0 *
        SUM(
            CASE
                WHEN recuperado = 'SIM' THEN saldo
                ELSE 0
            END
        ) / NULLIF(SUM(saldo), 0),
        2
    ) AS recovery_rate

FROM credit_analytics.credit_portfolio
GROUP BY canal
ORDER BY recovery_rate DESC;

--#	canal	total_contas	saldo_total	saldo_recuperado	recovery_rate
--1	CANAL_D	992	2030460.8700000006	857857.56	42.25
--2	CANAL_B	999	2113451.56	864001.15	40.88
--3	CANAL_A	1012	2126637.1300000004	863445.3899999999	40.6
--4	CANAL_C	993	2117478.7600000007	856206.0700000001	40.44
--5	CANAL_E	1004	2001174.2599999995	774673.7999999998	38.71
