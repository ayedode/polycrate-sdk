from typing import Literal

PolicyCriticalityType3Type1 = Literal["", "high", "low", "medium"]

POLICY_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[PolicyCriticalityType3Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_policy_criticality_type_3_type_1(value: str) -> PolicyCriticalityType3Type1:
    if value in POLICY_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POLICY_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}")
