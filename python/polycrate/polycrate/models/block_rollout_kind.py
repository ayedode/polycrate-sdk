from typing import Literal

BlockRolloutKind = Literal["generic"]

BLOCK_ROLLOUT_KIND_VALUES: set[BlockRolloutKind] = {
    "generic",
}


def check_block_rollout_kind(value: str) -> BlockRolloutKind:
    if value in BLOCK_ROLLOUT_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_KIND_VALUES!r}")
