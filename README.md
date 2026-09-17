# Performance Analytics

**Python · SQL · Amazon S3 · Amazon Athena · Power BI · DAX**

Projeto educacional de **Data Analytics aplicado a uma carteira de crédito**, desenvolvido com dados 100% sintéticos para analisar carteira, risco, PDD, atraso e recuperação ao longo do tempo.

> **Nenhum dado real de clientes, contratos ou empresas é utilizado neste projeto.**

---

## 🔎 Problema

Consolidar e analisar o comportamento de uma carteira de crédito volume, risco, provisão (PDD), atraso e recuperação, por meio de um pipeline de dados em nuvem, culminando em um dashboard executivo para análise dos principais indicadores.

---

## 🔄 Pipeline

```text
Synthetic Data
      ↓
Python (Pandas)
      ↓
Parquet
      ↓
Amazon S3
      ↓
Amazon Athena
      ↓
Power BI
```

---

## 📊 Dataset

A base utilizada no projeto é totalmente sintética e foi gerada em Python.

| Item      |   Valor |
| --------- | ------: |
| Registros |   5.000 |
| Variáveis |      25 |
| Formato   | Parquet |

Principais variáveis:

`saldo` · `saldo_pdd` · `atraso` · `risco` · `recuperado` · `canal` · `cliente_uf` · `parceiro`

---

## 📊 Principais Indicadores

Os principais indicadores calculados sobre a base sintética são:

| Indicador    |       Valor |
| ------------ | ----------: |
| Contas       |       5.000 |
| Carteira     | R$ 10,39 mi |
| Ticket médio | R$ 2.077,84 |
| PDD          |  R$ 3,20 mi |

> Os valores apresentados acima são referentes exclusivamente à base sintética utilizada no projeto.

---

## ☁️ AWS

O projeto utiliza uma arquitetura baseada em armazenamento e consulta de dados na AWS:

* **Amazon S3** — armazenamento dos dados em formato Parquet.
* **Amazon Athena** — consultas SQL diretamente sobre os dados armazenados no S3.

| Recurso | Nome               |
| ------- | ------------------ |
| Banco   | `credit_analytics` |
| Tabela  | `credit_portfolio` |

A infraestrutura é apresentada como parte da arquitetura demonstrativa do projeto. Não são armazenadas credenciais ou informações reais de acesso à AWS no repositório.

---

## 🧮 SQL Analytics

As consultas SQL foram desenvolvidas para análise da carteira armazenada no S3 e são compatíveis com o **Amazon Athena**.

As queries estão organizadas na pasta `sql/`:

| Arquivo                         | Descrição                                |
| ------------------------------- | ---------------------------------------- |
| `00_create_external_table.sql`  | Criação da tabela externa no Athena      |
| `01_portfolio_overview.sql`     | Indicadores gerais da carteira           |
| `02_risk_analysis.sql`          | Distribuição por nível de risco          |
| `03_pdd_analysis.sql`           | PDD por nível de risco                   |
| `04_delinquency_analysis.sql`   | Análise por faixa de atraso              |
| `05_recovery_analysis.sql`      | Recuperação por canal                    |
| `06_segmentation_analysis.sql`  | Segmentação por estado, parceiro e canal |
| `07_concentration_analysis.sql` | Concentração nas maiores contas          |
| `08_temporal_analysis.sql`      | Evolução mensal da carteira              |

### Exemplos de consultas

**Indicadores gerais:**

```sql
SELECT
    COUNT(DISTINCT numero_conta) AS quantidade_contas,
    SUM(saldo) AS carteira_total,
    SUM(saldo_pdd) AS pdd_total,
    AVG(saldo) AS ticket_medio,
    SUM(saldo_pdd) / NULLIF(SUM(saldo), 0) AS pdd_rate
FROM credit_analytics.credit_portfolio;
```

**Análise por risco:**

```sql
SELECT
    risco,
    COUNT(DISTINCT numero_conta) AS quantidade_contas,
    SUM(saldo) AS carteira_total,
    SUM(saldo_pdd) AS pdd_total
FROM credit_analytics.credit_portfolio
GROUP BY risco
ORDER BY carteira_total DESC;
```

**Evolução mensal:**

```sql
SELECT
    date_trunc('month', referencia) AS mes_referencia,
    COUNT(DISTINCT numero_conta) AS quantidade_contas,
    SUM(saldo) AS carteira_total,
    SUM(saldo_pdd) AS pdd_total
FROM credit_analytics.credit_portfolio
GROUP BY date_trunc('month', referencia)
ORDER BY mes_referencia;
```

As consultas apoiam as análises de **carteira, risco, PDD, atraso, recuperação, concentração, segmentação e evolução temporal** utilizadas no projeto.

---

## 📸 Dashboard

### Eficiência de Saldo

Evolução do saldo de cura por dia e comparativo entre períodos.

