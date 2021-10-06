import os 
from dotenv import load_dotenv

class Env_Vars:

    def __init__(self):
        load_dotenv()
        self.DB_MK = self.DB_MK()
        self.SAVE_QUERYS_MK = str(os.getenv('DEFAULT_SAVE_QUERYS_MK'))
        self.SAVE_EXCEL_MK = str(os.getenv('DEFAULT_SAVE_EXCEL_MK'))
        self.SAVE_PDF_MK = str(os.getenv('DEFAULT_SAVE_PDF_MK'))
        self.SAVE_CSV_MK = str(os.getenv('DEFAULT_SAVE_CSV_MK'))
        
        self.DEFAULT_INIT_DATE_RANGE = self.default_init_date_range()


    def DB_MK(self):
         return { # MK
                "postgres":{
                    "database": os.getenv('DATABASE_MK'),
                    "password": os.getenv('PASSWORD_MK'),
                    "host": os.getenv('HOST_MK'),
                    "user": os.getenv('USER_MK')
                }
            }

    def default_init_date_range(self):
        day = os.getenv('DEFAULT_DATE_INIT_MK_DAY') 
        month = os.getenv('DEFAULT_DATE_INIT_MK_MONTH')
        year = os.getenv('DEFAULT_DATE_INIT_MK_YEAR') 

        return (day, month, year)
