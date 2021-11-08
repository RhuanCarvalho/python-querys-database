from Consultas.Get_Date import Get_Date


class Querys_de_Pagamentos_MK:

    def __init__(self):
        # -----------------------------------------------------
        # Config Periodo de Consultas
        self.dates_ = Get_Date(type_date=1)
        # -----------------------------------------------------

    def pagamentos_geral(self):

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
    LEFT JOIN public.mk_profile_pgto profile        ON (fatura.cd_profile_cobranca = profile.codprofile)
    LEFT JOIN public.mk_pessoas pessoa              ON (pessoa.codpessoa = fatura.cd_pessoa)
    LEFT JOIN public.mk_provedor_empresas empresa   ON (empresa.codprovemp = fatura.cd_empresa)
    INNER JOIN public.mk_cidades cidade             ON (pessoa.codcidade = cidade.codcidade)

WHERE 
    fatura.tipo = 'P'
    AND fatura.excluida = 'N'
    AND fatura.suspenso =  'N'
    AND fatura.data_vencimento between '{}' AND '{}'

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
