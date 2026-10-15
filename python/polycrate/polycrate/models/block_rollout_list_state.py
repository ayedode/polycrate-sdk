from typing import Literal

BlockRolloutListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

BLOCK_ROLLOUT_LIST_STATE_VALUES: set[BlockRolloutListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_block_rollout_list_state(value: str) -> BlockRolloutListState:
    if value in BLOCK_ROLLOUT_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_LIST_STATE_VALUES!r}")
