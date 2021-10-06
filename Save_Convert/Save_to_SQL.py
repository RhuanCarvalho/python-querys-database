from Env_Vars import Env_Vars

class Save_to_SQL:
    def __init__(self):
        pass
    
    def save_querys(self, complete_query, path_save, name_arq):
        '''
        Função para salvar a string gerada em arquivos .sql

        * Params: 
        - complete_query(str): string que possui a consulta
        - path(str): nome da pasta de destino
        - name_aqr (str): nome do arquivo 
        '''

        local = Env_Vars()

        file = open(local.SAVE_QUERYS_MK + '{}/{}.sql'.format(path_save, name_arq), 'w')
        file.write(complete_query)
        file.close()