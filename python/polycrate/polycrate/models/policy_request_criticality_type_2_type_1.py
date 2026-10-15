from typing import Literal

PolicyRequestCriticalityType2Type1 = Literal["", "high", "low", "medium"]

POLICY_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[PolicyRequestCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_policy_request_criticality_type_2_type_1(value: str) -> PolicyRequestCriticalityType2Type1:
    if value in POLICY_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POLICY_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}")
