import os
from Consultas.Consulta import Resultado_Consultas_MK

teste = Resultado_Consultas_MK()

teste.Auto_()
os.system('taskkill /IM "EXCEL.EXE" /F')
