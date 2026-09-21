from pathlib import Path
from typing import Optional
import os
import yaml

def _project_root() -> Path:
    """
    Returns the root directory of the project.
    """
    return Path(__file__).resolve().parents[1]

def load_config(config_path: Optional[str] = None) -> dict:
    """
    Resolve config file path and load its contents
    """
    env_path = os.getenv("CONFIG_PATH")
    if config_path is None:
        config_path = env_path or str(_project_root() / "config" / "configuration.yaml")

    path = Path(config_path)
    if not path.is_absolute():
        path = _project_root() / path

    if not path.exists():
        raise FileNotFoundError(f"Configuration file not found at {path}")

    with open(path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file) or {}


