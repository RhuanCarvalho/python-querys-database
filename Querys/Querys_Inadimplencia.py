from datetime import date
from Consultas.Get_Date import Get_Date
from Save_Convert.Save_to_SQL import Save_to_SQL


class Querys_de_Inadimplencia_MK:

    def __init__(self):

        # -----------------------------------------------------
        #Config Periodo de Consultas
        self.dates_ = Get_Date( type_date = 1 )
        # -----------------------------------------------------
        # ----------------
        # Nome Colunas
        self.name_columns = []
        # ----------------

    def inadimplencia_por_cidades(self): # MK - OK OK OK
        
        # Variaveis 
        # ---------------------------
        self.name_columns = ['Data', 'Cidade', 'Valor']
        complete_query = ''
        # ---------------------------

        for x in range(self.dates_.range_meses):
            
            # Variaveis dates
            # --------------------------------------------------
            inicio, final, periodo = self.dates_.dates_personalizadas(x)
            # --------------------------------------------------

            simple_query = '''
            
            select 
                case when (fatura.data_vencimento BETWEEN '{}' and '{}') THEN TO_DATE('{}', 'MM/YYYY') end as vencimento,
                case when (upper(cidade.cidade) LIKE '%PATR%') THEN 'PATROCINIO'
                    when (upper(cidade.cidade) LIKE '%PATO%') THEN 'PATOS DE MINAS'
                    when (upper(cidade.cidade) LIKE '%GUIM%') THEN 'GUIMARANIA'
                    when (upper(cidade.cidade) LIKE '%ABAD%') THEN 'ABADIA DOS DOURADOS'
                    when (upper(cidade.cidade) LIKE '%IRA%') THEN 'IRAI DE MINAS'
                    when (upper(cidade.cidade) LIKE '%CRUZ%') THEN 'CRUZEIRO DA FORTALEZA'
                    when (upper(cidade.cidade) LIKE '%VARJ%') THEN 'VARJAO DE MINAS'
                    when (upper(cidade.cidade) LIKE '%OLEG%') THEN 'PRESIDENTE OLEGARIO'
                    when (upper(cidade.cidade) LIKE '%MARIAS%') THEN 'TRES MARIAS'
                    when (upper(cidade.cidade) LIKE '%JOAO%') THEN 'JOAO PINHEIRO'
                    when (upper(cidade.cidade) LIKE '%LAGOA%') THEN 'LAGOA FORMOSA'
                ELSE 'OUTROS'
                end as cidade,
                sum(fatura.valor_total) as valor
                
            from public.mk_faturas fatura
            left  join public.mk_profile_pgto profile on (fatura.cd_profile_cobranca = profile.codprofile)
            left  join public.mk_pessoas pessoa on (pessoa.codpessoa = fatura.cd_pessoa)
            inner join public.mk_cidades cidade on (pessoa.codcidade = cidade.codcidade)
                
            where fatura.tipo = 'R' 
            and fatura.excluida = 'N'
            and fatura.suspenso =  'N'
            and fatura.data_vencimento BETWEEN '{}' and '{}'
            and fatura.data_vencimento < CURRENT_DATE 
            and fatura.liquidado = 'N'

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

        Save_to_SQL.save_querys(complete_query, 'inadimplencia', 'inadimplencia_por_cidades')
        return str(complete_query)
        
    def inadimplencia_total_por_mes(self): # MK - OK OK OK

        # Variaveis
        # -------------------------
        self.name_columns = ['Data', 'Valor']
        complete_query = ''
        # -------------------------
        
        
        for x in range(self.dates_.range_meses): 

            # Variaveis dates
            # --------------------------------------------------
            inicio, final, periodo = self.dates_.dates_personalizadas(x)
            # --------------------------------------------------
            
            
            simple_query = '''

            select 
                case when (fatura.data_vencimento BETWEEN '{}' and '{}') THEN TO_DATE('{}', 'MM/YYYY') end as vencimento,
                sum(fatura.valor_total) as valor
                
            from public.mk_faturas fatura
            left  join public.mk_profile_pgto profile on (fatura.cd_profile_cobranca = profile.codprofile)
            left  join public.mk_pessoas pessoa on (pessoa.codpessoa = fatura.cd_pessoa)
            inner join public.mk_cidades cidade on (pessoa.codcidade = cidade.codcidade)
                
            where fatura.tipo = 'R' 
            and fatura.excluida = 'N'
            and fatura.suspenso =  'N'
            and fatura.data_vencimento BETWEEN '{}' and '{}'
            and fatura.data_vencimento < CURRENT_DATE 
            and fatura.liquidado = 'N'

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
                

        Save_to_SQL.save_querys(complete_query, 'inadimplencia', 'inadimplencia_total_por_mes')
        return str(complete_query)

    def evolucao_inadimplencia_por_cidade(self): # MK - OK OK OK

        # Variaveis
        # -------------------------
        self.name_columns = ['Data', 'Cidade', 'Valor']
        complete_query = ''
        # -------------------------

        # Data Fixa
        # -----------------------------
        data_fixa = str(date(2010,1,1).strftime(self.dates_.style_date)) 
        # -----------------------------
        
        for x in range(self.dates_.range_meses):

            # Variaveis
            # --------------------------------------------------
            inicio, final, periodo = self.dates_.dates_personalizadas(x)
            # --------------------------------------------------

            simple_query = '''
                
                select 
                    case when (fatura.data_vencimento BETWEEN '{}' and '{}') THEN TO_DATE('{}', 'MM/YYYY') end as vencimento,
                    case when (upper(cidade.cidade) LIKE '%PATR%') THEN 'PATROCINIO'
                        when (upper(cidade.cidade) LIKE '%PATO%') THEN 'PATOS DE MINAS'
                        when (upper(cidade.cidade) LIKE '%GUIM%') THEN 'GUIMARANIA'
                        when (upper(cidade.cidade) LIKE '%ABAD%') THEN 'ABADIA DOS DOURADOS'
                        when (upper(cidade.cidade) LIKE '%IRA%') THEN 'IRAI DE MINAS'
                        when (upper(cidade.cidade) LIKE '%CRUZ%') THEN 'CRUZEIRO DA FORTALEZA'
                        when (upper(cidade.cidade) LIKE '%VARJ%') THEN 'VARJAO DE MINAS'
                        when (upper(cidade.cidade) LIKE '%OLEG%') THEN 'PRESIDENTE OLEGARIO'
                        when (upper(cidade.cidade) LIKE '%MARIAS%') THEN 'TRES MARIAS'
                        when (upper(cidade.cidade) LIKE '%JOAO%') THEN 'JOAO PINHEIRO'
                        when (upper(cidade.cidade) LIKE '%LAGOA%') THEN 'LAGOA FORMOSA'
                    ELSE 'OUTROS'
                    end as cidade,
                    sum(fatura.valor_total) as valor
                    
                from public.mk_faturas fatura
                left  join public.mk_profile_pgto profile on (fatura.cd_profile_cobranca = profile.codprofile)
                left  join public.mk_pessoas pessoa on (pessoa.codpessoa = fatura.cd_pessoa)
                inner join public.mk_cidades cidade on (pessoa.codcidade = cidade.codcidade)
                    
                where fatura.tipo = 'R' 
                and fatura.excluida = 'N'
                and fatura.suspenso =  'N'
                and fatura.data_vencimento BETWEEN '{}' and '{}'
                and fatura.data_vencimento < CURRENT_DATE 
                and fatura.liquidado = 'N'

                GROUP BY 1,2

                '''.format(
                #-----------------
                data_fixa,
                final,
                periodo,
                data_fixa,
                final
                #-----------------
            )

            if x != (self.dates_.range_meses - 1):
                complete_query = complete_query + simple_query + '''UNION'''
            else:
                complete_query = complete_query + simple_query + '''ORDER BY 2, 1;'''



        Save_to_SQL.save_querys(complete_query, 'inadimplencia', 'evolucao_inadimplencia_por_cidade')
        return str(complete_query)

    def evolucao_inadimplencia_totais_por_mes(self): # MK - OK OK OK

        # Variaveis
        # -------------------------
        self.name_columns = ['Data', 'Valor']
        complete_query = ''
        # -------------------------

        # Data Fixa
        # -----------------------------
        data_fixa = str(date(2010,1,1).strftime(self.dates_.style_date)) 
        # -----------------------------
        
        

        for x in range(self.dates_.range_meses):

            # Variaveis
            # --------------------------------------------------
            inicio, final, periodo = self.dates_.dates_personalizadas(x)
            # --------------------------------------------------

            simple_query = '''
                select 
                    case when (fatura.data_vencimento BETWEEN '{}' and '{}') THEN TO_DATE('{}', 'MM/YYYY') end as vencimento,
                    sum(fatura.valor_total) as valor
                    
                from public.mk_faturas fatura
                left  join public.mk_profile_pgto profile on (fatura.cd_profile_cobranca = profile.codprofile)
                left  join public.mk_pessoas pessoa on (pessoa.codpessoa = fatura.cd_pessoa)
                inner join public.mk_cidades cidade on (pessoa.codcidade = cidade.codcidade)
                    
                where fatura.tipo = 'R' 
                and fatura.excluida = 'N'
                and fatura.suspenso =  'N'
                and fatura.data_vencimento BETWEEN '{}' and '{}'
                and fatura.data_vencimento < CURRENT_DATE 
                and fatura.liquidado = 'N'

                GROUP BY 1

                '''.format(
                    #-----------------
                    data_fixa,
                    final,
                    periodo,
                    data_fixa,
                    final
                    #-----------------
                )

            if x != (self.dates_.range_meses - 1):
                complete_query = complete_query + simple_query + '''UNION'''
            else:
                complete_query = complete_query + simple_query + '''ORDER BY 1;'''



        Save_to_SQL.save_querys(complete_query, 'inadimplencia', 'evolucao_inadimplencia_totais_por_mes')
        return str(complete_query)


