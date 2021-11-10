import json
import os.path
import pathlib

from .project_types import Settings, Paths


__all__ = ["get_settings"]


path_to_settings = os.path.join(
    pathlib.Path(__file__).parent.parent.parent,
    "settings.json"
)


def get_settings() -> Settings:
    with open(path_to_settings, "r", encoding="utf-8") as json_file:
        settings_file = json.loads(json_file.read())

        # input/output pathes
        paths = Paths(*settings_file["paths"].values())
        # border values for image cutter
        border = tuple(json.loads(settings_file["border"]))

        settings = Settings(
            paths=paths,
            border=border
        )

    return settings
