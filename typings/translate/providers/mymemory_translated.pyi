from typing import Any

from .base import BaseProvider

class MyMemoryProvider(BaseProvider):
    """
    @MyMemoryProvider: This is a integration with Translated MyMemory API.
    Follow Informations:
        Website: https://mymemory.translated.net/
        Documentation: https://mymemory.translated.net/doc/spec.php

    Usage Tips: Use a valid email instead of the default.
        With a valid email you get 10 times more words/day to translate.
    For further infomations checkout:
    http://mymemory.translated.net/doc/usagelimits.php
                                                    Tips from: @Bachstelze
    """

    name = ...
    base_url = ...
    def __init__(self, **kwargs: Any) -> None: ...
    def get_translation(self, text: str) -> Any: ...
