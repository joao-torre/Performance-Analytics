# Performance Analytics

Projeto de **Data Analytics aplicado a uma carteira de crédito sintética**, utilizando Python, SQL, Amazon S3, Amazon Athena e Power BI.

O objetivo é analisar **carteira, risco, PDD, atraso, recuperação e evolução**.

> Dados 100% sintéticos, desenvolvidos para fins educacionais e de portfólio.

## 🏗️ Arquitetura

```text
Python → Parquet → Amazon S3 → Amazon Athena → Power BI
```

## 📊 Dataset

* 5.000 registros
* 25 variáveis
* Formato Parquet
* Dados sintéticos

Principais informações:

`saldo` · `saldo_pdd` · `atraso` · `risco` · `recuperado` · `canal` · `cliente_uf` · `parceiro`

## ☁️ AWS

**S3:** armazenamento dos dados

**Athena:** consultas SQL

Banco:

`credit_analytics`

Tabela:

`credit_portfolio`

## 📈 Análises

* Portfolio Overview
* Risk Analysis
* Delinquency Analysis
* Recovery Analysis
* Monthly Evolution
* Segmentation

### KPIs atuais

| Indicador    |       Valor |
| ------------ | ----------: |
| Contas       |       5.000 |
| Carteira     | R$ 10,39 mi |
| Ticket médio | R$ 2.077,84 |
| PDD          |  R$ 3,20 mi |

## 📊 Power BI

Dashboard executivo com indicadores de:

**Carteira · Risco · Atraso · PDD · Recuperação · Evolução**

## 📁 Estrutura

```text
Performance-Analytics/
├── data/
├── python/
├── sql/
├── powerbi/
├── screenshots/
├── requirements.txt
├── .gitignore
└── README.md
```

## 🔐 Segurança

Todos os dados são sintéticos. Nenhuma informação real ou confidencial é utilizada.

Credenciais da AWS não devem ser armazenadas no repositório.

## 🛠️ Stack

**Python · Pandas · SQL · Amazon S3 · Amazon Athena · Parquet · Power BI · DAX**
