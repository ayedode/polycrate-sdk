from typing import Literal

ConditionInstanceListEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

CONDITION_INSTANCE_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[
    ConditionInstanceListEffectiveCriticalityType2Type1
] = {
    "high",
    "low",
    "medium",
}


def check_condition_instance_list_effective_criticality_type_2_type_1(
    value: str,
) -> ConditionInstanceListEffectiveCriticalityType2Type1:
    if value in CONDITION_INSTANCE_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONDITION_INSTANCE_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
