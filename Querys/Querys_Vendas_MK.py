from Consultas.Get_Date import Get_Date

class Querys_de_Vendas_MK:

    def __init__(self):
        # -----------------------------------------------------
        #Config Periodo de Consultas
        self.dates_ = Get_Date( type_date = 1 )
        # -----------------------------------------------------


    def vendas_por_cidades(self): 
        
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
            
                select distinct
                    case when (contrato.adesao between '{}' AND '{}') THEN TO_DATE('{}', 'MM/YYYY') end as adesao,
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
                    COUNT(contrato.codcontrato) AS vendas

                from public.mk_contratos contrato

                inner join public.mk_pessoas pessoa on (pessoa.codpessoa = contrato.cliente)
                inner join public.mk_cidades cidade on (pessoa.codcidade = cidade.codcidade)
                inner join public.mk_planos_acesso plano on (plano.codplano = contrato.plano_acesso)

                where contrato.adesao between '{}' AND '{}'
                and upper(plano.descricao) not like '%TELEFONIA%'
                and upper(pessoa.nome_razaosocial) not like '%CLIENTE%'
                and contrato.cancelado = 'N'
                and (contrato.suspenso = 'N' OR contrato.suspenso IS NULL)
                and (upper(pessoa.observacoes) not like '%INF%' OR pessoa.observacoes IS NULL)

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
                complete_query = complete_query + simple_query + '''ORDER BY 2 ASC, 1 ASC;'''

        return str(complete_query)
        
    def vendas_geral_por_mes(self): 
        
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
            
            select distinct
                case when (contrato.adesao between '{}' AND '{}') THEN TO_DATE('{}', 'MM/YYYY') end as adesao,
                COUNT(contrato.codcontrato) AS vendas

            from public.mk_contratos contrato

            inner join public.mk_pessoas pessoa on (pessoa.codpessoa = contrato.cliente)
            inner join public.mk_cidades cidade on (pessoa.codcidade = cidade.codcidade)
            inner join public.mk_planos_acesso plano on (plano.codplano = contrato.plano_acesso)

            where contrato.adesao between '{}' and '{}'
            and upper(plano.descricao) not like '%TELEFONIA%'
            and upper(pessoa.nome_razaosocial) not like '%CLIENTE%'
            and contrato.cancelado = 'N'
            and (contrato.suspenso = 'N' OR contrato.suspenso IS NULL)
            and (upper(pessoa.observacoes) not like '%INF%' OR pessoa.observacoes IS NULL)

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