from Consultas.Get_Date import Get_Date


class Querys_de_Cancelamentos_MK:

    def __init__(self):
        # -----------------------------------------------------
        # Config Periodo de Consultas
        self.dates_ = Get_Date(type_date=1)
        # -----------------------------------------------------

    def cancelamentos_por_cidades(self):

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

SELECT
    CASE 
        WHEN (contrato.dt_cancelamento BETWEEN '{}' AND '{}') THEN TO_DATE('{}', 'MM/YYYY') END AS dt_cancelamento,
    CASE 
        WHEN (upper(cidade.cidade) LIKE '%PATR%')       THEN 'PATROCINIO'
        WHEN (upper(cidade.cidade) LIKE '%PATO%')       THEN 'PATOS DE MINAS'
        WHEN (upper(cidade.cidade) LIKE '%GUIM%')       THEN 'GUIMARANIA'
        WHEN (upper(cidade.cidade) LIKE '%ABAD%')       THEN 'ABADIA DOS DOURADOS'
        WHEN (upper(cidade.cidade) LIKE 'IRA%')        THEN 'IRAI DE MINAS'
        WHEN (upper(cidade.cidade) LIKE '%CRUZ%')       THEN 'CRUZEIRO DA FORTALEZA'
        WHEN (upper(cidade.cidade) LIKE '%VARJ%')       THEN 'VARJAO DE MINAS'
        WHEN (upper(cidade.cidade) LIKE '%OLEG%')       THEN 'PRESIDENTE OLEGARIO'
        WHEN (upper(cidade.cidade) LIKE '%MARIAS%')     THEN 'TRES MARIAS'
        WHEN (upper(cidade.cidade) LIKE '%PINHEIRO%')   THEN 'JOAO PINHEIRO'
        WHEN (upper(cidade.cidade) LIKE '%LAGOA%')      THEN 'LAGOA FORMOSA'
        WHEN (upper(cidade.cidade) LIKE '%GON%ALO%')    THEN 'SAO GONCALO DO ABAETE'
        WHEN (upper(cidade.cidade) LIKE '%PIRAPORA%')  THEN 'PIRAPORA'
        WHEN (upper(cidade.cidade) LIKE '%V%RZEA%')  THEN 'VARZEA DA PALMA'
        WHEN (upper(cidade.cidade) LIKE '%BURITIZEIRO%')  THEN 'BURITIZEIRO'
        ELSE 'OUTROS'
    END AS cidade,
    COUNT(contrato.codcontrato)

FROM 
    public.mk_contratos contrato
    INNER JOIN public.mk_pessoas pessoa             ON (pessoa.codpessoa = contrato.cliente)
    INNER JOIN public.mk_cidades cidade             ON (pessoa.codcidade = cidade.codcidade)
    LEFT JOIN  public.mk_motivo_cancelamento motivo ON (contrato.motivo_cancelamento_2 = motivo.codmotcancel)

WHERE 
    contrato.cancelado = 'S'
    AND contrato.dt_cancelamento BETWEEN '{}' AND '{}'
    AND motivo.descricao_mot_cancel NOT LIKE '%AJUSTE%'

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

    def cancelamentos_geral_por_mes(self):

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
            
SELECT
    CASE WHEN (contrato.dt_cancelamento BETWEEN '{}' AND '{}') THEN TO_DATE('{}', 'MM/YYYY') END AS dt_cancelamento,
    COUNT(contrato.codcontrato)

FROM 
    public.mk_contratos contrato
    INNER JOIN public.mk_pessoas pessoa             ON (pessoa.codpessoa = contrato.cliente)
    INNER JOIN public.mk_cidades cidade             ON (pessoa.codcidade = cidade.codcidade)
    LEFT JOIN public.mk_motivo_cancelamento motivo  ON (contrato.motivo_cancelamento_2 = motivo.codmotcancel)

WHERE 
    contrato.cancelado = 'S'
    AND contrato.dt_cancelamento BETWEEN '{}' AND '{}'
    AND motivo.descricao_mot_cancel NOT LIKE '%AJUSTE%'

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
