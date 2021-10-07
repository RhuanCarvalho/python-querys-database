import os
from Consultas.Consulta import Resultado_Consultas_MK

start = Resultado_Consultas_MK()

start.Auto_()
os.system('taskkill /IM "EXCEL.EXE" /F')
