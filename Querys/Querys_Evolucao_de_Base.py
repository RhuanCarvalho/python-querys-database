from datetime import date
from Consultas.Get_Date import Get_Date


class Querys_Evolucao_de_Base_MK:

    def __init__(self):

        # -----------------------------------------------------
        #Config Periodo de Consultas
        self.dates_ = Get_Date( type_date = 1 )
        # -----------------------------------------------------
              

    def evolucao_contratos_cancelados_por_cidades(self): # MK - OK OK OK

        # Variaveis
        # -------------------------
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

                case when (contratos.adesao BETWEEN '{}' and '{}') THEN TO_DATE('{}', 'MM/YYYY') end as adesao,
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
                count(contratos.codcontrato) as contratos_cancelados


                from public.mk_contratos contratos
                inner join public.mk_pessoas pessoa on (contratos.cliente = pessoa.codpessoa)
                inner join public.mk_cidades cidade on (pessoa.codcidade = cidade.codcidade)

                where contratos.cancelado = 'S'
                and contratos.dt_cancelamento BETWEEN '{}' and '{}'

                group by 1,2

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
                complete_query = complete_query + simple_query + '''ORDER BY 2 ASC, 1 ASC;'''


        return str(complete_query)

    def evolucao_contratos_criados_por_cidades(self): # MK - OK OK OK

        # Variaveis
        # -------------------------
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

                case when (contratos.adesao between '{}' and '{}') THEN TO_DATE('{}', 'MM/YYYY') end as adesao,
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
                count(contratos.codcontrato) as contratos_criados


                from public.mk_contratos contratos
                inner join public.mk_pessoas pessoa on (contratos.cliente = pessoa.codpessoa)
                inner join public.mk_cidades cidade on (pessoa.codcidade = cidade.codcidade)

                where contratos.adesao between '{}' and '{}'

                group by 1,2


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
                complete_query = complete_query + simple_query + '''ORDER BY 2 ASC, 1 ASC;'''



        return str(complete_query)

    def evolucao_contratos_criados_e_cancelados_totais(self): # MK - OK OK OK

        # Variaveis
        # -------------------------
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

                case when (contratos.adesao BETWEEN '{}' and '{}') THEN TO_DATE('{}', 'MM/YYYY') end as data,
                count(contratos.codcontrato) as quantidade_contratos_criados,
                    (select count(contratos.codcontrato) from public.mk_contratos contratos 
                        inner join public.mk_pessoas pessoa on (contratos.cliente = pessoa.codpessoa)
                        inner join public.mk_cidades cidade on (pessoa.codcidade = cidade.codcidade)	
                        where contratos.cancelado = 'S'and contratos.dt_cancelamento BETWEEN '{}' and '{}'
                    ) as quantidade_contratos_cancelados



                from public.mk_contratos contratos
                inner join public.mk_pessoas pessoa on (contratos.cliente = pessoa.codpessoa)
                inner join public.mk_cidades cidade on (pessoa.codcidade = cidade.codcidade)

                where contratos.adesao between  '{}' and '{}'


                group by 1

                '''.format(
                    #-----------------
                    data_fixa,
                    final,
                    periodo,
                    data_fixa,
                    final,
                    data_fixa,
                    final
                    #-----------------
                )


            if x != (self.dates_.range_meses - 1):
                complete_query = complete_query + simple_query + '''UNION'''
            else:
                complete_query = complete_query + simple_query + '''ORDER BY 1 ASC;'''



        return str(complete_query)



