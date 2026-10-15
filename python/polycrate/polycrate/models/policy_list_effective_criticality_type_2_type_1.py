from typing import Literal

PolicyListEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

POLICY_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[PolicyListEffectiveCriticalityType2Type1] = {
    "high",
    "low",
    "medium",
}


def check_policy_list_effective_criticality_type_2_type_1(value: str) -> PolicyListEffectiveCriticalityType2Type1:
    if value in POLICY_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {POLICY_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
