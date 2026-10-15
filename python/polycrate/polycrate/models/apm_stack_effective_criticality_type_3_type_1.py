from typing import Literal

APMStackEffectiveCriticalityType3Type1 = Literal["high", "low", "medium"]

APM_STACK_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[APMStackEffectiveCriticalityType3Type1] = {
    "high",
    "low",
    "medium",
}


def check_apm_stack_effective_criticality_type_3_type_1(value: str) -> APMStackEffectiveCriticalityType3Type1:
    if value in APM_STACK_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {APM_STACK_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
