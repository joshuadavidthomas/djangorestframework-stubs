from _typeshed import Incomplete
from collections.abc import Iterable, Mapping
from typing import Any, TypeAlias

import coreapi  # type: ignore[import-untyped]
import requests
import urllib3
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AnonymousUser
from django.http import HttpRequest
from django.test import testcases
from django.test.client import Client as DjangoClient
from django.test.client import ClientHandler
from django.test.client import RequestFactory as DjangoRequestFactory
from rest_framework.authtoken.models import Token
from rest_framework.request import Request
from rest_framework.response import _MonkeyPatchedResponse

_GetDataType: TypeAlias = (
    Mapping[str, str | bytes | float | Iterable[str | bytes | float]]
    | Iterable[tuple[str, str | bytes | float | Iterable[str | bytes | float]]]
    | None
)

def force_authenticate(
    request: HttpRequest, user: AnonymousUser | AbstractBaseUser | None = ..., token: Token | None = ...
) -> None: ...

class HeaderDict(urllib3._collections.HTTPHeaderDict):
    def get_all(self, key: Any, default: Any) -> Incomplete: ...

class MockOriginalResponse:
    msg: Any
    closed: bool
    def __init__(self, headers: Any) -> None: ...
    def isclosed(self) -> bool: ...
    def close(self) -> None: ...

class DjangoTestAdapter(requests.adapters.HTTPAdapter):
    app: Any
    factory: Any
    def __init__(self) -> None: ...
    def get_environ(self, request: Request) -> Incomplete: ...
    def send(self, request: Request, *args: Any, **kwargs: Any) -> requests.Response: ...  # type: ignore[override]
    def close(self) -> None: ...

class RequestsClient(requests.Session): ...

class CoreAPIClient(coreapi.Client):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @property
    def session(self) -> Incomplete: ...

class APIRequestFactory(DjangoRequestFactory):
    renderer_classes_list: Any
    default_format: Any
    enforce_csrf_checks: Any
    renderer_classes: Any
    def __init__(self, enforce_csrf_checks: bool = ..., **defaults: Any) -> None: ...
    def request(self, **kwargs: Any) -> Request: ...  # type: ignore[override]
    def get(self, path: str, data: _GetDataType = ..., **extra: Any) -> Request: ...  # type: ignore[override]
    def post(  # type: ignore[override]
        self, path: str, data: Any | None = ..., format: str | None = ..., content_type: str | None = ..., **extra: Any
    ) -> Request: ...
    def put(  # type: ignore[override]
        self, path: str, data: Any | None = ..., format: str | None = ..., content_type: str | None = ..., **extra: Any
    ) -> Request: ...
    def patch(  # type: ignore[override]
        self, path: str, data: Any | None = ..., format: str | None = ..., content_type: str | None = ..., **extra: Any
    ) -> Request: ...
    def delete(  # type: ignore[override]
        self, path: str, data: Any | None = ..., format: str | None = ..., content_type: str | None = ..., **extra: Any
    ) -> Request: ...
    def options(  # type: ignore[override]
        self,
        path: str,
        data: dict[str, str] | str | None = ...,
        format: str | None = ...,
        content_type: Any | None = ...,
        **extra: Any,
    ) -> Request: ...
    def generic(  # type: ignore[override]
        self, method: str, path: str, data: str = ..., content_type: str = ..., secure: bool = ..., **extra: Any
    ) -> Request: ...

class ForceAuthClientHandler(ClientHandler):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def get_response(self, request: Request) -> _MonkeyPatchedResponse: ...  # type: ignore[override]

class APIClient(APIRequestFactory, DjangoClient):
    def credentials(self, **kwargs: Any) -> None: ...
    def force_authenticate(
        self, user: AnonymousUser | AbstractBaseUser | None = ..., token: Token | None = ...
    ) -> None: ...
    def request(self, **kwargs: Any) -> _MonkeyPatchedResponse: ...  # type: ignore[override]
    def get(self, path: str, data: _GetDataType = ..., follow: bool = ..., **extra: Any) -> _MonkeyPatchedResponse: ...  # type: ignore[override]
    def post(  # type: ignore[override]
        self,
        path: str,
        data: Any | None = ...,
        format: str | None = ...,
        content_type: str | None = ...,
        follow: bool = ...,
        **extra: Any,
    ) -> _MonkeyPatchedResponse: ...
    def put(  # type: ignore[override]
        self,
        path: str,
        data: Any | None = ...,
        format: str | None = ...,
        content_type: str | None = ...,
        follow: bool = ...,
        **extra: Any,
    ) -> _MonkeyPatchedResponse: ...
    def patch(  # type: ignore[override]
        self,
        path: str,
        data: Any | None = ...,
        format: str | None = ...,
        content_type: str | None = ...,
        follow: bool = ...,
        **extra: Any,
    ) -> _MonkeyPatchedResponse: ...
    def delete(  # type: ignore[override]
        self,
        path: str,
        data: Any | None = ...,
        format: str | None = ...,
        content_type: str | None = ...,
        follow: bool = ...,
        **extra: Any,
    ) -> _MonkeyPatchedResponse: ...
    def options(  # type: ignore[override]
        self,
        path: str,
        data: dict[str, str] | str = ...,
        format: str | None = ...,
        content_type: Any | None = ...,
        follow: bool = ...,
        **extra: Any,
    ) -> _MonkeyPatchedResponse: ...
    def logout(self) -> None: ...

class APITransactionTestCase(testcases.TransactionTestCase):
    client_class: type[APIClient]
    client: APIClient

class APITestCase(testcases.TestCase):
    client_class: type[APIClient]
    client: APIClient

class APISimpleTestCase(testcases.SimpleTestCase):
    client_class: type[APIClient]
    client: APIClient

class APILiveServerTestCase(testcases.LiveServerTestCase):
    client_class: type[APIClient]
    client: APIClient

def cleanup_url_patterns(cls: type[URLPatternsTestCase]) -> None: ...

class URLPatternsTestCase(testcases.SimpleTestCase): ...
