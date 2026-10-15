from typing import Literal

IdentityProviderEffectiveCriticalityType1 = Literal["high", "low", "medium"]

IDENTITY_PROVIDER_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[IdentityProviderEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_identity_provider_effective_criticality_type_1(value: str) -> IdentityProviderEffectiveCriticalityType1:
    if value in IDENTITY_PROVIDER_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {IDENTITY_PROVIDER_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
