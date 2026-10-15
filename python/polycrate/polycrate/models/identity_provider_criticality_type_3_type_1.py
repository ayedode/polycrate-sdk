from typing import Literal

IdentityProviderCriticalityType3Type1 = Literal["", "high", "low", "medium"]

IDENTITY_PROVIDER_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[IdentityProviderCriticalityType3Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_identity_provider_criticality_type_3_type_1(value: str) -> IdentityProviderCriticalityType3Type1:
    if value in IDENTITY_PROVIDER_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {IDENTITY_PROVIDER_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
