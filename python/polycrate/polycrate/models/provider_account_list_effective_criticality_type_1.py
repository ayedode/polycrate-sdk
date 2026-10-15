from typing import Literal

ProviderAccountListEffectiveCriticalityType1 = Literal["high", "low", "medium"]

PROVIDER_ACCOUNT_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[ProviderAccountListEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_provider_account_list_effective_criticality_type_1(
    value: str,
) -> ProviderAccountListEffectiveCriticalityType1:
    if value in PROVIDER_ACCOUNT_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PROVIDER_ACCOUNT_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
