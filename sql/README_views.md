# Views Analíticas — Helppi Analytics Case

## Visão Geral
As views SQL foram organizadas em três camadas:

1. Dimensões auxiliares
2. Views RAW (intermediárias)
3. Views analíticas finais (consumidas pelo Power BI)

---

## Dimensões

### dim_categoria_servico
Dimensão criada para normalizar categorias de serviço e evitar relacionamentos many-to-many no Power BI.

---

## Views RAW

### vw_nps_medio_por_categoria_servico_raw
Cálculo simples da média de NPS por categoria, utilizado para validação e entendimento dos dados.

### vw_sla_medio_por_categoria_servico_raw
Cálculo simples do SLA médio por categoria de serviço.

---

## Views Analíticas Finais

### vw_nps_oficial_por_categoria_servico
Implementa a metodologia oficial de NPS:
(score de promotores - score de detratores) / total de respostas.

### vw_percentual_sla_cumprido_por_servico
Calcula o percentual de atendimentos que cumpriram o SLA definido (<= 60 minutos).

### vw_receita_mensal_por_plano_clientes_ativos
Exibe a receita mensal considerando apenas clientes ativos.

### vw_receita_servicos_por_data
Apresenta a receita agregada por serviço ao longo do tempo.

### vw_volume_atendimentos_por_servico_por_data
Mostra o volume de atendimentos por serviço ao longo do tempo.
