from typing import Literal

BlockRolloutRequestKind = Literal["generic"]

BLOCK_ROLLOUT_REQUEST_KIND_VALUES: set[BlockRolloutRequestKind] = {
    "generic",
}


def check_block_rollout_request_kind(value: str) -> BlockRolloutRequestKind:
    if value in BLOCK_ROLLOUT_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_REQUEST_KIND_VALUES!r}")
