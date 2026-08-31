from typing import Literal

BlockRolloutConfigKindEnum = Literal["config", "trigger"]

BLOCK_ROLLOUT_CONFIG_KIND_ENUM_VALUES: set[BlockRolloutConfigKindEnum] = {
    "config",
    "trigger",
}


def check_block_rollout_config_kind_enum(value: str) -> BlockRolloutConfigKindEnum:
    if value in BLOCK_ROLLOUT_CONFIG_KIND_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_CONFIG_KIND_ENUM_VALUES!r}")
