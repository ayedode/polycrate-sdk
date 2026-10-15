from typing import Literal

APMStackEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

APM_STACK_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[APMStackEffectiveCriticalityType2Type1] = {
    "high",
    "low",
    "medium",
}


def check_apm_stack_effective_criticality_type_2_type_1(value: str) -> APMStackEffectiveCriticalityType2Type1:
    if value in APM_STACK_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {APM_STACK_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
