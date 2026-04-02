import pytest
from src.utils.config import load_config

@pytest.mark.parametrize(
    "config_path, expected",
    [
        ("tests/.config/test_cfg1.yml", {"key1": "value1", "key2": "value2"}),
        ("tests/.config/test_cfg2.yml", {"key3": "value3", "key4": "value4"}),
    ]
)
def test_load_config(config_path, expected):
    config = load_config(config_path)
    assert config == expected
