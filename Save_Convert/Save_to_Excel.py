from Env_Vars import Env_Vars
from .configs.Style_Cells import Style
from .Save_to_PDF import Save_to_PDF
from Consultas.Get_Date import Get_Date

import xlsxwriter

class Save_to_Excel:

    def __init__(self):
        self.envs                       = Env_Vars()
        self.save_                      = Save_to_PDF()
        self.style                      = Style()
        self.dates                      = Get_Date( type_date = 1 )
        self.default_data_labels        = { 'value': True, 'legend_key': False, 'font': {'size': 12 }} 
        self.default_pattern            = { 'pattern': 'shingle', 'fg_color': '#de1a00', 'bg_color': '#de1a00' }
        self.default_border             = { 'color': '#de1a00' } 


    def Create_Cidades_e_Geral(self, relatorio_cidade, relatorio_geral, name_arq_with_extensao, name_columns, name_consulta ):
        aux = 3

        file        = xlsxwriter.Workbook(self.envs.SAVE_EXCEL_MK + name_arq_with_extensao)
        table       = file.add_worksheet()
        table_chart = file.add_worksheet()
        

        merge_format            = file.add_format(self.style.merge_format)
        cell_format_header      = file.add_format(self.style.cell_format_header)
        cell_format             = file.add_format(self.style.cell_format)
        cell_format_Currency    = file.add_format(self.style.cell_format_Currency)
        cell_bg_color           = file.add_format(self.style.cell_bg_color)
        cell_bg_color_Currency  = file.add_format(self.style.cell_bg_color_Currency)

        table.merge_range('A1:C1', name_consulta + ' por cidade', merge_format)

        table.write('A2',name_columns[0], cell_format_header)        
        table.write('B2',name_columns[1], cell_format_header)        
        table.write('C2',name_columns[2], cell_format_header)
        table.set_column('A:C', 25)

        for row in relatorio_cidade:

            cell_format = cell_format
            cell_bg_color = cell_bg_color


            if type(row[0]) != str:
                table.write('A'+str(aux), row[0].strftime('%m/%Y'), cell_format if aux % 2 else cell_bg_color)
            # else:
            #     table.write('A'+str(aux), row[0], cell_format if aux % 2 else cell_bg_color)
            table.write('B'+str(aux), row[1], cell_format if aux % 2 else cell_bg_color)

            if type(row[2]) != float:
                cell_format = cell_format
                cell_bg_color = cell_bg_color
                table.write('C'+str(aux),row[2], cell_format if aux % 2 else cell_bg_color)
            else:
                cell_format = cell_format_Currency
                cell_bg_color = cell_bg_color_Currency
                table.write_number('C'+str(aux),row[2], cell_format if aux % 2 else cell_bg_color)


            aux += 1

        table.merge_range('A{}:C{}'.format(str(aux), str(aux)), name_consulta + ' por mês', merge_format)

        aux += 1

        for row in relatorio_geral:

            cell_format = cell_format
            cell_bg_color = cell_bg_color


            if type(row[0]) != str:
                table.write('A'+str(aux), row[0].strftime('%m/%Y'), cell_format if aux % 2 else cell_bg_color)
            # else:
            #     table.write('A'+str(aux), row[0], cell_format if aux % 2 else cell_bg_color)
            table.write('B'+str(aux), 'TOTAIS', cell_format if aux % 2 else cell_bg_color)
            
            if type(row[1]) != float:
                cell_format = cell_format
                cell_bg_color = cell_bg_color
                table.write('C'+str(aux), row[1], cell_format if aux % 2 else cell_bg_color)
            else:
                cell_format = cell_format_Currency
                cell_bg_color = cell_bg_color_Currency
                table.write_number('C'+str(aux),row[1], cell_format if aux % 2 else cell_bg_color)

            aux += 1

        chart = file.add_chart({'type':'column'})
        chart.add_series({
            'name': name_consulta,
            'categories': '=Sheet1!A{}:A{}'.format(aux - self.dates.range_meses, aux - 1),
            'values': '=Sheet1!C{}:C{}'.format(aux - self.dates.range_meses, aux - 1),
            'data_labels': self.default_data_labels,
            'pattern': self.default_pattern, 
            'border': self.default_border 
        })
        chart.set_legend({ 'none': True })
        chart.set_style(2)
        chart.set_y_axis( { 'major_gridlines': { 'visible': False } } )
        chart.set_x_axis( { 'major_gridlines': { 'visible': False } } )
        table_chart.insert_chart('A1', chart)

        file.close()

        self.save_.excel_to_pdf(
            name_arq_with_extensao,
            name_consulta
        )

    def Create_Simple_return(self, relatorio, name_arq_with_extensao, name_columns, name_consulta ):
        aux = 2

        file = xlsxwriter.Workbook(self.envs.SAVE_EXCEL_MK + name_arq_with_extensao)
        table = file.add_worksheet()
        table_chart = file.add_worksheet()


        merge_format = file.add_format(self.style.merge_format)
        cell_format_header = file.add_format(self.style.cell_format_header)
        cell_format_Currency = file.add_format(self.style.cell_format_Currency)
        cell_bg_color_Currency = file.add_format(self.style.cell_bg_color_Currency)
        cell_format = file.add_format(self.style.cell_format)
        cell_bg_color = file.add_format(self.style.cell_bg_color)

        table.merge_range('A1:B1', name_consulta, merge_format)

        table.write('A2',name_columns[0], cell_format_header)        
        table.write('B2',name_columns[1], cell_format_header)  
        table.set_column('A:B', 25)

        aux += 1
        for row in relatorio:

            cell_format = cell_format
            cell_bg_color = cell_bg_color


            if type(row[0]) != str:
                table.write('A'+str(aux), row[0].strftime('%m/%Y'), cell_format if aux % 2 else cell_bg_color)
            else:
                table.write('A'+str(aux), row[0], cell_format if aux % 2 else cell_bg_color)
            
            if type(row[1]) != float:
                cell_format = cell_format
                cell_bg_color = cell_bg_color
                table.write('B'+str(aux), row[1], cell_format if aux % 2 else cell_bg_color)
            else:
                cell_format = cell_format_Currency
                cell_bg_color = cell_bg_color_Currency
                table.write_number('B'+str(aux),row[1], cell_format if aux % 2 else cell_bg_color)

            

            aux += 1

        chart = file.add_chart({'type':'column'})
        chart.add_series({
            'name': name_consulta,
            'categories': '=Sheet1!A{}:A{}'.format(aux - self.dates.range_meses, aux - 1),
            'values': '=Sheet1!B{}:B{}'.format(aux - self.dates.range_meses, aux - 1),
            'data_labels': self.default_data_labels,
            'pattern': self.default_pattern, 
            'border': self.default_border
        })
        chart.set_legend({ 'none': True })
        chart.set_style(2)
        chart.set_y_axis( { 'major_gridlines': { 'visible': False } } )
        chart.set_x_axis( { 'major_gridlines': { 'visible': False } } )
        table_chart.insert_chart('A1', chart)

        file.close()

        self.save_.excel_to_pdf(
            name_arq_with_extensao,
            name_consulta
        )

    def Create_evolucao_base(self, relatorio_criados, relatorio_cancelados, relatorio_totais, name_arq_with_extensao, name_columns, name_consulta):
        aux = 3

        file = xlsxwriter.Workbook(self.envs.SAVE_EXCEL_MK + name_arq_with_extensao)
        table = file.add_worksheet()
        table_chart = file.add_worksheet()

        merge_format = file.add_format(self.style.merge_format)
        cell_format_header = file.add_format(self.style.cell_format_header)
        cell_format = file.add_format(self.style.cell_format)
        cell_bg_color = file.add_format(self.style.cell_bg_color)

        table.merge_range('A1:E1', name_consulta , merge_format)

        table.write('A2',name_columns[0], cell_format_header)        
        table.write('B2',name_columns[1], cell_format_header)        
        table.write('C2',name_columns[2], cell_format_header)
        table.write('D2',name_columns[3], cell_format_header)
        table.write('E2',name_columns[4], cell_format_header)
        table.set_column('A:E', 25)

        for row in relatorio_criados:
            if row[0] != None:

                if type(row[0]) != str:
                    table.write('A'+str(aux), row[0].strftime('%m/%Y'), cell_format if aux % 2 else cell_bg_color)
                else:
                    table.write('A'+str(aux), row[0], cell_format if aux % 2 else cell_bg_color)

                table.write('B'+str(aux), row[1], cell_format if aux % 2 else cell_bg_color)
                table.write('C'+str(aux),row[2], cell_format if aux % 2 else cell_bg_color)
                
                aux += 1

        aux = 3
        for row in relatorio_cancelados:

            if row[0] != None:
                table.write('D'+str(aux), row[2], cell_format if aux % 2 else cell_bg_color)
                table.write_formula('E'+str(aux), ' = C'+str(aux) + '- D'+str(aux) , cell_format if aux % 2 else cell_bg_color)

                aux += 1


        table.merge_range('A{}:E{}'.format(str(aux), str(aux)), name_consulta, merge_format)

        aux += 1

        for row in relatorio_totais:

            if type(row[0]) != str:
                table.write('A'+str(aux), row[0].strftime('%m/%Y'), cell_format if aux % 2 else cell_bg_color)
            else:
                table.write('A'+str(aux), row[0], cell_format if aux % 2 else cell_bg_color)
            table.write('B'+str(aux), 'TOTAIS', cell_format if aux % 2 else cell_bg_color)
            
            table.write('C'+str(aux), row[1], cell_format if aux % 2 else cell_bg_color)
            table.write('D'+str(aux), row[2], cell_format if aux % 2 else cell_bg_color)
            table.write_formula('E'+str(aux), ' = C'+str(aux) + '- D'+str(aux) , cell_format if aux % 2 else cell_bg_color)

            aux += 1


        chart = file.add_chart({'type':'column'})
        chart.add_series({
            'categories': '=Sheet1!A{}:A{}'.format(aux - self.dates.range_meses, aux - 1),
            'name': name_columns[2],
            'values': '=Sheet1!C{}:C{}'.format(aux - self.dates.range_meses, aux - 1),
            'data_labels': self.default_data_labels,
            'pattern': self.default_pattern, 
            'border': self.default_border
        })
        chart.add_series({
            'name': name_columns[3],
            'values': '=Sheet1!D{}:D{}'.format(aux - self.dates.range_meses, aux - 1),
            'data_labels': self.default_data_labels,
            'pattern': self.default_pattern, 
            'border': self.default_border
        })
        chart.add_series({
            'name': name_columns[4],
            'values': '=Sheet1!E{}:E{}'.format(aux - self.dates.range_meses, aux - 1),
            'data_labels': self.default_data_labels,
            'pattern': self.default_pattern, 
            'border': self.default_border
        })
        chart.set_legend({ 'none': True })
        chart.set_style(2)
        chart.set_y_axis( { 'major_gridlines': { 'visible': False } } )
        chart.set_x_axis( { 'major_gridlines': { 'visible': False } } )
        table_chart.insert_chart('A1', chart)

        file.close()

        self.save_.excel_to_pdf(
            name_arq_with_extensao,
            name_consulta
        )
