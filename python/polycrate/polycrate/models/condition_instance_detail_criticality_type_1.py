from typing import Literal

ConditionInstanceDetailCriticalityType1 = Literal["", "high", "low", "medium"]

CONDITION_INSTANCE_DETAIL_CRITICALITY_TYPE_1_VALUES: set[ConditionInstanceDetailCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_condition_instance_detail_criticality_type_1(value: str) -> ConditionInstanceDetailCriticalityType1:
    if value in CONDITION_INSTANCE_DETAIL_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONDITION_INSTANCE_DETAIL_CRITICALITY_TYPE_1_VALUES!r}"
    )
