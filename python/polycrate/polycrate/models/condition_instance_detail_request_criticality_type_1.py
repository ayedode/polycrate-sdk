from typing import Literal

ConditionInstanceDetailRequestCriticalityType1 = Literal["", "high", "low", "medium"]

CONDITION_INSTANCE_DETAIL_REQUEST_CRITICALITY_TYPE_1_VALUES: set[ConditionInstanceDetailRequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_condition_instance_detail_request_criticality_type_1(
    value: str,
) -> ConditionInstanceDetailRequestCriticalityType1:
    if value in CONDITION_INSTANCE_DETAIL_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONDITION_INSTANCE_DETAIL_REQUEST_CRITICALITY_TYPE_1_VALUES!r}"
    )
