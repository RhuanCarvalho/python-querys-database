

class Style:

    def __init__(self):
        
        self.merge_format = {
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': '#70ad47',
        'bold': 1
            }

        self.cell_format_header = {
        'bg_color': '#70ad47',
        'border': 1,
        'align': 'center',
        'valign': 'vcenter'
            }

        self.cell_format = {
        'border': 1,
        'align': 'center',
        'valign': 'vcenter'
            }

        self.cell_bg_color = {
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'bg_color': '#e2efda'
            }

        self.cell_format_Currency = {
            'border': 1,
            'align': 'center',
            'valign': 'vcenter',
            'num_format': 'R$ #,###,###.##'
        }

        self.cell_bg_color_Currency = {
            'border': 1,
            'align': 'center',
            'valign': 'vcenter',
            'bg_color': '#e2efda',
            'num_format': 'R$ #,###,###.##'
        }