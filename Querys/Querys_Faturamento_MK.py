from Consultas.Get_Date import Get_Date


class Querys_de_Faturamento_MK:

    def __init__(self):
        # -----------------------------------------------------
        # Config Periodo de Consultas
        self.dates_ = Get_Date(type_date=1)
        # -----------------------------------------------------

    def faturamento_por_cidades(self):

        # Variaveis
        # ---------------------------
        complete_query = ''
        # ---------------------------

        for x in range(self.dates_.range_meses):

            # Variaveis
            # --------------------------------------------------
            inicio, final, periodo = self.dates_.dates_personalizadas(x)
            # --------------------------------------------------

            simple_query = '''

SELECT DISTINCT 
    CASE 
        WHEN (fatura.data_vencimento BETWEEN '{}' AND '{}') THEN TO_DATE('{}', 'MM/YYYY') END AS vencimento,
    CASE 
        WHEN (upper(cidade.cidade) LIKE '%PATR%')   THEN 'PATROCINIO'
        WHEN (upper(cidade.cidade) LIKE '%PATO%')   THEN 'PATOS DE MINAS'
        WHEN (upper(cidade.cidade) LIKE '%GUIM%')   THEN 'GUIMARANIA'
        WHEN (upper(cidade.cidade) LIKE '%ABAD%')   THEN 'ABADIA DOS DOURADOS'
        WHEN (upper(cidade.cidade) LIKE 'IRA%')    THEN 'IRAI DE MINAS'
        WHEN (upper(cidade.cidade) LIKE '%CRUZ%')   THEN 'CRUZEIRO DA FORTALEZA'
        WHEN (upper(cidade.cidade) LIKE '%VARJ%')   THEN 'VARJAO DE MINAS'
        WHEN (upper(cidade.cidade) LIKE '%OLEG%')   THEN 'PRESIDENTE OLEGARIO'
        WHEN (upper(cidade.cidade) LIKE '%MARIAS%') THEN 'TRES MARIAS'
        WHEN (upper(cidade.cidade) LIKE '%PINHEIRO%')   THEN 'JOAO PINHEIRO'
        WHEN (upper(cidade.cidade) LIKE '%LAGOA%')  THEN 'LAGOA FORMOSA'
        WHEN (upper(cidade.cidade) LIKE '%GON%ALO%')  THEN 'SAO GONCALO DO ABAETE'
        WHEN (upper(cidade.cidade) LIKE '%PIRAPORA%')  THEN 'PIRAPORA'
        WHEN (upper(cidade.cidade) LIKE '%V%RZEA%')  THEN 'VARZEA DA PALMA'
        WHEN (upper(cidade.cidade) LIKE '%BURITIZEIRO%')  THEN 'BURITIZEIRO'
        ELSE 'OUTROS'
    END AS cidade,
    SUM(fatura.valor_total) valor

FROM 
    public.mk_faturas fatura
    LEFT JOIN public.mk_profile_pgto profile        ON (fatura.cd_profile_cobranca = profile.codprofile)
    LEFT JOIN public.mk_pessoas pessoa              ON (pessoa.codpessoa = fatura.cd_pessoa)
    LEFT JOIN public.mk_provedor_empresas empresa   ON (empresa.codprovemp = fatura.cd_empresa)
    INNER JOIN public.mk_cidades cidade             ON (pessoa.codcidade = cidade.codcidade)

WHERE 
    fatura.tipo = 'R'
    AND fatura.excluida = 'N'
    AND fatura.suspenso =  'N'
    AND fatura.data_vencimento BETWEEN '{}' AND '{}'

GROUP BY 1,2

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
ORDER BY 2, 1;
'''

        return str(complete_query)

    def faturamento_geral_por_mes(self):

        # Variaveis
        # ---------------------------
        complete_query = ''
        # ---------------------------

        for x in range(self.dates_.range_meses):

            # Variaveis
            # --------------------------------------------------
            inicio, final, periodo = self.dates_.dates_personalizadas(x)
            # --------------------------------------------------

            simple_query = '''

SELECT DISTINCT
    CASE WHEN (fatura.data_vencimento BETWEEN '{}' AND '{}') THEN TO_DATE('{}', 'MM/YYYY') END AS vencimento,
    SUM(fatura.valor_total) valor
        
FROM 
    public.mk_faturas fatura
    LEFT JOIN public.mk_profile_pgto profile ON (fatura.cd_profile_cobranca = profile.codprofile)
    LEFT JOIN public.mk_pessoas pessoa ON (pessoa.codpessoa = fatura.cd_pessoa)
    LEFT JOIN public.mk_provedor_empresas empresa ON (empresa.codprovemp = fatura.cd_empresa)
    INNER JOIN public.mk_cidades cidade ON (pessoa.codcidade = cidade.codcidade)

WHERE 
    fatura.tipo = 'R'
    AND fatura.excluida = 'N'
    AND fatura.suspenso =  'N'
    AND fatura.data_vencimento BETWEEN '{}' AND '{}'

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
