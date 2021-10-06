from Consultas.Get_Date import Get_Date
from Save_Convert.Save_to_SQL import Save_to_SQL

class Querys_de_Cancelamentos_MK:

    def __init__(self):


        # -----------------------------------------------------
        #Config Periodo de Consultas
        self.dates_ = Get_Date( type_date = 1 )
        # -----------------------------------------------------
        # ----------------
        # Nome Colunas
        self.name_columns = []
        # ----------------
        

    def cancelamentos_por_cidades(self): # MK - OK OK OK
        
        # Variaveis 
        # ---------------------------
        self.name_columns = ['Data', 'Cidade', 'Quantidade']
        complete_query = ''
        # ---------------------------

        for x in range(self.dates_.range_meses):
            
            # Variaveis
            # --------------------------------------------------
            inicio, final, periodo = self.dates_.dates_personalizadas(x)
            # --------------------------------------------------

            simple_query = '''
            
                SELECT
                    CASE WHEN (contrato.dt_cancelamento between '{}' AND '{}') THEN TO_DATE('{}', 'MM/YYYY') end as dt_cancelamento,
                    CASE WHEN (upper(cidade.cidade) LIKE '%PATR%') THEN 'PATROCINIO'
                    WHEN (upper(cidade.cidade) LIKE '%PATO%') THEN 'PATOS DE MINAS'
                    WHEN (upper(cidade.cidade) LIKE '%GUIM%') THEN 'GUIMARANIA'
                    WHEN (upper(cidade.cidade) LIKE '%ABAD%') THEN 'ABADIA DOS DOURADOS'
                    WHEN (upper(cidade.cidade) LIKE '%IRA%') THEN 'IRAI DE MINAS'
                    WHEN (upper(cidade.cidade) LIKE '%CRUZ%') THEN 'CRUZEIRO DA FORTALEZA'
                    WHEN (upper(cidade.cidade) LIKE '%VARJ%') THEN 'VARJAO DE MINAS'
                    WHEN (upper(cidade.cidade) LIKE '%OLEG%') THEN 'PRESIDENTE OLEGARIO'
                    WHEN (upper(cidade.cidade) LIKE '%MARIAS%') THEN 'TRES MARIAS'
                    WHEN (upper(cidade.cidade) LIKE '%JOAO%') THEN 'JOAO PINHEIRO'
                    WHEN (upper(cidade.cidade) LIKE '%LAGOA%') THEN 'LAGOA FORMOSA'
                    ELSE 'OUTROS'
                end as cidade,
                        count(contrato.codcontrato)
                        
                from public.mk_contratos contrato
                inner join public.mk_pessoas pessoa on (pessoa.codpessoa = contrato.cliente)
                inner join public.mk_cidades cidade on (pessoa.codcidade = cidade.codcidade)
                left join public.mk_motivo_cancelamento motivo on (contrato.motivo_cancelamento_2 = motivo.codmotcancel)

                where contrato.cancelado = 'S'
                and contrato.dt_cancelamento between '{}' AND '{}'
                and motivo.descricao_mot_cancel not like '%AJUSTE%'

                GROUP BY 1,2

            '''.format(
                #-----------------
                inicio,
                final,
                periodo,
                inicio,
                final
                #-----------------
            )

            if x != (self.dates_.range_meses - 1):
                complete_query = complete_query + simple_query + '''UNION'''
            else:
                complete_query = complete_query + simple_query + '''ORDER BY 2, 1;'''

        return str(complete_query)
        
    def cancelamentos_geral_por_mes(self): # MK - OK OK
        
        # Variaveis 
        # ---------------------------
        self.name_columns = ['Data', 'Quantidade']
        complete_query = ''
        # ---------------------------

        for x in range(self.dates_.range_meses):
            
            # Variaveis
            # --------------------------------------------------
            inicio, final, periodo = self.dates_.dates_personalizadas(x)
            # --------------------------------------------------

            simple_query = '''
            
            select
                case when (contrato.dt_cancelamento between '{}' AND '{}') THEN TO_DATE('{}', 'MM/YYYY') end as dt_cancelamento,
                count(contrato.codcontrato)
                    
            from public.mk_contratos contrato
            inner join public.mk_pessoas pessoa on (pessoa.codpessoa = contrato.cliente)
            inner join public.mk_cidades cidade on (pessoa.codcidade = cidade.codcidade)
            left join public.mk_motivo_cancelamento motivo on (contrato.motivo_cancelamento_2 = motivo.codmotcancel)

            where contrato.cancelado = 'S'
            and contrato.dt_cancelamento between '{}' AND '{}'
            and motivo.descricao_mot_cancel not like '%AJUSTE%'

            GROUP BY 1

            '''.format(
                #-----------------
                inicio,
                final,
                periodo,
                inicio,
                final
                #-----------------
            )

            if x != (self.dates_.range_meses - 1):
                complete_query = complete_query + simple_query + '''UNION'''
            else:
                complete_query = complete_query + simple_query + '''ORDER BY 1;'''

        return str(complete_query)