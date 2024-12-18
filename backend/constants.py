from datetime import datetime

# core/config
APP_TITLE = 'Приложение B2B Hub'
ENV_FILE_NAME = '.env'

# models
CREATE_DATE_DEFAULT = datetime.now().replace(microsecond=0)

COMPANY_NAME_MAX_LEN = 100
STATUS_MAX_LEN = 15
TG_USERNAME_MAX_LEN = 100

APPLICATION_FOREIGN_KEY = 'application.id'
COMPANY_INN_FOREIGN_KEY = 'company.company_inn'
TG_USER_FOREIGN_KEY = 'tguser.tg_user_id'

# api/routers
APPLICATION_ROUTER_PREFIX = '/application'
APPLICATION_ROUTER_TAG = 'Applications'

COMPANY_ROUTER_PREFIX = '/company'
COMPANY_ROUTER_TAG = 'Companies'

TGUSER_ROUTER_PREFIX = '/tguser'
TGUSER_ROUTER_TAG = 'Telegram users'

USER_ROUTER_PREFIX = '/user'
USER_ROUTER_TAG = 'Users'

# api/endpoints/application
CLEAR_ROUTE = '/'

# schemas/wish
EMPTY_FIELD_ERROR = 'Поле {} не может быть пустым!'
