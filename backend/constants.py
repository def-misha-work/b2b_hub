from datetime import datetime

# core/config
APP_TITLE = 'Приложение B2B Hub'
ENV_FILE_NAME = '.env'

# models
CREATE_DATE_DEFAULT = datetime.utcnow

COMPANY_NAME_MAX_LEN = 100
COMPANY_ID_FOREIGN_KEY = 'company.id'
COMPANY_INN_FOREIGN_KEY = 'company.company_inn'
