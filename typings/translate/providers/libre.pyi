"""
This type stub file was generated by pyright.
"""

from typing import Any

from .base import BaseProvider

class LibreProvider(BaseProvider):
    """
    @LibreProvider: This is a integration with LibreTranslate translation API.
    Website: https://libretranslate.com/
    Documentation: https://libretranslate.com/docs/
    Github: https://github.com/LibreTranslate/LibreTranslate
    """

    name = ...
    def __init__(
        self,
        to_lang: Any,
        from_lang: Any = ...,
        secret_access_key: Any = ...,
        region: Any = ...,
        base_url: Any = ...,
        **kwargs: Any
    ) -> None: ...
    def get_translation(self, text: Any) -> Any: ...
