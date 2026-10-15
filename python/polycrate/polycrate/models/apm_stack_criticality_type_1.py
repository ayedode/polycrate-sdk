from typing import Literal

APMStackCriticalityType1 = Literal["", "high", "low", "medium"]

APM_STACK_CRITICALITY_TYPE_1_VALUES: set[APMStackCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_apm_stack_criticality_type_1(value: str) -> APMStackCriticalityType1:
    if value in APM_STACK_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {APM_STACK_CRITICALITY_TYPE_1_VALUES!r}")
