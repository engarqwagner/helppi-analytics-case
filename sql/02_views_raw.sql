-- VIEWS RAW (INTERMEDIÁRIAS)
-- NPS médio simples por categoria (RAW)
CREATE OR REPLACE VIEW vw_nps_medio_por_categoria_servico_raw AS
SELECT
    categoria AS categoria_servico,
    AVG(nota_nps) AS nota_media_nps
FROM fato_nps
GROUP BY categoria;

-- SLA médio simples por categoria (RAW)
CREATE OR REPLACE VIEW vw_sla_medio_por_categoria_servico_raw AS
SELECT
    categoria AS categoria_servico,
    AVG(sla_real_min) AS tempo_medio_atendimento_minutos
FROM fato_atendimentos
GROUP BY categoria;
