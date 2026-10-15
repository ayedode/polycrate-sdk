from typing import Literal

ProviderDetailCriticalityType1 = Literal["", "high", "low", "medium"]

PROVIDER_DETAIL_CRITICALITY_TYPE_1_VALUES: set[ProviderDetailCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_provider_detail_criticality_type_1(value: str) -> ProviderDetailCriticalityType1:
    if value in PROVIDER_DETAIL_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_DETAIL_CRITICALITY_TYPE_1_VALUES!r}")