![Eficiência de Saldo](screenshots/eficiencia_saldo.png)

### Eficiência de Distribuição

Distribuição percentual da cura por canal e representatividade do saldo.

![Eficiência de Distribuição](screenshots/eficiencia_distribuicao.png)

### Histórico de Cura

Evolução do percentual de cura por faixa de atraso ao longo dos meses.

![Histórico de Cura](screenshots/historico_cura.png)

---

## 🧠 Análises

O dashboard contempla diferentes perspectivas analíticas:

* **Eficiência de Saldo** — saldo da carteira, saldo de cura e saldo remanescente por período.
* **Eficiência de Distribuição** — distribuição do percentual de cura por canal.
* **Histórico de Cura** — evolução do percentual de cura por faixa de atraso (`FX_ATRASO`).
* **Segmentação** — análise por FPD, campanha, canal, parceiro, bandeira, risco e unidade de cobrança.
* **Análise temporal** — evolução dos principais indicadores ao longo dos períodos.
* **Análise de risco** — distribuição da carteira e PDD por nível de risco.

---

## 📈 Power BI

Dashboard desenvolvido no **Power BI** para acompanhamento dos principais indicadores de:

**Carteira · Risco · Atraso · PDD · Recuperação · Evolução**

O modelo utiliza medidas **DAX** sobre uma base consolidada, incluindo tratamentos para valores repetidos com `AVERAGEX` e lógica de truncamento da série no mês corrente.

O arquivo `.pbix` está disponível em:

```text
Powerbi/Eficiencia.pbix
```

---

## 🗂️ Estrutura do Projeto

```text
Performance-Analytics/
├── data/
│   └── BASE_ANALYTICS_MOCK.parquet
├── Notebooks/
│   └── Base_Analytics.ipynb
├── src/
│   └── data_generator.py
├── sql/
│   ├── 00_create_external_table.sql
│   ├── 01_portfolio_overview.sql
│   ├── 02_risk_analysis.sql
│   ├── 03_pdd_analysis.sql
│   ├── 04_delinquency_analysis.sql
│   ├── 05_recovery_analysis.sql
│   ├── 06_segmentation_analysis.sql
│   ├── 07_concentration_analysis.sql
│   └── 08_temporal_analysis.sql
├── Powerbi/
│   └── Eficiencia.pbix
├── screenshots/
│   ├── eficiencia_saldo.png
│   ├── eficiencia_distribuicao.png
│   └── historico_cura.png
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🚀 Execução

Clone o repositório e crie um ambiente virtual:

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Instalação das dependências

```bash
pip install -r requirements.txt
```

### Geração da base sintética

```bash
python src/data_generator.py
```

### Validação dos dados

Abra o notebook:

```text
Notebooks/Base_Analytics.ipynb
```

ou execute:

```bash
jupyter notebook Notebooks/Base_Analytics.ipynb
```

### Power BI

Abra o arquivo:

```text
Powerbi/Eficiencia.pbix
```

no **Power BI Desktop**.

---

## 🛠️ Stack

### Tecnologias

**Python · Pandas · SQL · Amazon S3 · Amazon Athena · Parquet · Power BI · DAX**

### Conceitos

**Data Analytics · Credit Analytics · Cloud Data Pipeline · Risk Analysis · Delinquency Analysis · Recovery Analysis · Business Intelligence · Data Segmentation · Temporal Analysis**

---

## 🔐 Segurança e Privacidade

* Todos os dados utilizados no projeto são sintéticos.
* Nenhuma informação real ou confidencial de clientes, contratos ou empresas é utilizada.
* Nenhuma credencial da AWS é armazenada no repositório.
* Variáveis e identificadores utilizados no projeto são exclusivamente para fins educacionais e demonstrativos.

---

## ⚠️ Limitações

* Os dados são totalmente sintéticos e não representam uma carteira real.
* Os indicadores e resultados não devem ser interpretados como metodologia regulatória ou contábil.
* O projeto não contempla modelos preditivos de crédito.
* O projeto não contempla estratégias reais de cobrança ou decisão de crédito.
* A arquitetura AWS apresentada possui finalidade demonstrativa.

---

## 📌 Objetivo

Demonstrar, de ponta a ponta, a construção de um fluxo de **Data Analytics aplicado a crédito**, desde a geração e preparação dos dados até sua exploração analítica e visualização:

```text
Data Generation
      ↓
Data Processing
      ↓
Parquet
      ↓
Cloud Storage
      ↓
SQL Analytics
      ↓
Business Metrics
      ↓
Segmentation
      ↓
Temporal Analysis
      ↓
Power BI
      ↓
Business Insights
```

> **Projeto educacional desenvolvido exclusivamente com dados sintéticos, com foco em demonstrar competências técnicas em Data Analytics, SQL, Cloud e Business Intelligence.**
