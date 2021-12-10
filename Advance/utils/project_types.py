from typing import NamedTuple


class ImgsData(NamedTuple):
    img_paths: list[str]
    file_exts: list[str]

    def is_empty(self) -> bool:
        return False if self.img_paths and self.file_exts else True


class Paths(NamedTuple):
    input_path: str
    output_path: str


class Settings(NamedTuple):
    paths: Paths
    border: list
