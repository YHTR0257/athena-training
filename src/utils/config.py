import json
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent.parent

def load_config(config_path: Path|str) -> dict:
    if config_path is None:
        config_path = ROOT_DIR / ".config" / "general.json"
    elif isinstance(config_path, str):
        config_path = Path(config_path)
        config_path = ROOT_DIR / config_path if not config_path.is_absolute() else config_path
    elif not config_path.is_absolute():
        config_path = ROOT_DIR / config_path

    if config_path.suffix not in [".json", ".yml", ".yaml"]:
        return {"error": f"Unsupported config file format: {config_path.suffix}"}
    if config_path.suffix in [".yml", ".yaml"]:
        import yaml
        with open(config_path, "r") as f:
            return yaml.safe_load(f)
    elif config_path.suffix == ".json":
        with open(config_path, "r") as f:
            return json.load(f)
    else:
        return {"error": "File not found or unsupported format"}
