from typing import Literal

PolicyEffectiveCriticalityType1 = Literal["high", "low", "medium"]

POLICY_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[PolicyEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_policy_effective_criticality_type_1(value: str) -> PolicyEffectiveCriticalityType1:
    if value in POLICY_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POLICY_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}")
