from .possibilities import SJC_OPTIONS, GREENVIEW_OPTIONS, SATELITE_OPTIONS
from dotenv import load_dotenv
from os import environ

load_dotenv()

EXPORT_URL = 'https://qualar.cetesb.sp.gov.br/qualar/exportaDadosAvanc.do?method=exportar'
AUTH_URL = 'https://qualar.cetesb.sp.gov.br/qualar/autenticador'

USERNAME = environ.get('QUALAR_USERNAME')
PASSWORD = environ.get('QUALAR_PASSWORD')
