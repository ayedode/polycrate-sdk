from typing import Literal

BlockRolloutConfigState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

BLOCK_ROLLOUT_CONFIG_STATE_VALUES: set[BlockRolloutConfigState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_block_rollout_config_state(value: str) -> BlockRolloutConfigState:
    if value in BLOCK_ROLLOUT_CONFIG_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_CONFIG_STATE_VALUES!r}")
