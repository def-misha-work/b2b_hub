from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.crud.base import CRUDBase
from backend.app.models.application import Application
from backend.constants import CREATE_DATE_APPLICATION


class CRUDApplication(CRUDBase):
    """CRUD-операции с заявками."""
    ...

    async def create_application(
            self,
            application,
            session: AsyncSession,
            # user: Optional[User] = None,
    ):
        """Создать новую заявку."""
        application_data = application.dict()
        new_application = Application(
            target_date=application_data['target_date'],
            cost=application_data['cost'],
            create_date=CREATE_DATE_APPLICATION,
        )
        # if user is not None:
        #     obj_in_data['user_id'] = user.id
        session.add(new_application)
        await session.commit()
        await session.refresh(new_application)
        return new_application

    # async def get_wish_id_by_user...


application_crud = CRUDApplication(Application)
