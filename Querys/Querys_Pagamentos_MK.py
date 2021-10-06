from Consultas.Get_Date import Get_Date
from Save_Convert.Save_to_SQL import Save_to_SQL

class Querys_de_Pagamentos_MK:

    def __init__(self):

        # -----------------------------------------------------
        #Config Periodo de Consultas
        self.dates_ = Get_Date( type_date = 1 )
        # -----------------------------------------------------
        # ----------------
        # Nome Colunas
        self.name_columns = []
        # ----------------
        

    def pagamentos_geral(self): # MK - OK OK
        
        # Variaveis 
        # ---------------------------
        self.name_columns = ['Data', 'Valor']
        complete_query = ''
        # ---------------------------

        for x in range(self.dates_.range_meses):
            
            # Variaveis
            # --------------------------------------------------
            inicio, final, periodo = self.dates_.dates_personalizadas(x)
            # --------------------------------------------------

            simple_query = '''
            
                select distinct
                            case when (fatura.data_vencimento between '{}' and '{}') THEN TO_DATE('{}', 'MM/YYYY') end as vencimento,
                        sum(fatura.valor_total) valor
                            
                from public.mk_faturas fatura
                left  join public.mk_profile_pgto profile on (fatura.cd_profile_cobranca = profile.codprofile)
                left  join public.mk_pessoas pessoa on (pessoa.codpessoa = fatura.cd_pessoa)
                inner join public.mk_cidades cidade on (pessoa.codcidade = cidade.codcidade)
                left  join public.mk_provedor_empresas empresa on (empresa.codprovemp = fatura.cd_empresa)

                where fatura.tipo = 'P'
                and fatura.excluida = 'N'
                and fatura.suspenso =  'N'
                and fatura.data_vencimento between '{}' and '{}'

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
        
    