from win32com import client
from Env_Vars import Env_Vars
import os


class Save_to_PDF:

    def __init__(self):
        self.envs = Env_Vars()

    def excel_to_pdf(self, name_arq_with_extensao, name_consulta):

        input_file = os.path.abspath(self.envs.SAVE_EXCEL_MK + name_arq_with_extensao)
        output_file = os.path.abspath(self.envs.SAVE_PDF_MK + name_consulta + ".pdf")

        xlApp = client.Dispatch("Excel.Application")
        books = xlApp.Workbooks.Open(input_file)

        ws = books.Worksheets[0]
        ws.Visible = 1
        ws.ExportAsFixedFormat(0, output_file)
