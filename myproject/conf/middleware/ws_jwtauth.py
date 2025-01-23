# middleware/ws_jwtauth -- WS MIDDLEWARE

from typing import Union
from channels.middleware import BaseMiddleware
from django.contrib.auth.models import AnonymousUser, User

from apps.a12n import async_get_user_from_token


def _get_token_from_header(header: str) -> Union[str, None]:
    if header.lower().startswith("bearer"):
        return header.split(" ", 1)[1]


class JWTAuthMiddleware(BaseMiddleware):
    """
    JWTAuthMiddleware is used to assign user_id to scope
    """

    async def __call__(self, scope, receive, send):
        headers = dict(scope.get('headers'))
        auth_header = headers.get(b'authorization').decode()

        if auth_header:
            token: Union[str | None] = _get_token_from_header(auth_header)
            scope['user']: Union[AnonymousUser | User] = await async_get_user_from_token(token) if token else AnonymousUser()

        return await super().__call__(scope, receive, send)

