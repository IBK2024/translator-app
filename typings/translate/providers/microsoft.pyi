from typing import Any

from .base import BaseProvider

class MicrosoftProvider(BaseProvider):
    """
    @MicrosoftProvider: This is a integration with Microsoft Translator API.
    Website: http://docs.microsofttranslator.com
    Documentation: http://docs.microsofttranslator.com/text-translate.html
    """

    name = ...
    base_url = ...
    def get_translation(self, text: Any) -> Any: ...
