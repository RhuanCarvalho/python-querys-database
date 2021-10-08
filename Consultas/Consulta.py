import pandas as pd, os
from Save_Convert.Geral_Saves import Geral_Save
# Esses imports retornam apenas a query e não o resultado delas
# -------------------------------------------------------------
from Querys.Querys_Bloqueios_MK                     import Querys_de_Bloqueio_MK
from Querys.Querys_Cancelamentos_MK                 import Querys_de_Cancelamentos_MK
from Querys.Querys_Vendas_MK                        import Querys_de_Vendas_MK
from Querys.Querys_Faturamento_MK                   import Querys_de_Faturamento_MK
from Querys.Querys_Pagamentos_MK                    import Querys_de_Pagamentos_MK
from Querys.Querys_Recebimentos_MK                  import Querys_de_Recebimentos_MK
from Querys.Querys_SPC_Cadastros_e_Retiradas        import Querys_SPC_Cadastros_e_Retiradas_MK
from Querys.Querys_Evolucao_de_Base                 import Querys_Evolucao_de_Base_MK
from Querys.Querys_Inadimplencia                    import Querys_de_Inadimplencia_MK
from Querys.Querys_Evolucao_de_Base_sem_migracao    import Querys_Evolucao_de_Base_sem_migracao_MK

