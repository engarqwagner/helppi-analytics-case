
-- VIEWS ANALÍTICAS FINAIS
-- 1. NPS oficial por categoria de serviço
CREATE OR REPLACE VIEW vw_nps_oficial_por_categoria_servico AS
SELECT
    categoria AS categoria_servico,
    COUNT(*) AS quantidade_total_respostas,
    SUM(CASE WHEN nota_nps >= 9 THEN 1 ELSE 0 END) AS quantidade_promotores,
    SUM(CASE WHEN nota_nps <= 6 THEN 1 ELSE 0 END) AS quantidade_detratores,
    ROUND(
        (
            SUM(CASE WHEN nota_nps >= 9 THEN 1 ELSE 0 END)
            - SUM(CASE WHEN nota_nps <= 6 THEN 1 ELSE 0 END)
        ) / COUNT(*) * 100,
        2
    ) AS score_nps
FROM fato_nps
GROUP BY categoria;


-- 2. Percentual de SLA cumprido por serviço
CREATE OR REPLACE VIEW vw_percentual_sla_cumprido_por_servico AS
SELECT
    ds.id_servico,
    ds.nome_servico,
    COUNT(*) AS quantidade_total_atendimentos,
    SUM(CASE WHEN fa.sla_real_min <= 60 THEN 1 ELSE 0 END) AS quantidade_atendimentos_dentro_sla,
    ROUND(
        SUM(CASE WHEN fa.sla_real_min <= 60 THEN 1 ELSE 0 END) / COUNT(*) * 100,
        2
    ) AS percentual_sla_cumprido
FROM fato_atendimentos fa
JOIN dim_servicos ds
    ON fa.id_servico = ds.id_servico
GROUP BY ds.id_servico, ds.nome_servico;


-- 3. Receita mensal por plano (clientes ativos)
CREATE OR REPLACE VIEW vw_receita_mensal_por_plano_clientes_ativos AS
SELECT
    plano AS nome_plano,
    COUNT(DISTINCT id_cliente) AS quantidade_clientes_ativos,
    SUM(valor_mensal) AS valor_total_receita_mensal
FROM dim_clientes
WHERE status = 'Ativo'
GROUP BY plano;


-- 4. Receita por serviço ao longo do tempo
CREATE OR REPLACE VIEW vw_receita_servicos_por_data AS
SELECT
    fa.data_abertura AS data_atendimento,
    ds.id_servico,
    ds.nome_servico,
    SUM(fa.custo_real) AS valor_total_receita
FROM fato_atendimentos fa
JOIN dim_servicos ds
    ON fa.id_servico = ds.id_servico
GROUP BY fa.data_abertura, ds.id_servico, ds.nome_servico;


-- 5. Volume de atendimentos por serviço e data
CREATE OR REPLACE VIEW vw_volume_atendimentos_por_servico_por_data AS
SELECT
    fa.data_abertura AS data_atendimento,
    ds.id_servico,
    ds.nome_servico,
    COUNT(*) AS quantidade_atendimentos
FROM fato_atendimentos fa
JOIN dim_servicos ds
    ON fa.id_servico = ds.id_servico
GROUP BY fa.data_abertura, ds.id_servico, ds.nome_servico;
