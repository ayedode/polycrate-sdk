from typing import Literal

BlockRolloutScope = Literal["system", "user"]

BLOCK_ROLLOUT_SCOPE_VALUES: set[BlockRolloutScope] = {
    "system",
    "user",
}


def check_block_rollout_scope(value: str) -> BlockRolloutScope:
    if value in BLOCK_ROLLOUT_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_SCOPE_VALUES!r}")
