from typing import Literal

BlockRolloutRequestCriticalityType1 = Literal["", "high", "low", "medium"]

BLOCK_ROLLOUT_REQUEST_CRITICALITY_TYPE_1_VALUES: set[BlockRolloutRequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_block_rollout_request_criticality_type_1(value: str) -> BlockRolloutRequestCriticalityType1:
    if value in BLOCK_ROLLOUT_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_ROLLOUT_REQUEST_CRITICALITY_TYPE_1_VALUES!r}")
