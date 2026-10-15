from typing import Literal

ProviderAccountDetailRequestCriticalityType1 = Literal["", "high", "low", "medium"]

PROVIDER_ACCOUNT_DETAIL_REQUEST_CRITICALITY_TYPE_1_VALUES: set[ProviderAccountDetailRequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_provider_account_detail_request_criticality_type_1(
    value: str,
) -> ProviderAccountDetailRequestCriticalityType1:
    if value in PROVIDER_ACCOUNT_DETAIL_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PROVIDER_ACCOUNT_DETAIL_REQUEST_CRITICALITY_TYPE_1_VALUES!r}"
    )
