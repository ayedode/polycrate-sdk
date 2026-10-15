from typing import Literal

BlockRolloutConfigScope = Literal["system", "user"]

BLOCK_ROLLOUT_CONFIG_SCOPE_VALUES: set[BlockRolloutConfigScope] = {
    "system",
    "user",
}


def check_block_rollout_config_scope(value: str) -> BlockRolloutConfigScope:
    if value in BLOCK_ROLLOUT_CONFIG_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_CONFIG_SCOPE_VALUES!r}")
