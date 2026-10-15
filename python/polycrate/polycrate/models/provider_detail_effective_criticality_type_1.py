from typing import Literal

ProviderDetailEffectiveCriticalityType1 = Literal["high", "low", "medium"]

PROVIDER_DETAIL_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[ProviderDetailEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_provider_detail_effective_criticality_type_1(value: str) -> ProviderDetailEffectiveCriticalityType1:
    if value in PROVIDER_DETAIL_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PROVIDER_DETAIL_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
