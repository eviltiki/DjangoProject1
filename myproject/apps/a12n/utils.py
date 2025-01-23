# utils -- APPLICATION LAYER

import logging
from channels.db import database_sync_to_async
from django.contrib.auth.models import AnonymousUser, User
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.tokens import AccessToken

from apps.accounts.services.user_creator import UserCreator


@database_sync_to_async
def async_get_user_from_token(token: str):
    try:
        validated_token = AccessToken(token)
        if validated_token:
            user_id: int = validated_token['user_id']
            return UserCreator(id=user_id).get()
        else:
            return AnonymousUser()
    except (InvalidToken, TokenError) as err:
        logging.exception(f"Failed to extract user_id from token apps:utils.py {err}")
        return AnonymousUser()