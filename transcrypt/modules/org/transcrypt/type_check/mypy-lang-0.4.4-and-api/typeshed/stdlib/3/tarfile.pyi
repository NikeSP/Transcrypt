# TODO these are incomplete

from typing import Any, List, overload, Callable

class TarError(Exception): ...

class TarInfo:
    name = ...  # type: str
    size = 0
    uid = 0
    gid = 0

class TarFile:
    def getmember(self, name: str) -> TarInfo: ...
    def getmembers(self) -> List[TarInfo]: ...
    def getnames(self) -> List[str]: ...
    def extractall(self, path: str = ...,
                   members: List[TarInfo] = ...) -> None: ...

    @overload
    def extract(self, member: str, path: str = ...,
                set_attrs: bool = ...) -> None: ...
    @overload
    def extract(self, member: TarInfo, path: str = ...,
                set_attrs: bool = ...) -> None: ...

    def add(self, name: str, arcname: str = ..., recursive: bool = ...,
            exclude: Callable[[str], bool] = ..., *,
            filter: 'Callable[[TarFile], TarFile]' = ...) -> None: ...
    def close(self) -> None: ...

def open(name: str = ..., mode: str = ..., fileobj: Any = ..., bufsize: int = ...,
         **kwargs) -> TarFile: ...