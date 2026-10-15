from typing import Literal

PatchedConditionInstanceDetailRequestCriticalityType2Type1 = Literal["", "high", "low", "medium"]

PATCHED_CONDITION_INSTANCE_DETAIL_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[
    PatchedConditionInstanceDetailRequestCriticalityType2Type1
] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_condition_instance_detail_request_criticality_type_2_type_1(
    value: str,
) -> PatchedConditionInstanceDetailRequestCriticalityType2Type1:
    if value in PATCHED_CONDITION_INSTANCE_DETAIL_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_CONDITION_INSTANCE_DETAIL_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
