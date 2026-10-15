from typing import Literal

BlockRolloutConfigLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

BLOCK_ROLLOUT_CONFIG_LAST_STATE_VALUES: set[BlockRolloutConfigLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_block_rollout_config_last_state(value: str) -> BlockRolloutConfigLastState:
    if value in BLOCK_ROLLOUT_CONFIG_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_CONFIG_LAST_STATE_VALUES!r}")
