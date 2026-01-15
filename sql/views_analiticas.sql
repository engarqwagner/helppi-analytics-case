--- Receita por plano
CREATE VIEW vw_receita_por_plano as
select
    plano,
    COUNT(DISTINCT id_cliente) AS total_clientes,
    sum(valor_mensal) AS receita_mensal
FROM dim_clientes
where status = 'Ativo'
GROUP BY plano;

--- SLA medio por serviço
CREATE VIEW vw_sla_servico AS
select
    categoria,
    AVG(sla_real_min) AS sla_medio_min
FROM fato_atendimentos
GROUP BY categoria;

--- NPS medio por serviço
CREATE VIEW vw_nps_servico AS
select
    categoria,
    AVG(nota_nps) AS nps_medio
FROM fato_nps
GROUP BY categoria;


