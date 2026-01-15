Medidas DAX — Helppi Analytics (Power BI)

Este documento descreve todas as medidas DAX criadas no Power BI, detalhando:
- Nome da medida
- Tabela de origem
- Fórmula DAX
- Finalidade no relatório

--------------------------------------

1. Receita Mensal (Clientes Ativos)

Receita Mensal (Clientes Ativos) =
SUM (
    'helppi_analytics vw_receita_mensal_por_plano_clientes_ativos'[valor_total_receita_mensal]
)

Tabela:
- helppi_analytics vw_receita_mensal_por_plano_clientes_ativos

Descrição:
Soma da receita recorrente mensal considerando apenas clientes ativos.

--------------------------------------

2. Total de Clientes Ativos

Total de Clientes Ativos =
SUM (
    'helppi_analytics vw_receita_mensal_por_plano_clientes_ativos'[quantidade_clientes_ativos]
)

Tabela:
- helppi_analytics vw_receita_mensal_por_plano_clientes_ativos

Descrição:
Quantidade total de clientes ativos no período selecionado.

--------------------------------------

3. Ticket Médio Mensal

Ticket Médio Mensal =
DIVIDE (
    [Receita Mensal (Clientes Ativos)],
    [Total de Clientes Ativos]
)

Descrição:
Receita média mensal por cliente ativo.

--------------------------------------

4. Total de Atendimentos

01 - Total Atendimentos =
SUM (
    'helppi_analytics vw_percentual_sla_cumprido_por_servico'[quantidade_total_atendimentos]
)

Tabela:
- helppi_analytics vw_percentual_sla_cumprido_por_servico

Descrição:
Total de atendimentos realizados por serviço.

--------------------------------------

5. Atendimentos Dentro do SLA

02 - Atendimentos Dentro do SLA =
SUM (
    'helppi_analytics vw_percentual_sla_cumprido_por_servico'[quantidade_atendimentos_dentro_sla]
)

Descrição:
Quantidade de atendimentos realizados dentro do SLA.

--------------------------------------

6. Atendimentos Fora do SLA

04 - Atendimentos Fora do SLA =
[01 - Total Atendimentos] - [02 - Atendimentos Dentro do SLA]

Descrição:
Quantidade de atendimentos realizados fora do prazo.

--------------------------------------

7. % Fora do SLA

05 - % Fora do SLA =
DIVIDE (
    [04 - Atendimentos Fora do SLA],
    [01 - Total Atendimentos]
)

Descrição:
Percentual de atendimentos fora do SLA.

--------------------------------------

8. SLA Médio da Operação (%)

SLA Médio da Operação (%) =
AVERAGE (
    'helppi_analytics vw_percentual_sla_cumprido_por_servico'[percentual_sla_cumprido]
)

Descrição:
Média simples do percentual de SLA por serviço.

--------------------------------------

9. Quantidade Total de Serviços Prestados

Qtd. Serviços =
SUM (
    'helppi_analytics vw_volume_atendimentos_por_servico_por_data'[quantidade_atendimentos]
)

Tabela:
- helppi_analytics vw_volume_atendimentos_por_servico_por_data

Descrição:
Total de serviços executados no período selecionado.

--------------------------------------

10. Receita Total por Serviço

Receita Total =
SUM (
    'helppi_analytics vw_receita_servicos_por_data'[valor_total_receita]
)

Tabela:
- helppi_analytics vw_receita_servicos_por_data

Descrição:
Receita operacional associada aos serviços prestados.

--------------------------------------

Observações de Modelagem

- As medidas utilizam views analíticas pré-agregadas no banco.
- Não há tabela calendário dedicada.
- Filtros de data usam hierarquia nativa (Ano/Mês).
- Métricas financeiras, operacionais e de satisfação são mantidas em camadas separadas.
