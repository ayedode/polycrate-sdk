from typing import Literal

BlockRolloutConfigRequestScope = Literal["system", "user"]

BLOCK_ROLLOUT_CONFIG_REQUEST_SCOPE_VALUES: set[BlockRolloutConfigRequestScope] = {
    "system",
    "user",
}


def check_block_rollout_config_request_scope(value: str) -> BlockRolloutConfigRequestScope:
    if value in BLOCK_ROLLOUT_CONFIG_REQUEST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_CONFIG_REQUEST_SCOPE_VALUES!r}")
