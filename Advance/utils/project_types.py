from typing import NamedTuple, Dict


class ImgsData(NamedTuple):
    img_paths: list[str]
    file_exts: list[str]


class Paths(NamedTuple):
    input_path: str
    output_path: str


class Settings(NamedTuple):
    paths: Paths
    border: list

# GUI types
