from typing import Literal

PatchedBlockRolloutRequestCriticalityType3Type1 = Literal["", "high", "low", "medium"]

PATCHED_BLOCK_ROLLOUT_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[PatchedBlockRolloutRequestCriticalityType3Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_block_rollout_request_criticality_type_3_type_1(
    value: str,
) -> PatchedBlockRolloutRequestCriticalityType3Type1:
    if value in PATCHED_BLOCK_ROLLOUT_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_BLOCK_ROLLOUT_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
