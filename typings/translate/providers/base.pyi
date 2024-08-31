from abc import ABCMeta, abstractmethod
from typing import Any

class BaseProvider:
    __metaclass__ = ABCMeta
    name = ...
    base_url = ...
    def __init__(self, to_lang: Any, from_lang: Any = ..., secret_access_key: Any = ..., region: Any = ..., **kwargs) -> None: ...  # type: ignore
    @abstractmethod
    def get_translation(self, params): ...  # type: ignore
