from typing import Literal

PatchedProviderAccountDetailRequestCriticalityType1 = Literal["", "high", "low", "medium"]

PATCHED_PROVIDER_ACCOUNT_DETAIL_REQUEST_CRITICALITY_TYPE_1_VALUES: set[
    PatchedProviderAccountDetailRequestCriticalityType1
] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_provider_account_detail_request_criticality_type_1(
    value: str,
) -> PatchedProviderAccountDetailRequestCriticalityType1:
    if value in PATCHED_PROVIDER_ACCOUNT_DETAIL_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_PROVIDER_ACCOUNT_DETAIL_REQUEST_CRITICALITY_TYPE_1_VALUES!r}"
    )
