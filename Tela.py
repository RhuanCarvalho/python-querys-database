import PySimpleGUI as sg, pandas as pd, os


class Tela:
    
    def __init__(self):
        pass

    def type_consultas(self):

        sg.theme('Reddit')

        layout = [
            [sg.Text('Quais Consultas deseja realizar?')],
            [sg.Checkbox('Bloqueio',                        default=True, key='Bloqueio')],
            [sg.Checkbox('Evolucao Bloqueio',               default=True, key='Evolucao_Bloqueio')],
            [sg.Checkbox('Cancelamento',                    default=True, key='Cancelamento')],
            [sg.Checkbox('Vendas',                          default=True, key='Vendas')],
            [sg.Checkbox('Faturamento',                     default=True, key='Faturamento')],
            [sg.Checkbox('Pagamentos',                      default=True, key='Pagamentos')],
            [sg.Checkbox('Recebimento',                     default=True, key='Recebimento')],
            [sg.Checkbox('SPC',                             default=True, key='SPC')],
            [sg.Checkbox('Inadimplencia',                   default=True, key='Inadimplencia')],
            [sg.Checkbox('Evolucao Inadimplencia',          default=True, key='Evolucao_Inadimplencia')],
            [sg.Checkbox('Evolução de Base',                default=True, key='Evolucao_de_Base')],
            [sg.Checkbox('Evolução de Base Sem Migracao',   default=True, key='Evolucao_de_Base_Sem_Migracao')],
            [sg.Button('Start')]
        ]

        return sg.Window('Start', layout=layout, finalize=True)
        
        
    def values_(self):
        df_values = []

        list_ = [
        int(self.values['Bloqueio']),
        int(self.values['Evolucao_Bloqueio']),
        int(self.values['Cancelamento']),
        int(self.values['Vendas']),
        int(self.values['Faturamento']),
        int(self.values['Pagamentos']),
        int(self.values['Recebimento']),
        int(self.values['SPC']),
        int(self.values['Inadimplencia']),
        int(self.values['Evolucao_Inadimplencia']),
        int(self.values['Evolucao_de_Base']),
        int(self.values['Evolucao_de_Base_Sem_Migracao'])
        ]
        df_values.append(list_)
        df = pd.DataFrame(df_values, columns=[
            'Bloqueio',
            'Evolucao_Bloqueio',
            'Cancelamento',
            'Vendas',
            'Faturamento',
            'Pagamentos',
            'Recebimento',
            'SPC',
            'Inadimplencia',
            'Evolucao_Inadimplencia',
            'Evolucao_de_Base',
            'Evolucao_de_Base_Sem_Migracao'
        ])
        df.to_csv('default.txt')
        # return df.iloc[0]


    def start(self, function_):
        
        window_one = self.type_consultas()

        # Criando Janelas 
        self.window, self.event, self.values = sg.read_all_windows() 


        while True:
            
            if self.window == window_one:
                if self.event == 'Start':
                    self.window.hide()
                    self.values_()
                    function_()
                    break
        
        
         
        
        
        
           