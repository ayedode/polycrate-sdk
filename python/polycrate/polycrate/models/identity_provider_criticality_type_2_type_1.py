from typing import Literal

IdentityProviderCriticalityType2Type1 = Literal["", "high", "low", "medium"]

IDENTITY_PROVIDER_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[IdentityProviderCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_identity_provider_criticality_type_2_type_1(value: str) -> IdentityProviderCriticalityType2Type1:
    if value in IDENTITY_PROVIDER_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {IDENTITY_PROVIDER_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
