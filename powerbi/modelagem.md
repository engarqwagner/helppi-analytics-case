# Modelagem Power BI — Helppi Analytics

## Tabelas importadas do MySQL
- dim_clientes
- dim_servicos
- dim_categoria_servico
- vw_receita_servicos_por_data
- vw_volume_atendimentos_por_servico_por_data
- vw_percentual_sla_cumprido_por_servico
- vw_nps_oficial_por_categoria_servico
- vw_receita_mensal_por_plano_clientes_ativos

## Papel de cada tabela
- Dimensões:
  - dim_servicos → dimensão principal de serviço
  - dim_categoria_servico → dimensão auxiliar para NPS
  - dim_clientes → dimensão de clientes e planos

- Fatos / Views analíticas:
  - vw_receita_servicos_por_data → receita por serviço e data
  - vw_volume_atendimentos_por_servico_por_data → volume operacional
  - vw_percentual_sla_cumprido_por_servico → SLA operacional
  - vw_nps_oficial_por_categoria_servico → satisfação (NPS)
  - vw_receita_mensal_por_plano_clientes_ativos → receita recorrente

## Relacionamentos principais
- dim_servicos[id_servico] 1:* vw_receita_servicos_por_data[id_servico]
- dim_servicos[id_servico] 1:* vw_volume_atendimentos_por_servico_por_data[id_servico]
- dim_servicos[id_servico] 1:* vw_percentual_sla_cumprido_por_servico[id_servico]

- dim_categoria_servico[categoria_servico] 1:* vw_nps_oficial_por_categoria_servico[categoria_servico]

## Decisões de modelagem
- Não foi utilizada tabela calendário dedicada
- Filtros de data usam hierarquia nativa (Ano / Mês)
- Views já chegam agregadas para performance
- NPS não cruza com serviços individualmente, apenas por categoria
