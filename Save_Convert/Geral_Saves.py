import pandas as pd

from Env_Vars import Env_Vars
from DataBase.Connect_DB import Person

from Save_Convert.configs.Save_to_SQL import Save_to_SQL
from Save_Convert.configs.Save_to_Excel import Save_to_Excel
from Save_Convert.configs.Save_to_PDF import Save_to_PDF


class Geral_Save:

    def __init__(self):
        self.consulta = Person()
        self.envs = Env_Vars()
        self.sql = Save_to_SQL()
        self.excel = Save_to_Excel()
        self.pdf = Save_to_PDF()

        self.resultado = ()

    def create_df(self, query_sql, name_columns):

        result = self.consulta.query(query_sql)

        result_DataFrame = pd.DataFrame(result)
        result_DataFrame.columns = name_columns

        return (result, result_DataFrame)

    def saves(
        self,
        numero_de_querys,
        querys_sql,
        path_querys,
        names_arquivos,
        names_columns,
        name_consulta
    ):

        self.resultado = ()

        for x in range(numero_de_querys):

            # SAVE SQL - OK
            # -----------------------
            self.sql.save_querys(   #
                querys_sql[x],      #
                path_querys,        #
                names_arquivos[x]   #
            )                       #
            # -----------------------

            # SAVE CSV - OK
            # -----------------------------------------------------------------------
            result = ()                                                             #
            resultado, df_ = self.create_df(querys_sql[x], names_columns[x])        #
            result = tuple(resultado)                                               #
            self.resultado += (result,)                                             #
                                                                                    #
            df_.to_csv(self.envs.SAVE_CSV_MK + str(names_arquivos[x]) + '.csv')     #
            # -----------------------------------------------------------------------

        # SAVE EXCEL
        # ---------------------------------------------------
        # Simple Query                                      #
        if numero_de_querys == 1:                           #
            self.excel.Create_Simple_return(                #
                self.resultado[0],                          #
                name_consulta+'.xlsx',                      #
                names_columns[0],                           #
                name_consulta                               #
            )                                               #
        # ---------------------------------------------------
        # Query City and Month                              # 
        if numero_de_querys == 2:                           #
            self.excel.Create_Cidades_e_Geral(              #
                self.resultado[0],                          #
                self.resultado[1],                          #
                name_consulta+'.xlsx',                      #
                names_columns[0],                           #
                name_consulta                               #
            )                                               #
        # ---------------------------------------------------
        # Query Evolução de Base                            #      
        elif numero_de_querys == 3:                         #
            self.excel.Create_evolucao_base(                #
                self.resultado[0],                          #
                self.resultado[1],                          #
                self.resultado[2],                          #
                name_consulta+'.xlsx',                      #
                names_columns[3],                           #
                name_consulta                               #
            )                                               #
        # ---------------------------------------------------

        # SAVE PDF
        # -------------------------------
        self.pdf.excel_to_pdf(          #
            name_consulta+'.xlsx',      #
            name_consulta               #
        )                               #
        # -------------------------------
