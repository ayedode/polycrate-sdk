from typing import Literal

PatchedBlockRolloutRequestScope = Literal["system", "user"]

PATCHED_BLOCK_ROLLOUT_REQUEST_SCOPE_VALUES: set[PatchedBlockRolloutRequestScope] = {
    "system",
    "user",
}


def check_patched_block_rollout_request_scope(value: str) -> PatchedBlockRolloutRequestScope:
    if value in PATCHED_BLOCK_ROLLOUT_REQUEST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_BLOCK_ROLLOUT_REQUEST_SCOPE_VALUES!r}")