##################
# MK
##################
class Resultado_Consultas_MK:
    
    def __init__(self):

        self.geral = Geral_Save()
        
        self.bloqueio_MK =                      Querys_de_Bloqueio_MK() 
        self.cancelamento_MK =                  Querys_de_Cancelamentos_MK() 
        self.vendas_MK =                        Querys_de_Vendas_MK()
        self.faturamento_MK =                   Querys_de_Faturamento_MK()
        self.pagamentos_MK =                    Querys_de_Pagamentos_MK()
        self.recebimentos_MK =                  Querys_de_Recebimentos_MK()
        self.evolucao_spc_MK =                  Querys_SPC_Cadastros_e_Retiradas_MK()
        self.evulacao_de_base_MK =              Querys_Evolucao_de_Base_MK()
        self.indimplencia_MK =                  Querys_de_Inadimplencia_MK()
        self.evolucao_base_sem_migracao_MK =    Querys_Evolucao_de_Base_sem_migracao_MK() 

    # Type Colunms
        #-----------------------------------------------------
        self.type_column_DCQ    = ['Data','Cidade','Quantidade']    
        self.type_column_DQ     = ['Data','Quantidade']    
        self.type_column_DCV    = ['Data','Cidade','Valor']    
        self.type_column_DV     = ['Data','Valor']    
        self.type_column_DQQ    = ['Data','Quantidade', 'Quantidade']    
        #-----------------------------------------------------

    # Paths SQL saves

        self.bloqueio                       = 'bloqueio' 
        self.cancelamento                   = 'cancelamento' 
        self.evolucao_base                  = 'evolucao_base' 
        self.evolucao_base_sem_migracao     = 'evolucao_base_sem_migracao'
        self.faturamento                    = 'faturamento' 
        self.inadimplencia                  = 'inadimplencia'
        self.pagamento                      = 'pagamento' 
        self.recebimento                    = 'recebimento'
        self.spc                            = 'spc'
        self.venda                          = 'venda'


    def Auto_ (self):
        vars_ = pd.DataFrame(pd.read_csv(os.path.abspath('default.txt'))).iloc[0]

    #--------------------------------
    # Bloqueio
    #-------------------------------- 
        if vars_.Bloqueio:
            print('\nBloqueio')
            self.geral.saves(
                numero_de_querys    = 2,
                querys_sql          = [
                    self.bloqueio_MK.bloqueios_por_cidades(),
                    self.bloqueio_MK.bloqueios_total_por_mes()
                    ],
                path_querys         = self.bloqueio,
                names_arquivos      = [
                    'bloqueios_por_cidades',
                    'bloqueios_total_por_mes'
                    ],
                names_columns       = [self.type_column_DCQ, self.type_column_DQ],
                name_consulta       = 'Bloqueio'
                )

    #--------------------------------
    # Evolucao Bloqueio
    #-------------------------------- 
        if vars_.Evolucao_Bloqueio:
            print('\nEvolucao Bloqueio')
            self.geral.saves(
                numero_de_querys    = 2,
                querys_sql          = [
                    self.bloqueio_MK.evolucao_bloqueios_por_cidade(), 
                    self.bloqueio_MK.evolucao_bloqueios_totais_por_mes()
                    ],
                path_querys         = self.bloqueio,
                names_arquivos      = [
                    'evolucao_bloqueios_por_cidade',
                    'evolucao_bloqueios_totais_por_mes'
                    ],
                names_columns       = [self.type_column_DCQ, self.type_column_DQ],
                name_consulta       = 'Evolucao Bloqueio'
                )
        
    #--------------------------------
    # Cancelamento
    #--------------------------------
        if vars_.Cancelamento:
            print('\nCancelamento')
            self.geral.saves(
                numero_de_querys    = 2,
                querys_sql          = [
                    self.cancelamento_MK.cancelamentos_por_cidades(),
                    self.cancelamento_MK.cancelamentos_geral_por_mes()
                    ],
                path_querys         = self.cancelamento,
                names_arquivos      = [
                    'cancelamentos_por_cidades',
                    'cancelamentos_geral_por_mes'
                    ],
                names_columns       = [self.type_column_DCQ, self.type_column_DQ],
                name_consulta       = 'Cancelamento'
                )

    #--------------------------------
    # Vendas
    #--------------------------------
        if vars_.Vendas:
            print('\nVendas')
            self.geral.saves(
                numero_de_querys    = 2,
                querys_sql          = [
                    self.vendas_MK.vendas_por_cidades(), 
                    self.vendas_MK.vendas_geral_por_mes()
                    ],
                path_querys         = self.venda,
                names_arquivos      = [
                    'vendas_por_cidades',
                    'vendas_geral_por_mes'
                    ],
                names_columns       = [self.type_column_DCQ, self.type_column_DQ],
                name_consulta       = 'Vendas'
                )

    #--------------------------------
    # Faturamento
    #--------------------------------
        if vars_.Faturamento:
            print('\nFaturamento')
            self.geral.saves(
                numero_de_querys    = 2,
                querys_sql          = [
                    self.faturamento_MK.faturamento_por_cidades(), 
                    self.faturamento_MK.faturamento_geral_por_mes()
                    ],
                path_querys         = self.faturamento,
                names_arquivos      = [
                    'faturamento_por_cidades',
                    'faturamento_geral_por_mes'
                    ],
                names_columns       = [self.type_column_DCV, self.type_column_DV],
                name_consulta       = 'Faturamento'
                )
    
    #--------------------------------
    # Pagamentos
    #--------------------------------
        if vars_.Pagamentos:
            print('\nPagamentos')
            self.geral.saves(
                numero_de_querys    = 1,
                querys_sql          = [self.pagamentos_MK.pagamentos_geral()],
                path_querys         = self.pagamento,
                names_arquivos      = ['pagamentos_geral'],
                names_columns       = [self.type_column_DV],
                name_consulta       = 'Pagamentos'
                )

    #--------------------------------
    # Recebimento
    #--------------------------------
        if vars_.Recebimento:
            print('\nRecebimento')
            self.geral.saves(
                numero_de_querys    = 2,
                querys_sql          = [
                    self.recebimentos_MK.recebimentos_por_cidades(), 
                    self.recebimentos_MK.recebimentos_geral_por_mes()
                    ],
                path_querys         = self.recebimento,
                names_arquivos      = [
                    'recebimentos_por_cidades',
                    'recebimentos_geral_por_mes'
                    ],
                names_columns       = [self.type_column_DCV, self.type_column_DV],
                name_consulta       = 'Recebimento'
                )

    #--------------------------------
    # SPC 
    #--------------------------------
        if vars_.SPC :
            print('\nSPC ')
            self.geral.saves(
                numero_de_querys    = 1,
                querys_sql          = [self.evolucao_spc_MK.cadastros_SPC_mensal()],
                path_querys         = self.spc,
                names_arquivos      = ['cadastros_SPC_mensal'],
                names_columns       = [self.type_column_DV],
                name_consulta       = 'SPC Cadastro Mensal'
                )

            self.geral.saves(
                numero_de_querys    = 1,
                querys_sql          = [self.evolucao_spc_MK.retiradas_SPC_mensal()],
                path_querys         = self.spc,
                names_arquivos      = ['retiradas_SPC_mensal'],
                names_columns       = [self.type_column_DV],
                name_consulta       = 'SPC Retiradas Mensal'
                )

            self.geral.saves(
                numero_de_querys    = 1,
                querys_sql          = [self.evolucao_spc_MK.evolucao_cadastros_SPC()],
                path_querys         = self.spc,
                names_arquivos      = ['evolucao_cadastros_SPC'],
                names_columns       = [self.type_column_DV],
                name_consulta       = 'SPC Evolucao Cadastros '
                )

            self.geral.saves(
                numero_de_querys    = 1,
                querys_sql          = [self.evolucao_spc_MK.evolucao_retiradas_SPC()],
                path_querys         = self.spc,
                names_arquivos      = ['evolucao_retiradas_SPC'],
                names_columns       = [self.type_column_DV],
                name_consulta       = 'SPC Evolucao Retiradas '
                )

    #--------------------------------
    # Inadimplencia
    #--------------------------------
        if vars_.Inadimplencia:
            print('\nInadimplencia')
            self.geral.saves(
                numero_de_querys    = 2,
                querys_sql          = [
                    self.indimplencia_MK.inadimplencia_por_cidades(), 
                    self.indimplencia_MK.inadimplencia_total_por_mes()
                    ],
                path_querys         = self.inadimplencia,
                names_arquivos      = [
                    'inadimplencia_por_cidades',
                    'inadimplencia_total_por_mes'
                    ],
                names_columns       = [self.type_column_DCV, self.type_column_DV],
                name_consulta       = 'Inadimplencia'
                )

    #--------------------------------
    # Evolucao Inadimplencia
    #--------------------------------
        if vars_.Evolucao_Inadimplencia:
            print('\nEvolucao Inadimplencia')
            self.geral.saves(
                numero_de_querys    = 2,
                querys_sql          = [
                    self.indimplencia_MK.evolucao_inadimplencia_por_cidade(), 
                    self.indimplencia_MK.evolucao_inadimplencia_totais_por_mes()
                    ],
                path_querys         = self.inadimplencia,
                names_arquivos      = [
                    'evolucao_inadimplencia_por_cidade',
                    'evolucao_inadimplencia_totais_por_mes'
                    ],
                names_columns       = [self.type_column_DCV, self.type_column_DV],
                name_consulta       = 'Evolucao Inadimplencia'
                )

    #--------------------------------
    # Evolução de Base
    #--------------------------------
        if vars_.Evolucao_de_Base :
            print('\nEvolução de Base')    
            self.geral.saves(
                numero_de_querys     = 3,
                querys_sql           = [
                    self.evulacao_de_base_MK.evolucao_contratos_criados_por_cidades(), 
                    self.evulacao_de_base_MK.evolucao_contratos_cancelados_por_cidades(), 
                    self.evulacao_de_base_MK.evolucao_contratos_criados_e_cancelados_totais()
                    ],
                path_querys          = self.evolucao_base,
                names_arquivos       = [
                    'evolucao_contratos_criados_por_cidades',
                    'evolucao_contratos_cancelados_por_cidades', 
                    'evolucao_contratos_criados_e_cancelados_totais'
                    ],
                names_columns        = [self.type_column_DCQ, self.type_column_DCQ, self.type_column_DQQ,['Data','Cidade', 'Contratos_Criados', 'Constratos_Cancelados', 'Contratos_Ativos']],
                name_consulta        = 'Evolucao de Base'
                )

    #--------------------------------
    # Evolução de Base Sem Migracao
    #--------------------------------
        if vars_.Evolucao_de_Base_Sem_Migracao:
            print('\nEvolução de Base Sem Migracao')     
            self.geral.saves(
                numero_de_querys     = 3,
                querys_sql           = [
                    self.evolucao_base_sem_migracao_MK.evolucao_contratos_criados_por_cidades(), 
                    self.evolucao_base_sem_migracao_MK.evolucao_contratos_cancelados_por_cidades(), 
                    self.evolucao_base_sem_migracao_MK.evolucao_contratos_criados_e_cancelados_totais()
                    ],
                path_querys          = self.evolucao_base_sem_migracao,
                names_arquivos       = [
                    'evolucao_contratos_criados_por_cidades_sem_migracao',
                    'evolucao_contratos_cancelados_por_cidades_sem_migracao', 
                    'evolucao_contratos_criados_e_cancelados_totais_sem_migracao'
                    ],
                names_columns        = [self.type_column_DCQ, self.type_column_DCQ, self.type_column_DQQ, ['Data','Cidade', 'Contratos_Criados', 'Constratos_Cancelados', 'Contratos_Ativos']],
                name_consulta        = 'Evolucao de Base Sem Migracao'
                )