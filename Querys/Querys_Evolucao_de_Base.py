from datetime import date
from Consultas.Get_Date import Get_Date


class Querys_Evolucao_de_Base_MK:

    def __init__(self):
        # -----------------------------------------------------
        # Config Periodo de Consultas
        self.dates_ = Get_Date(type_date=1)
        # -----------------------------------------------------

    def evolucao_contratos_cancelados_por_cidades(self):

        # Variaveis
        # -------------------------
        complete_query = ''
        # -------------------------

        # Data Fixa
        # -----------------------------
        data_fixa = str(date(2010, 1, 1).strftime(self.dates_.style_date))
        # -----------------------------

        for x in range(self.dates_.range_meses):

            # Variaveis
            # --------------------------------------------------
            inicio, final, periodo = self.dates_.dates_personalizadas(x)
            # --------------------------------------------------

            simple_query = '''

SELECT
    CASE 
        WHEN (contratos.adesao BETWEEN '{}' AND '{}') THEN TO_DATE('{}', 'MM/YYYY') END AS adesao,
    CASE 
        WHEN (upper(cidade.cidade) LIKE '%PATR%')   THEN 'PATROCINIO'
        WHEN (upper(cidade.cidade) LIKE '%PATO%')   THEN 'PATOS DE MINAS'
        WHEN (upper(cidade.cidade) LIKE '%GUIM%')   THEN 'GUIMARANIA'
        WHEN (upper(cidade.cidade) LIKE '%ABAD%')   THEN 'ABADIA DOS DOURADOS'
        WHEN (upper(cidade.cidade) LIKE '%IRA%')    THEN 'IRAI DE MINAS'
        WHEN (upper(cidade.cidade) LIKE '%CRUZ%')   THEN 'CRUZEIRO DA FORTALEZA'
        WHEN (upper(cidade.cidade) LIKE '%VARJ%')   THEN 'VARJAO DE MINAS'
        WHEN (upper(cidade.cidade) LIKE '%OLEG%')   THEN 'PRESIDENTE OLEGARIO'
        WHEN (upper(cidade.cidade) LIKE '%MARIAS%') THEN 'TRES MARIAS'
        WHEN (upper(cidade.cidade) LIKE '%JOAO%')   THEN 'JOAO PINHEIRO'
        WHEN (upper(cidade.cidade) LIKE '%LAGOA%')  THEN 'LAGOA FORMOSA'
        ELSE 'OUTROS'
    END AS cidade,
    COUNT(contratos.codcontrato) AS contratos_cancelados

FROM 
    public.mk_contratos contratos
    INNER JOIN public.mk_pessoas pessoa ON (contratos.cliente = pessoa.codpessoa)
    INNER JOIN public.mk_cidades cidade ON (pessoa.codcidade = cidade.codcidade)

WHERE 
    contratos.cancelado = 'S'
    AND contratos.dt_cancelamento BETWEEN '{}' AND '{}'

GROUP BY 1,2

            '''.format(
            # -----------------
            data_fixa,
            final,
            periodo,
            data_fixa,
            final
            # -----------------
            )

            if x != (self.dates_.range_meses - 1):
                complete_query = complete_query + simple_query + '''
UNION
'''
            else:
                complete_query = complete_query + simple_query + '''
ORDER BY 2 ASC, 1 ASC;
'''

        return str(complete_query)

    def evolucao_contratos_criados_por_cidades(self):

        # Variaveis
        # -------------------------
        complete_query = ''
        # -------------------------

        # Data Fixa
        # -----------------------------
        data_fixa = str(date(2010, 1, 1).strftime(self.dates_.style_date))
        # -----------------------------

        for x in range(self.dates_.range_meses):

            # Variaveis
            # --------------------------------------------------
            inicio, final, periodo = self.dates_.dates_personalizadas(x)
            # --------------------------------------------------

            simple_query = '''

SELECT
    CASE 
        WHEN (contratos.adesao BETWEEN '{}' AND '{}') THEN TO_DATE('{}', 'MM/YYYY') END AS adesao,
    CASE 
        WHEN (upper(cidade.cidade) LIKE '%PATR%')   THEN 'PATROCINIO'
        WHEN (upper(cidade.cidade) LIKE '%PATO%')   THEN 'PATOS DE MINAS'
        WHEN (upper(cidade.cidade) LIKE '%GUIM%')   THEN 'GUIMARANIA'
        WHEN (upper(cidade.cidade) LIKE '%ABAD%')   THEN 'ABADIA DOS DOURADOS'
        WHEN (upper(cidade.cidade) LIKE '%IRA%')    THEN 'IRAI DE MINAS'
        WHEN (upper(cidade.cidade) LIKE '%CRUZ%')   THEN 'CRUZEIRO DA FORTALEZA'
        WHEN (upper(cidade.cidade) LIKE '%VARJ%')   THEN 'VARJAO DE MINAS'
        WHEN (upper(cidade.cidade) LIKE '%OLEG%')   THEN 'PRESIDENTE OLEGARIO'
        WHEN (upper(cidade.cidade) LIKE '%MARIAS%') THEN 'TRES MARIAS'
        WHEN (upper(cidade.cidade) LIKE '%JOAO%')   THEN 'JOAO PINHEIRO'
        WHEN (upper(cidade.cidade) LIKE '%LAGOA%')  THEN 'LAGOA FORMOSA'
        ELSE 'OUTROS'
    END AS cidade,
    COUNT(contratos.codcontrato) AS contratos_criados

FROM 
    public.mk_contratos contratos
    INNER JOIN public.mk_pessoas pessoa ON (contratos.cliente = pessoa.codpessoa)
    INNER JOIN public.mk_cidades cidade ON (pessoa.codcidade = cidade.codcidade)

WHERE 
    contratos.adesao BETWEEN '{}' AND '{}'

GROUP BY 1,2

            '''.format(
            # -----------------
            data_fixa,
            final,
            periodo,
            data_fixa,
            final
            # -----------------
            )

            if x != (self.dates_.range_meses - 1):
                complete_query = complete_query + simple_query + '''
UNION
'''
            else:
                complete_query = complete_query + simple_query + '''
ORDER BY 2 ASC, 1 ASC;
'''

        return str(complete_query)

    def evolucao_contratos_criados_e_cancelados_totais(self):

        # Variaveis
        # -------------------------
        complete_query = ''
        # -------------------------

        # Data Fixa
        # -----------------------------
        data_fixa = str(date(2010, 1, 1).strftime(self.dates_.style_date))
        # -----------------------------

        for x in range(self.dates_.range_meses):

            # Variaveis
            # --------------------------------------------------
            inicio, final, periodo = self.dates_.dates_personalizadas(x)
            # --------------------------------------------------

            simple_query = '''

SELECT
    CASE WHEN (contratos.adesao BETWEEN '{}' AND '{}') THEN TO_DATE('{}', 'MM/YYYY') END AS data,
    COUNT(contratos.codcontrato) AS quantidade_contratos_criados,
    -- INICIO
    (
    SELECT 
        COUNT(contratos.codcontrato) 

    FROM 
        public.mk_contratos contratos 
        INNER JOIN public.mk_pessoas pessoa ON (contratos.cliente = pessoa.codpessoa)
        INNER JOIN public.mk_cidades cidade ON (pessoa.codcidade = cidade.codcidade)

    WHERE 
        contratos.cancelado = 'S' 
        AND contratos.dt_cancelamento BETWEEN '{}' AND '{}'

    ) AS quantidade_contratos_cancelados
    -- FIM

FROM 
    public.mk_contratos contratos
    INNER JOIN public.mk_pessoas pessoa ON (contratos.cliente = pessoa.codpessoa)
    INNER JOIN public.mk_cidades cidade ON (pessoa.codcidade = cidade.codcidade)

WHERE 
    contratos.adesao BETWEEN '{}' AND '{}'

GROUP BY 1
            
            '''.format(
            # -----------------
            data_fixa,
            final,
            periodo,
            data_fixa,
            final,
            data_fixa,
            final
            # -----------------
            )

            if x != (self.dates_.range_meses - 1):
                complete_query = complete_query + simple_query + '''
UNION
'''
            else:
                complete_query = complete_query + simple_query + '''
ORDER BY 1 ASC;
'''

        return str(complete_query)
