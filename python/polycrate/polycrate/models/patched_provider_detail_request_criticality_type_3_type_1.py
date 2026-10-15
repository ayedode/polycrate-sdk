from typing import Literal

PatchedProviderDetailRequestCriticalityType3Type1 = Literal["", "high", "low", "medium"]

PATCHED_PROVIDER_DETAIL_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[
    PatchedProviderDetailRequestCriticalityType3Type1
] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_provider_detail_request_criticality_type_3_type_1(
    value: str,
) -> PatchedProviderDetailRequestCriticalityType3Type1:
    if value in PATCHED_PROVIDER_DETAIL_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_PROVIDER_DETAIL_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
