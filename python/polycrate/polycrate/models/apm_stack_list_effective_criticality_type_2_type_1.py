from typing import Literal

APMStackListEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

APM_STACK_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[APMStackListEffectiveCriticalityType2Type1] = {
    "high",
    "low",
    "medium",
}


def check_apm_stack_list_effective_criticality_type_2_type_1(value: str) -> APMStackListEffectiveCriticalityType2Type1:
    if value in APM_STACK_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {APM_STACK_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
