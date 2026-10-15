from typing import Literal

APMStackListEffectiveCriticalityType1 = Literal["high", "low", "medium"]

APM_STACK_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[APMStackListEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_apm_stack_list_effective_criticality_type_1(value: str) -> APMStackListEffectiveCriticalityType1:
    if value in APM_STACK_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {APM_STACK_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
