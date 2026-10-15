from typing import Literal

PolicyListEffectiveCriticalityType1 = Literal["high", "low", "medium"]

POLICY_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[PolicyListEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_policy_list_effective_criticality_type_1(value: str) -> PolicyListEffectiveCriticalityType1:
    if value in POLICY_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POLICY_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}")
