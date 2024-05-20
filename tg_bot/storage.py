class UserStorage():

    def __init__(self, tg_id, tg_username, tg_name, tg_surname):
        self.tg_id = tg_id
        self.tg_username = tg_username
        self.tg_name = tg_name
        self.tg_surname = tg_surname

    def to_dict(self):
        return {
            'tg_user_id': self.tg_id,
            'tg_username': self.tg_username,
            'name': self.tg_name,
            'lastname': self.tg_surname
        }


class ApplicationStorage():

    def __init__(
        self,
        tg_id=None,
        inn_payer=None,
        name_payer=None,
        inn_recipient=None,
        name_recipient=None,
        application_cost=None,
        target_date=None,
        application_id=None
    ):
        self.tg_id = tg_id
        self.inn_payer = inn_payer
        self.name_payer = name_payer
        self.inn_recipient = inn_recipient
        self.name_recipient = name_recipient
        self.application_cost = application_cost
        self.target_date = target_date
        self.application_id = application_id

    def update_tg_id(self, new_tg_id):
        self.tg_id = new_tg_id

    def update_inn_payer(self, new_inn_payer):
        self.inn_payer = new_inn_payer

    def update_name_payer(self, new_name_payer):
        self.name_payer = new_name_payer

    def update_inn_recipient(self, new_inn_recipient):
        self.inn_recipient = new_inn_recipient

    def update_name_recipient(self, new_name_recipient):
        self.name_recipient = new_name_recipient

    def update_application_cost(self, new_application_cost):
        self.application_cost = new_application_cost

    def update_target_date(self, new_target_date):
        self.target_date = new_target_date

    def update_application_id(self, new_application_id):
        self.application_id = new_application_id

    def to_dict(self):
        return {
            'target_date': self.target_date,
            'cost': self.application_cost,
            'inn_payer': self.inn_payer,
            'name_payer': self.name_payer,
            'inn_recipient': self.inn_recipient,
            'name_recipient': self.name_recipient,
            'tg_user_id': self.tg_id,
        }


# class CompanyStorage():
#     def __init__(self, company_inn, company_name=None):
#         self.company_inn = company_inn
#         self.company_name = company_name

#     def update_company_name(self, new_company_name):
#         self.company_name = new_company_name

#     def to_dict(self):
#         return {
#             'company_inn': self.company_inn,
#             'company_name': self.company_name,
#         }
