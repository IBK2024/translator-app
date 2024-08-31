from typing import Any

from .providers import MyMemoryProvider

DEFAULT_PROVIDER = MyMemoryProvider
TRANSLATION_API_MAX_LENGHT = ...
PROVIDERS_CLASS = ...

class Translator:
    def __init__(
        self,
        to_lang: Any,
        from_lang: Any = ...,
        provider: Any = ...,
        secret_access_key: Any = ...,
        region: Any = ...,
        **kwargs: Any
    ) -> None: ...
    def translate(self, text: str) -> str: ...
