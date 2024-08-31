from typing import Any

from .base import BaseProvider

class DeeplProvider(BaseProvider):
    """
    @DeeplProvider: This is a integration with DeepL Translator API.
    Website: https://www.deepl.com
    Documentation: https://www.deepl.com/docs-api
    """

    name = ...
    base_free_url = ...
    base_pro_url = ...
    def __init__(self, **kwargs: Any) -> None: ...
    def get_translation(self, text: Any) -> Any: ...
