from sqlalchemy import Column, ForeignKey, BigInteger, String

from backend.constants import (
    APPLICATION_FOREIGN_KEY, COMPANY_INN_FOREIGN_KEY, STATUS_MAX_LEN,
)
from backend.app.core.db import Base


class ApplicationCompany(Base):
    """Модель для связи id заявки и ИНН компании (плательщика или получателя)."""
    id_application = Column(
        BigInteger,
        ForeignKey(APPLICATION_FOREIGN_KEY),
    )
    company_inn = Column(
        BigInteger,
        ForeignKey(COMPANY_INN_FOREIGN_KEY),
    )
    payer_or_recipient_status = Column(String(STATUS_MAX_LEN))
