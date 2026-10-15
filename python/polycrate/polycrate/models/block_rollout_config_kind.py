from typing import Literal

BlockRolloutConfigKind = Literal["config", "trigger"]

BLOCK_ROLLOUT_CONFIG_KIND_VALUES: set[BlockRolloutConfigKind] = {
    "config",
    "trigger",
}


def check_block_rollout_config_kind(value: str) -> BlockRolloutConfigKind:
    if value in BLOCK_ROLLOUT_CONFIG_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_CONFIG_KIND_VALUES!r}")
