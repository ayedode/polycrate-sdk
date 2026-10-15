from typing import Literal

BlockRolloutConfigRequestLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

BLOCK_ROLLOUT_CONFIG_REQUEST_LAST_STATE_VALUES: set[BlockRolloutConfigRequestLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_block_rollout_config_request_last_state(value: str) -> BlockRolloutConfigRequestLastState:
    if value in BLOCK_ROLLOUT_CONFIG_REQUEST_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_CONFIG_REQUEST_LAST_STATE_VALUES!r}")
