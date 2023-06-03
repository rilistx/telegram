from typing import Dict

from aiogram.filters import BaseFilter
from aiogram.types import Message


# class IsTrueContact(BaseFilter):
#     async def __call__(self, message: Message) -> bool:
#         try:
#             return message.contact.user_id == message.from_user.id
#         except:
#             return False

class IsTrueContact(BaseFilter):
    async def __call__(self, message: Message):
        if message.contact.user_id == message.from_user.id:
            return {'phone': message.contact.phone_number}
        else:
            return False
