import pandas as pd
from DataBase.Connect_DB import Person

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
        
        self.consulta = Person()

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

    #--------------------------------
    # Returns Consultas de bloqueio
    #-------------------------------- 
    def bloqueios_por_cidades(self):
        result = self.consulta.query(self.bloqueio_MK.bloqueios_por_cidades())
        result_DataFrame = pd.DataFrame(result)
        result_DataFrame.columns = self.bloqueio_MK.name_columns
        return (result, result_DataFrame, self.bloqueio_MK.name_columns)
        
    def bloqueios_total_por_mes(self):
        result = self.consulta.query(self.bloqueio_MK.bloqueios_total_por_mes())
        result_DataFrame = pd.DataFrame(result)  
        result_DataFrame.columns = self.bloqueio_MK.name_columns
        return (result, result_DataFrame, self.bloqueio_MK.name_columns)

    def evolucao_bloqueios_por_cidade(self):
        result = self.consulta.query(self.bloqueio_MK.evolucao_bloqueios_por_cidade())
        result_DataFrame = pd.DataFrame(result)
        result_DataFrame.columns = self.bloqueio_MK.name_columns
        return (result, result_DataFrame, self.bloqueio_MK.name_columns)

    def evolucao_bloqueios_totais_por_mes(self):
        result = self.consulta.query(self.bloqueio_MK.evolucao_bloqueios_totais_por_mes())
        result_DataFrame = pd.DataFrame(result) 
        result_DataFrame.columns = self.bloqueio_MK.name_columns
        return (result, result_DataFrame, self.bloqueio_MK.name_columns)

    #--------------------------------
    # Returns Consultas de cancelamento
    #--------------------------------
    def cancelamentos_por_cidades(self):
        result = self.consulta.query(self.cancelamento_MK.cancelamentos_por_cidades())
        result_DataFrame = pd.DataFrame(result)
        result_DataFrame.columns = self.cancelamento_MK.name_columns
        return (result, result_DataFrame, self.cancelamento_MK.name_columns)

    def cancelamentos_geral_por_mes(self):
        result = self.consulta.query(self.cancelamento_MK.cancelamentos_geral_por_mes())
        result_DataFrame = pd.DataFrame(result)
        result_DataFrame.columns = self.cancelamento_MK.name_columns
        return (result, result_DataFrame, self.cancelamento_MK.name_columns)
    
    #--------------------------------
    # Returns Consultas de Vendas
    #--------------------------------
    def vendas_por_cidades(self):
        result = self.consulta.query(self.vendas_MK.vendas_por_cidades())
        result_DataFrame = pd.DataFrame(result)
        result_DataFrame.columns = self.vendas_MK.name_columns
        return (result, result_DataFrame, self.vendas_MK.name_columns)

    def vendas_geral_por_mes(self):
        result = self.consulta.query(self.vendas_MK.vendas_geral_por_mes())
        result_DataFrame = pd.DataFrame(result)
        result_DataFrame.columns = self.vendas_MK.name_columns
        return (result, result_DataFrame, self.vendas_MK.name_columns)

    #--------------------------------
    # Returns Consultas de Faturamento
    #--------------------------------
    def faturamento_por_cidades(self):
        result = self.consulta.query(self.faturamento_MK.faturamento_por_cidades())
        result_DataFrame = pd.DataFrame(result)
        result_DataFrame.columns = self.faturamento_MK.name_columns
        return (result, result_DataFrame, self.faturamento_MK.name_columns)

    def faturamento_geral_por_mes(self):
        result = self.consulta.query(self.faturamento_MK.faturamento_geral_por_mes())
        result_DataFrame = pd.DataFrame(result)
        result_DataFrame.columns = self.faturamento_MK.name_columns
        return (result, result_DataFrame, self.faturamento_MK.name_columns)
    
    #--------------------------------
    # Returns Consultas de Pagamentos
    #--------------------------------
    def pagamentos_geral(self):
        result = self.consulta.query(self.pagamentos_MK.pagamentos_geral())
        result_DataFrame = pd.DataFrame(result)
        result_DataFrame.columns = self.pagamentos_MK.name_columns
        return (result, result_DataFrame, self.pagamentos_MK.name_columns)

    #--------------------------------
    # Returns Consutas de Recebimento
    #--------------------------------
    def recebimentos_por_cidades(self):
        result = self.consulta.query(self.recebimentos_MK.recebimentos_por_cidades())
        result_DataFrame = pd.DataFrame(result)
        result_DataFrame.columns = self.recebimentos_MK.name_columns
        return (result, result_DataFrame, self.recebimentos_MK.name_columns)
    
    def recebimentos_geral_por_mes(self):
        result = self.consulta.query(self.recebimentos_MK.recebimentos_geral_por_mes())
        result_DataFrame = pd.DataFrame(result)
        result_DataFrame.columns = self.recebimentos_MK.name_columns
        return (result, result_DataFrame, self.recebimentos_MK.name_columns)

    #--------------------------------
    #Returns Consultas Evolução SPC
    #--------------------------------
    def evolucao_spc_cadastradas(self):
        result = self.consulta.query(self.evolucao_spc_MK.evolucao_cadastros_SPC())
        result_DataFrame = pd.DataFrame(result)
        result_DataFrame.columns = self.evolucao_spc_MK.name_columns
        return (result, result_DataFrame, self.evolucao_spc_MK.name_columns)

    def evolucao_spc_retiradas(self):
        result = self.consulta.query(self.evolucao_spc_MK.evolucao_retiradas_SPC())
        result_DataFrame = pd.DataFrame(result)
        result_DataFrame.columns = self.evolucao_spc_MK.name_columns
        return (result, result_DataFrame, self.evolucao_spc_MK.name_columns)

    def spc_cadastradas_mensal(self):
        result = self.consulta.query(self.evolucao_spc_MK.cadastros_SPC_mensal())
        result_DataFrame = pd.DataFrame(result)
        result_DataFrame.columns = self.evolucao_spc_MK.name_columns
        return (result, result_DataFrame, self.evolucao_spc_MK.name_columns)

    def spc_retiradas_mensal(self):
        result = self.consulta.query(self.evolucao_spc_MK.retiradas_SPC_mensal())
        result_DataFrame = pd.DataFrame(result)
        result_DataFrame.columns = self.evolucao_spc_MK.name_columns
        return (result, result_DataFrame, self.evolucao_spc_MK.name_columns)

    #--------------------------------
    #Returns Evolução de Base
    #--------------------------------
    def evolucao_contratos_cancelados_por_cidades(self):
        result = self.consulta.query(self.evulacao_de_base_MK.evolucao_contratos_cancelados_por_cidades())
        result_DataFrame = pd.DataFrame(result)
        result_DataFrame.columns = self.evulacao_de_base_MK.name_columns
        return (result, result_DataFrame, self.evulacao_de_base_MK.name_columns)

    def evolucao_contratos_criados_por_cidades(self):
        result = self.consulta.query(self.evulacao_de_base_MK.evolucao_contratos_criados_por_cidades())
        result_DataFrame = pd.DataFrame(result)
        result_DataFrame.columns = self.evulacao_de_base_MK.name_columns
        return (result, result_DataFrame, self.evulacao_de_base_MK.name_columns)

    def evolucao_contratos_criados_e_cancelados_totais(self):
        result = self.consulta.query(self.evulacao_de_base_MK.evolucao_contratos_criados_e_cancelados_totais())
        result_DataFrame = pd.DataFrame(result)
        result_DataFrame.columns = self.evulacao_de_base_MK.name_columns
        return (result, result_DataFrame, self.evulacao_de_base_MK.name_columns)


    #--------------------------------
    #Returns Evolução de Base Sem Migracao
    #--------------------------------
    def evolucao_contratos_cancelados_por_cidades_sem_migracao(self):
        result = self.consulta.query(self.evolucao_base_sem_migracao_MK.evolucao_contratos_cancelados_por_cidades())
        result_DataFrame = pd.DataFrame(result)
        result_DataFrame.columns = self.evolucao_base_sem_migracao_MK.name_columns
        return (result, result_DataFrame, self.evolucao_base_sem_migracao_MK.name_columns)

    def evolucao_contratos_criados_por_cidades_sem_migracao(self):
        result = self.consulta.query(self.evolucao_base_sem_migracao_MK.evolucao_contratos_criados_por_cidades())
        result_DataFrame = pd.DataFrame(result)
        result_DataFrame.columns = self.evolucao_base_sem_migracao_MK.name_columns
        return (result, result_DataFrame, self.evolucao_base_sem_migracao_MK.name_columns)

    def evolucao_contratos_criados_e_cancelados_totais_sem_migracao(self):
        result = self.consulta.query(self.evolucao_base_sem_migracao_MK.evolucao_contratos_criados_e_cancelados_totais())
        result_DataFrame = pd.DataFrame(result)
        result_DataFrame.columns = self.evolucao_base_sem_migracao_MK.name_columns
        return (result, result_DataFrame, self.evolucao_base_sem_migracao_MK.name_columns)

    #--------------------------------
    #Returns Inadimplencia
    #--------------------------------
    def inadimplencia_total_por_mes(self):
        result = self.consulta.query(self.indimplencia_MK.inadimplencia_total_por_mes())
        result_DataFrame = pd.DataFrame(result)  
        result_DataFrame.columns = self.indimplencia_MK.name_columns
        return (result, result_DataFrame, self.indimplencia_MK.name_columns)

    def inadimplencia_por_cidades(self):
        result = self.consulta.query(self.indimplencia_MK.inadimplencia_por_cidades())
        result_DataFrame = pd.DataFrame(result)
        result_DataFrame.columns = self.indimplencia_MK.name_columns
        return (result, result_DataFrame, self.indimplencia_MK.name_columns)

    def evolucao_inadimplencia_por_cidade(self):
        result = self.consulta.query(self.indimplencia_MK.evolucao_inadimplencia_por_cidade())
        result_DataFrame = pd.DataFrame(result)
        result_DataFrame.columns = self.indimplencia_MK.name_columns
        return (result, result_DataFrame, self.indimplencia_MK.name_columns)

    def evolucao_inadimplencia_totais_por_mes(self):
        result = self.consulta.query(self.indimplencia_MK.evolucao_inadimplencia_totais_por_mes())
        result_DataFrame = pd.DataFrame(result) 
        result_DataFrame.columns = self.indimplencia_MK.name_columns
        return (result, result_DataFrame, self.indimplencia_MK.name_columns)
