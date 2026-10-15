from typing import Literal

PatchedBlockRolloutRequestKind = Literal["generic"]

PATCHED_BLOCK_ROLLOUT_REQUEST_KIND_VALUES: set[PatchedBlockRolloutRequestKind] = {
    "generic",
}


def check_patched_block_rollout_request_kind(value: str) -> PatchedBlockRolloutRequestKind:
    if value in PATCHED_BLOCK_ROLLOUT_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_BLOCK_ROLLOUT_REQUEST_KIND_VALUES!r}")
