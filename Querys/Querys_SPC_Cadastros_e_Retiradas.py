from datetime import date
from Consultas.Get_Date import Get_Date


class Querys_SPC_Cadastros_e_Retiradas_MK:

    def __init__(self):
        # -----------------------------------------------------
        # Config Periodo de Consultas
        self.dates_ = Get_Date(type_date=1)
        # -----------------------------------------------------

    def cadastros_SPC_mensal(self):

        # Variaveis
        # -------------------------
        complete_query = ''
        # -------------------------

        for x in range(self.dates_.range_meses):

            # Variaveis
            # --------------------------------------------------
            inicio, final, periodo = self.dates_.dates_personalizadas(x)
            # --------------------------------------------------

            simple_query = '''

SELECT 
    CASE WHEN (spc.dh BETWEEN '{}' AND '{}') THEN TO_DATE('{}', 'MM/YYYY') END AS dt_spc,
    SUM(fatura.valor_total) AS valor

FROM 
    public.mk_cobr_spc spc
    LEFT JOIN public.mk_faturas fatura          ON (fatura.codfatura = spc.cd_fatura)
    LEFT JOIN public.mk_profile_pgto profile    ON (fatura.cd_profile_cobranca = profile.codprofile)
    LEFT JOIN public.mk_pessoas pessoa          ON (pessoa.codpessoa = fatura.cd_pessoa)
    INNER JOIN public.mk_cidades cidade         ON (pessoa.codcidade = cidade.codcidade)

WHERE 
    fatura.tipo = 'R' 
    AND spc.fim = 'N'
    AND spc.dh BETWEEN '{}' AND '{}'

GROUP BY 1

            '''.format(
            # -----------------
            inicio,
            final,
            periodo,
            inicio,
            final
            # -----------------
            )

            if x != (self.dates_.range_meses - 1):
                complete_query = complete_query + simple_query + '''
UNION
'''
            else:
                complete_query = complete_query + simple_query + '''
ORDER BY 1;
'''

        return str(complete_query)

    def retiradas_SPC_mensal(self):

        # Variaveis
        # -------------------------
        complete_query = ''
        # -------------------------

        for x in range(self.dates_.range_meses):

            # Variaveis
            # --------------------------------------------------
            inicio, final, periodo = self.dates_.dates_personalizadas(x)
            # --------------------------------------------------

            simple_query = '''

SELECT  
    CASE WHEN (spc.dh_fim BETWEEN '{}' AND '{}') THEN TO_DATE('{}', 'MM/YYYY') END AS dt_spc,
    SUM(fatura.valor_total) AS valor

FROM 
    public.mk_cobr_spc spc
    LEFT JOIN public.mk_faturas fatura          ON (fatura.codfatura = spc.cd_fatura)
    LEFT JOIN public.mk_profile_pgto profile    ON (fatura.cd_profile_cobranca = profile.codprofile)
    LEFT JOIN public.mk_pessoas pessoa          ON (pessoa.codpessoa = fatura.cd_pessoa)
    INNER JOIN public.mk_cidades cidade         ON (pessoa.codcidade = cidade.codcidade)

WHERE 
    fatura.tipo = 'R' 
    AND spc.fim = 'S'
    AND spc.dh_fim BETWEEN '{}' AND '{}'

GROUP BY 1

            '''.format(
            # -----------------
            inicio,
            final,
            periodo,
            inicio,
            final
            # -----------------
            )

            if x != (self.dates_.range_meses - 1):
                complete_query = complete_query + simple_query + '''
UNION
'''
            else:
                complete_query = complete_query + simple_query + '''
ORDER BY 1;
'''

        return str(complete_query)

    def evolucao_cadastros_SPC(self):

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
    CASE WHEN (spc.dh BETWEEN '{}' AND '{}') THEN TO_DATE('{}', 'MM/YYYY') END AS dt_spc,
    SUM(fatura.valor_total) AS valor

FROM 
    public.mk_cobr_spc spc
    LEFT JOIN public.mk_faturas fatura          ON (fatura.codfatura = spc.cd_fatura)
    LEFT JOIN public.mk_profile_pgto profile    ON (fatura.cd_profile_cobranca = profile.codprofile)
    LEFT JOIN public.mk_pessoas pessoa          ON (pessoa.codpessoa = fatura.cd_pessoa)
    INNER JOIN public.mk_cidades cidade         ON (pessoa.codcidade = cidade.codcidade)

WHERE
    fatura.tipo = 'R' 
    AND spc.fim = 'N'
    AND spc.dh BETWEEN '{}' AND '{}'

GROUP BY 1
        
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
ORDER BY 1;
'''

        return str(complete_query)

    def evolucao_retiradas_SPC(self):

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
    CASE WHEN (spc.dh_fim BETWEEN '{}' AND '{}') THEN TO_DATE('{}', 'MM/YYYY') END AS dt_spc,
    SUM(fatura.valor_total) AS valor

FROM 
    public.mk_cobr_spc spc
    LEFT JOIN public.mk_faturas fatura          ON (fatura.codfatura = spc.cd_fatura)
    LEFT JOIN public.mk_profile_pgto profile    ON (fatura.cd_profile_cobranca = profile.codprofile)
    LEFT JOIN public.mk_pessoas pessoa          ON (pessoa.codpessoa = fatura.cd_pessoa)
    INNER JOIN public.mk_cidades cidade         ON (pessoa.codcidade = cidade.codcidade)

WHERE 
    fatura.tipo = 'R' 
    AND spc.fim = 'S'
    AND spc.dh_fim BETWEEN '{}' AND '{}'

GROUP BY 1

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
ORDER BY 1;
'''

        return str(complete_query)
