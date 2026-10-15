from typing import Literal

ProviderAccountDetailCriticalityType2Type1 = Literal["", "high", "low", "medium"]

PROVIDER_ACCOUNT_DETAIL_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[ProviderAccountDetailCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_provider_account_detail_criticality_type_2_type_1(value: str) -> ProviderAccountDetailCriticalityType2Type1:
    if value in PROVIDER_ACCOUNT_DETAIL_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PROVIDER_ACCOUNT_DETAIL_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
