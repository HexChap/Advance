import json
import pathlib

from .project_types import Settings, Paths


__all__ = ["get_settings"]

ROOT_DIR = pathlib.Path(__file__).parent.parent.parent
path_to_settings = ROOT_DIR / "settings.json"


def get_settings() -> Settings:
    with open(path_to_settings, "r", encoding="utf-8") as json_file:
        settings_file = json.loads(json_file.read())

        # input/output pathes
        path_list = list(settings_file["paths"].values())

        if path_list[0] == "None" or path_list[1] == "None":
            paths = Paths(ROOT_DIR, ROOT_DIR)
        else:
            paths = Paths(*settings_file["paths"].values())
        # border values for image cutter
        border = tuple(json.loads(settings_file["border"]))

        settings = Settings(
            paths=paths,
            border=border
        )

    return settings
