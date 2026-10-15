from typing import Literal

BlockRolloutRequestScope = Literal["system", "user"]

BLOCK_ROLLOUT_REQUEST_SCOPE_VALUES: set[BlockRolloutRequestScope] = {
    "system",
    "user",
}


def check_block_rollout_request_scope(value: str) -> BlockRolloutRequestScope:
    if value in BLOCK_ROLLOUT_REQUEST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_REQUEST_SCOPE_VALUES!r}")
