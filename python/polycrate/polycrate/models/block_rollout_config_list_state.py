from typing import Literal

BlockRolloutConfigListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

BLOCK_ROLLOUT_CONFIG_LIST_STATE_VALUES: set[BlockRolloutConfigListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_block_rollout_config_list_state(value: str) -> BlockRolloutConfigListState:
    if value in BLOCK_ROLLOUT_CONFIG_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_CONFIG_LIST_STATE_VALUES!r}")
