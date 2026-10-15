from typing import Literal

ProviderDetailCriticalityType3Type1 = Literal["", "high", "low", "medium"]

PROVIDER_DETAIL_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[ProviderDetailCriticalityType3Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_provider_detail_criticality_type_3_type_1(value: str) -> ProviderDetailCriticalityType3Type1:
    if value in PROVIDER_DETAIL_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_DETAIL_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}")
