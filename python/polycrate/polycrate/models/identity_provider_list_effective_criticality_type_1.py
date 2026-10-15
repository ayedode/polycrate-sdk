from typing import Literal

IdentityProviderListEffectiveCriticalityType1 = Literal["high", "low", "medium"]

IDENTITY_PROVIDER_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[IdentityProviderListEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_identity_provider_list_effective_criticality_type_1(
    value: str,
) -> IdentityProviderListEffectiveCriticalityType1:
    if value in IDENTITY_PROVIDER_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {IDENTITY_PROVIDER_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
