from typing import Literal

ProviderDetailEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

PROVIDER_DETAIL_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[ProviderDetailEffectiveCriticalityType2Type1] = {
    "high",
    "low",
    "medium",
}


def check_provider_detail_effective_criticality_type_2_type_1(
    value: str,
) -> ProviderDetailEffectiveCriticalityType2Type1:
    if value in PROVIDER_DETAIL_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PROVIDER_DETAIL_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
