from typing import Literal

ConditionInstanceDetailEffectiveCriticalityType1 = Literal["high", "low", "medium"]

CONDITION_INSTANCE_DETAIL_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[ConditionInstanceDetailEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_condition_instance_detail_effective_criticality_type_1(
    value: str,
) -> ConditionInstanceDetailEffectiveCriticalityType1:
    if value in CONDITION_INSTANCE_DETAIL_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONDITION_INSTANCE_DETAIL_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
