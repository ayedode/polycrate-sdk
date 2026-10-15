from typing import Literal

PatchedIdentityProviderRequestCriticalityType3Type1 = Literal["", "high", "low", "medium"]

PATCHED_IDENTITY_PROVIDER_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[
    PatchedIdentityProviderRequestCriticalityType3Type1
] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_identity_provider_request_criticality_type_3_type_1(
    value: str,
) -> PatchedIdentityProviderRequestCriticalityType3Type1:
    if value in PATCHED_IDENTITY_PROVIDER_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_IDENTITY_PROVIDER_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
