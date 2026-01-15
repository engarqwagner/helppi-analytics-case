-- DIMENSÕES AUXILIARES
-- Dimensão de Categoria de Serviço
-- Normaliza categorias para evitar many-to-many no Power BI
CREATE OR REPLACE VIEW dim_categoria_servico AS
SELECT DISTINCT
    categoria AS categoria_servico
FROM dim_servicos;