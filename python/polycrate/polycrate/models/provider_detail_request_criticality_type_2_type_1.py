from typing import Literal

ProviderDetailRequestCriticalityType2Type1 = Literal["", "high", "low", "medium"]

PROVIDER_DETAIL_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[ProviderDetailRequestCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_provider_detail_request_criticality_type_2_type_1(value: str) -> ProviderDetailRequestCriticalityType2Type1:
    if value in PROVIDER_DETAIL_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PROVIDER_DETAIL_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
