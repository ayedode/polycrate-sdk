from typing import Literal

IdentityProviderRequestCriticalityType1 = Literal["", "high", "low", "medium"]

IDENTITY_PROVIDER_REQUEST_CRITICALITY_TYPE_1_VALUES: set[IdentityProviderRequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_identity_provider_request_criticality_type_1(value: str) -> IdentityProviderRequestCriticalityType1:
    if value in IDENTITY_PROVIDER_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {IDENTITY_PROVIDER_REQUEST_CRITICALITY_TYPE_1_VALUES!r}"
    )
