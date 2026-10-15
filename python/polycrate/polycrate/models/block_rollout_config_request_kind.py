from typing import Literal

BlockRolloutConfigRequestKind = Literal["config", "trigger"]

BLOCK_ROLLOUT_CONFIG_REQUEST_KIND_VALUES: set[BlockRolloutConfigRequestKind] = {
    "config",
    "trigger",
}


def check_block_rollout_config_request_kind(value: str) -> BlockRolloutConfigRequestKind:
    if value in BLOCK_ROLLOUT_CONFIG_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_CONFIG_REQUEST_KIND_VALUES!r}")
