from datetime import datetime

# core/config
APP_TITLE = 'Приложение B2B Hub'
ENV_FILE_NAME = '.env'

# models
CREATE_DATE_DEFAULT = datetime.utcnow

COMPANY_NAME_MAX_LEN = 100
STATUS_MAX_LEN = 15

APPLICATION_FOREIGN_KEY = 'application.id'
COMPANY_INN_FOREIGN_KEY = 'company.company_inn'
COMPANY_ID_FOREIGN_KEY = 'company.id'

# api/routers
APPLICATION_ROUTER_PREFIX = '/application'
APPLICATION_ROUTER_TAG = 'Applications'

# api/endpoints/application
CLEAR_ROUTE = '/'

# schemas/wish
CREATE_DATE = datetime.now().isoformat(timespec='seconds')
EMPTY_FIELD_ERROR = 'Поле {} не может быть пустым!'

# crud application
CREATE_DATE_APPLICATION = datetime.utcnow()
