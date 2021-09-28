from datetime import date
from Save_Convert.Save_to_SQL import Save_to_SQL
from Consultas.Get_Date import Get_Date

class Querys_de_Bloqueio_MK:

    def __init__(self):

        # -----------------------------------------------------
        #Config Periodo de Consultas
        self.dates_ = Get_Date( type_date = 1 )
        # -----------------------------------------------------

        # ----------------
        # Nome Colunas
        self.name_columns = []
        # ----------------

    def bloqueios_por_cidades(self): # MK - OK OK OK
        
        # Variaveis 
        # ---------------------------
        self.name_columns = ['Data', 'Cidade', 'Quantidade']
        complete_query = ''
        # ---------------------------

        for x in range(self.dates_.range_meses):
            
            # Variaveis dates
            # --------------------------------------------------
            inicio, final, periodo = self.dates_.dates_personalizadas(x)
            # --------------------------------------------------

            simple_query = '''
            
            SELECT
                case when (conexao.ultimo_bloqueio_auto between '{}' AND '{}') THEN TO_DATE('{}', 'MM/YYYY') end as dt_bloqueio,
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
                    count(contrato.codcontrato)
                    
            from public.mk_contratos contrato
            inner join public.mk_pessoas pessoa on (pessoa.codpessoa = contrato.cliente)
            inner join public.mk_cidades cidade on (pessoa.codcidade = cidade.codcidade)
            inner join public.mk_conexoes conexao on (contrato.codcontrato = conexao.contrato)

            where contrato.cancelado = 'N'
            and (contrato.suspenso = 'N' OR contrato.suspenso IS NULL)
            and conexao.tipo_conexao = 1
            and conexao.conexao_bloqueada = 'S'
            and conexao.ultimo_bloqueio_auto between '{}' AND '{}'

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
                complete_query = complete_query + simple_query + '''ORDER BY 2 ASC	, 1 ASC;'''

        Save_to_SQL.save_querys(complete_query, 'bloqueio', 'bloqueios_por_cidades')
        return str(complete_query)
        
    def bloqueios_total_por_mes(self): # MK - OK Ok OK

        # Variaveis
        # -------------------------
        self.name_columns = ['Data', 'Quantidade']
        complete_query = ''
        # -------------------------
        
        
        for x in range(self.dates_.range_meses): 

            # Variaveis dates
            # --------------------------------------------------
            inicio, final, periodo = self.dates_.dates_personalizadas(x)
            # --------------------------------------------------
            
            
            simple_query = '''

            SELECT
                case when (conexao.ultimo_bloqueio_auto between '{}' AND '{}') THEN TO_DATE('{}', 'MM/YYYY') end as dt_bloqueio,
                count(contrato.codcontrato)
                    
            from public.mk_contratos contrato
            inner join public.mk_pessoas pessoa on (pessoa.codpessoa = contrato.cliente)
            inner join public.mk_cidades cidade on (pessoa.codcidade = cidade.codcidade)
            inner join public.mk_conexoes conexao on (contrato.codcontrato = conexao.contrato)

            where contrato.cancelado = 'N'
            and (contrato.suspenso = 'N' OR contrato.suspenso IS NULL)
            and conexao.tipo_conexao = 1
            and conexao.conexao_bloqueada = 'S'
            and conexao.ultimo_bloqueio_auto between '{}' AND '{}'

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
                

        Save_to_SQL.save_querys(complete_query, 'bloqueio', 'bloqueios_total_por_mes')
        return str(complete_query)

    def evolucao_bloqueios_por_cidade(self): # MK - OK OK OK

        # Variaveis
        # -------------------------
        self.name_columns = ['Data', 'Cidade', 'Quantidade']
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
                SELECT
                    case when (conexao.ultimo_bloqueio_auto between '{}' AND '{}') THEN TO_DATE('{}', 'MM/YYYY')
                    end as dt_bloqueio,
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
                    count(contrato.codcontrato)
                        
                from public.mk_contratos contrato
                inner join public.mk_pessoas pessoa on (pessoa.codpessoa = contrato.cliente)
                inner join public.mk_cidades cidade on (pessoa.codcidade = cidade.codcidade)
                inner join public.mk_conexoes conexao on (contrato.codcontrato = conexao.contrato)

                where contrato.cancelado = 'N'
                and (contrato.suspenso = 'N' OR contrato.suspenso IS NULL)
                and conexao.tipo_conexao = 1
                and conexao.conexao_bloqueada = 'S'
                and (conexao.ultimo_bloqueio_auto between '{}' AND '{}')

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

            # Final da Query para Datas NULL
            end_simple_query = ''' 
                UNION

                SELECT
                    case when (conexao.ultimo_bloqueio_auto IS NULL) THEN 'DATA NULL'
                    end as dt_bloqueio,
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
                    count(contrato.codcontrato)
                        
                from public.mk_contratos contrato
                inner join public.mk_pessoas pessoa on (pessoa.codpessoa = contrato.cliente)
                inner join public.mk_cidades cidade on (pessoa.codcidade = cidade.codcidade)
                inner join public.mk_conexoes conexao on (contrato.codcontrato = conexao.contrato)

                where contrato.cancelado = 'N'
                and (contrato.suspenso = 'N' OR contrato.suspenso IS NULL)
                and conexao.tipo_conexao = 1
                and conexao.conexao_bloqueada = 'S'
                and (conexao.ultimo_bloqueio_auto IS NULL)

                GROUP BY 1,2
            '''

            if x != (self.dates_.range_meses - 1):
                complete_query = complete_query + simple_query + '''UNION'''
            else:
                # complete_query = complete_query + simple_query + end_simple_query + '''ORDER BY  2,  1;'''
                complete_query = complete_query + simple_query + '''ORDER BY  2,  1;'''



        Save_to_SQL.save_querys(complete_query, 'bloqueio', 'evolucao_bloqueios_por_cidade')
        return str(complete_query)

    def evolucao_bloqueios_totais_por_mes(self): # MK - OK OK OK

        # Variaveis
        # -------------------------
        self.name_columns = ['Data', 'Quantidade']
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
                SELECT
                    case when (conexao.ultimo_bloqueio_auto between '{}' AND '{}') THEN TO_DATE('{}', 'MM/YYYY')
                    end as dt_bloqueio,
                    count(contrato.codcontrato)
                        
                from public.mk_contratos contrato
                inner join public.mk_pessoas pessoa on (pessoa.codpessoa = contrato.cliente)
                inner join public.mk_cidades cidade on (pessoa.codcidade = cidade.codcidade)
                inner join public.mk_conexoes conexao on (contrato.codcontrato = conexao.contrato)

                where contrato.cancelado = 'N'
                and (contrato.suspenso = 'N' OR contrato.suspenso IS NULL)
                and conexao.tipo_conexao = 1
                and conexao.conexao_bloqueada = 'S'
                and (conexao.ultimo_bloqueio_auto between '{}' AND '{}')

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

            end_simple_query = '''
                    UNION

                    SELECT
                        case when (conexao.ultimo_bloqueio_auto IS NULL) THEN 'DATA NULL'
                        end as dt_bloqueio,
                        count(contrato.codcontrato)
                            
                    from public.mk_contratos contrato
                    inner join public.mk_pessoas pessoa on (pessoa.codpessoa = contrato.cliente)
                    inner join public.mk_cidades cidade on (pessoa.codcidade = cidade.codcidade)
                    inner join public.mk_conexoes conexao on (contrato.codcontrato = conexao.contrato)

                    where contrato.cancelado = 'N'
                    and (contrato.suspenso = 'N' OR contrato.suspenso IS NULL)
                    and conexao.tipo_conexao = 1
                    and conexao.conexao_bloqueada = 'S'
                    and (conexao.ultimo_bloqueio_auto IS NULL)

                    GROUP BY 1

                '''

            if x != (self.dates_.range_meses - 1):
                complete_query = complete_query + simple_query + '''UNION'''
            else:
                # complete_query = complete_query + simple_query + end_simple_query + '''ORDER BY  1,  2;'''
                complete_query = complete_query + simple_query + '''ORDER BY  1,  2;'''



        Save_to_SQL.save_querys(complete_query, 'bloqueio', 'evolucao_bloqueios_totais_por_mes')
        return str(complete_query)

