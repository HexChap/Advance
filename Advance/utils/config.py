import pathlib

from .project_types import Settings, Paths
from .settings_parser import get_settings

# Basic Settings
ROOT_DIR = pathlib.Path(__file__).parent.parent.parent
settings: Settings = get_settings()
paths: Paths = settings.paths

# Border for image cutter
border: tuple = settings.border
