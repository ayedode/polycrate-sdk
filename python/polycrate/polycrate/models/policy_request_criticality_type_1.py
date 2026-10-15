from typing import Literal

PolicyRequestCriticalityType1 = Literal["", "high", "low", "medium"]

POLICY_REQUEST_CRITICALITY_TYPE_1_VALUES: set[PolicyRequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_policy_request_criticality_type_1(value: str) -> PolicyRequestCriticalityType1:
    if value in POLICY_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POLICY_REQUEST_CRITICALITY_TYPE_1_VALUES!r}")
