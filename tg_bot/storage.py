﻿class UserStorage():

    def __init__(self, tg_id, tg_username, tg_name, tg_surname):
        self.tg_id = tg_id
        self.tg_username = tg_username
        self.tg_name = tg_name
        self.tg_surname = tg_surname

    def to_dict(self):
        return {
            'tg_id': self.tg_id,
            'tg_username': self.tg_username,
            'tg_name': self.tg_name,
            'tg_surname': self.tg_surname
        }


class ApplicationStorage():

    def __init__(
        self,
        tg_id=None,
        inn_payer=None,
        inn_recipient=None,
        application_cost=None,
        target_date=None
    ):
        self.tg_id = tg_id
        self.inn_payer = inn_payer
        self.inn_recipient = inn_recipient
        self.application_cost = application_cost
        self.target_date = target_date

    def update_tg_id(self, new_tg_id):
        self.tg_id = new_tg_id

    def update_inn_payer(self, new_inn_payer):
        self.inn_payer = new_inn_payer

    def update_inn_recipient(self, new_inn_recipient):
        self.inn_recipient = new_inn_recipient

    def update_application_cost(self, new_application_cost):
        self.application_cost = new_application_cost

    def update_target_date(self, new_target_date):
        self.target_date = new_target_date

    def to_dict(self):
        return {
            'tg_id': self.tg_id,
            'inn_payer': self.inn_payer,
            'inn_recipient': self.inn_recipient,
            'application_cost': self.application_cost,
            'target_date': self.target_date
        }
