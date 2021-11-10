import mimetypes
import os

from .project_types import ImgsData


mimetypes.init()

__all__ = ["get_images"]


def get_images(input_dir: str) -> ImgsData:
    """Return a list of paths to filtered images from the selected folder."""
    imgs_data = ImgsData(
        img_paths=list(__filter_paths(input_dir)),
        file_exts=list(__get_exts_of_filtred_paths(input_dir))
    )
    return imgs_data


def __get_all_image_exts():
    for ext in mimetypes.types_map:
        if mimetypes.types_map[ext].split("/")[0] == "image":
            yield ext


def __get_exts_of_filtred_paths(input_dir):
    for path in list(__filter_paths(input_dir)):
        yield path.split(".")[-1]


def __get_files(input_dir):
    for root, _, files in os.walk(input_dir):
        for name in files:
            yield os.path.join(root, name)


def __filter_paths(input_dir):
    for filepath in list(__get_files(input_dir)):
        img_ext = "." + filepath.split(".")[-1]
        img_dir = "\\".join(filepath.split("\\")[:-1])

        if img_ext not in list(__get_all_image_exts()):
            continue

        if img_dir == input_dir:
            yield filepath.replace("\\", "/")
