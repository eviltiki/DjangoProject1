# services/user_creator -- DTO to transfer data between APPLICATION LAYER and BUSINESS LAYER
from dataclasses import dataclass
from typing import Union

from django.contrib.auth.models import User


@dataclass
class UserCreator:
    id: int

    def get(self) -> Union[User | None]:
        if self.id:
            return User.objects.filter(is_active=True).filter(id=self.id).first()
