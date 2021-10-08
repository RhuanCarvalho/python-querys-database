import os
from Consultas.Consulta import Resultado_Consultas_MK
from Tela import Tela

tela = Tela()
start = Resultado_Consultas_MK()

tela.start(start.Auto_)

os.system('taskkill /IM "EXCEL.EXE" /F')
