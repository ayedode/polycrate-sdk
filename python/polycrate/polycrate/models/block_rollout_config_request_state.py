from typing import Literal

BlockRolloutConfigRequestState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

BLOCK_ROLLOUT_CONFIG_REQUEST_STATE_VALUES: set[BlockRolloutConfigRequestState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_block_rollout_config_request_state(value: str) -> BlockRolloutConfigRequestState:
    if value in BLOCK_ROLLOUT_CONFIG_REQUEST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_CONFIG_REQUEST_STATE_VALUES!r}")
