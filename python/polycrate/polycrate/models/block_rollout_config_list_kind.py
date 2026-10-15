from typing import Literal

BlockRolloutConfigListKind = Literal["config", "trigger"]

BLOCK_ROLLOUT_CONFIG_LIST_KIND_VALUES: set[BlockRolloutConfigListKind] = {
    "config",
    "trigger",
}


def check_block_rollout_config_list_kind(value: str) -> BlockRolloutConfigListKind:
    if value in BLOCK_ROLLOUT_CONFIG_LIST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_CONFIG_LIST_KIND_VALUES!r}")
