from datetime import datetime, date
import pandas as pd
import calendar
from Env_Vars import Env_Vars



class Get_Date:

    def __init__(self, type_date ,forc_ano=None, forc_mes=None):

        default_date = Env_Vars()
        day_init, mont_init, year_init = default_date.DEFAULT_INIT_DATE_RANGE

        if forc_ano != None and forc_mes != None:
                # Get
            #-------------------------------------------
            # Get Mês
            self.mes_range = forc_mes
            # Get Ano
            self.ano_range =  forc_ano        
        else:
            # Get
            #-------------------------------------------
            # Get Mês
            self.mes_range = int(mont_init)
            # Get Ano
            self.ano_range =  int(year_init)
            #-------------------------------------------

        if type_date == 1:
            self.style_date = '%d/%m/%Y'
        elif type_date == 2:
            self.style_date = '%Y-%m-%d'


        self.list = []
        self.salve = []

        self.dates_ = self.generate_date()
        self.range_meses = self.count_range()

    def generate_date(self):


        # Atual
        #-------------------------------------------
        # Mês Atual
        month_today = int(datetime.now().strftime('%m'))
        # Ano Atual
        year_today = int(datetime.now().strftime('%Y'))
        #-------------------------------------------

        while True:

            last_day_month = calendar.monthrange(self.ano_range, self.mes_range)[-1]

            data_inicial = date(self.ano_range, self.mes_range, 1) #.strftime('%Y/%m/%d') # Modificado formato
            data_final = date(self.ano_range, self.mes_range, last_day_month) # Formato padrão
            period = date(self.ano_range, self.mes_range, 1).strftime('%m/%Y') # Formato periodo

            # print('Inicio :|{}| Fim: |{}| MÊS: |{}|'.format(data_inicial, data_final, period))


            # Count
            # ---------------------------------------------------------------------
            self.mes_range += 1

            if self.mes_range == 13:
                self.mes_range = 1
                self.ano_range += 1
            # ---------------------------------------------------------------------


            # Salve Dates
            # ---------------------------------------------------------------------
            self.list = (data_inicial, data_final, period)
            self.salve.append(self.list)
            # ---------------------------------------------------------------------

            # Break
            # ---------------------------------------------------------------------
            if self.ano_range == year_today and self.mes_range == month_today:
                break
            # ---------------------------------------------------------------------

        # return dataFrame list of date
        df = pd.DataFrame(self.salve, columns=["Data_Inicial","Data_Final","Periodo"])

        return df

    def dates_personalizadas(self, index_):

        # função para personalizar o formato de data para ser realiozado a pesquisa

        inicio = str(self.dates_.Data_Inicial[index_].strftime(self.style_date))
        final = str(self.dates_.Data_Final[index_].strftime(self.style_date))
        periodo = str(self.dates_.Periodo[index_])

        return (inicio, final, periodo)

    def count_range(self):
        return len(self.dates_.Periodo)