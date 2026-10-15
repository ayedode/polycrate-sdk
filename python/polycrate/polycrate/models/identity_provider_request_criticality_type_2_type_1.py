from typing import Literal

IdentityProviderRequestCriticalityType2Type1 = Literal["", "high", "low", "medium"]

IDENTITY_PROVIDER_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[IdentityProviderRequestCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_identity_provider_request_criticality_type_2_type_1(
    value: str,
) -> IdentityProviderRequestCriticalityType2Type1:
    if value in IDENTITY_PROVIDER_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {IDENTITY_PROVIDER_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
