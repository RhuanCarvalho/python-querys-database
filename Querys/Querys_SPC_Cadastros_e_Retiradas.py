from datetime import date
from Consultas.Get_Date import Get_Date
from Save_Convert.Save_to_SQL import Save_to_SQL


class Querys_SPC_Cadastros_e_Retiradas_MK:

    def __init__(self):

        # -----------------------------------------------------
        #Config Periodo de Consultas
        self.dates_ = Get_Date( type_date = 1 )
        # -----------------------------------------------------
        # ----------------
        # Nome Colunas
        self.name_columns = []
        # ----------------

    def cadastros_SPC_mensal(self): # MK - OK OK

        # Variaveis
        # -------------------------
        self.name_columns = ['Data', 'Valor']
        complete_query = ''
        # -------------------------

        for x in range(self.dates_.range_meses):

            # Variaveis
            # --------------------------------------------------
            inicio, final, periodo = self.dates_.dates_personalizadas(x)
            # --------------------------------------------------

            simple_query = '''
                
            select 
                case when (spc.dh between '{}' and '{}') THEN TO_DATE('{}', 'MM/YYYY') end as dt_spc,
                sum(fatura.valor_total) as valor
                
            from public.mk_cobr_spc spc
            left join public.mk_faturas fatura on (fatura.codfatura = spc.cd_fatura)
            left  join public.mk_profile_pgto profile on (fatura.cd_profile_cobranca = profile.codprofile)
            left  join public.mk_pessoas pessoa on (pessoa.codpessoa = fatura.cd_pessoa)
            inner join public.mk_cidades cidade on (pessoa.codcidade = cidade.codcidade)
                
            where fatura.tipo = 'R' 
            and spc.fim = 'N'
            and spc.dh between '{}' and '{}'

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



        Save_to_SQL.save_querys(complete_query, 'spc', 'cadastros_SPC_mensal')
        return str(complete_query)

    def retiradas_SPC_mensal(self): # MK - OK OK

        # Variaveis
        # -------------------------
        self.name_columns = ['Data', 'Valor']
        complete_query = ''
        # -------------------------
        
        
        for x in range(self.dates_.range_meses):

            # Variaveis
            # --------------------------------------------------
            inicio, final, periodo = self.dates_.dates_personalizadas(x)
            # --------------------------------------------------

            simple_query = '''
               
            select 
                case when (spc.dh_fim between '{}' and '{}') THEN TO_DATE('{}', 'MM/YYYY') end as dt_spc,
                sum(fatura.valor_total) as valor
                
            from public.mk_cobr_spc spc
            left join public.mk_faturas fatura on (fatura.codfatura = spc.cd_fatura)
            left  join public.mk_profile_pgto profile on (fatura.cd_profile_cobranca = profile.codprofile)
            left  join public.mk_pessoas pessoa on (pessoa.codpessoa = fatura.cd_pessoa)
            inner join public.mk_cidades cidade on (pessoa.codcidade = cidade.codcidade)
                
            where fatura.tipo = 'R' 
            and spc.fim = 'S'
            and spc.dh_fim between '{}' and '{}'

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



        Save_to_SQL.save_querys(complete_query, 'spc', 'retiradas_SPC_mensal')
        return str(complete_query)

    def evolucao_cadastros_SPC(self): # MK - OK OK

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
                case when (spc.dh between '{}' and '{}') THEN TO_DATE('{}', 'MM/YYYY') end as dt_spc,
                sum(fatura.valor_total) as valor
                
            from public.mk_cobr_spc spc
            left join public.mk_faturas fatura on (fatura.codfatura = spc.cd_fatura)
            left  join public.mk_profile_pgto profile on (fatura.cd_profile_cobranca = profile.codprofile)
            left  join public.mk_pessoas pessoa on (pessoa.codpessoa = fatura.cd_pessoa)
            inner join public.mk_cidades cidade on (pessoa.codcidade = cidade.codcidade)
                
            where fatura.tipo = 'R' 
            and spc.fim = 'N'
            and spc.dh between '{}' and '{}'

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



        Save_to_SQL.save_querys(complete_query, 'spc', 'evolucao_cadastros_SPC')
        return str(complete_query)

    def evolucao_retiradas_SPC(self): # MK - OK OK

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
                case when (spc.dh_fim between '{}' and '{}') THEN TO_DATE('{}', 'MM/YYYY') end as dt_spc,
                sum(fatura.valor_total) as valor
                
            from public.mk_cobr_spc spc
            left join public.mk_faturas fatura on (fatura.codfatura = spc.cd_fatura)
            left  join public.mk_profile_pgto profile on (fatura.cd_profile_cobranca = profile.codprofile)
            left  join public.mk_pessoas pessoa on (pessoa.codpessoa = fatura.cd_pessoa)
            inner join public.mk_cidades cidade on (pessoa.codcidade = cidade.codcidade)
                
            where fatura.tipo = 'R' 
            and spc.fim = 'S'
            and spc.dh_fim between '{}' and '{}'

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



        Save_to_SQL.save_querys(complete_query, 'spc', 'evolucao_retiradas_SPC')
        return str(complete_query)

