from typing import Literal

DomainPublicDetailEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

DOMAIN_PUBLIC_DETAIL_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[
    DomainPublicDetailEffectiveCriticalityType2Type1
] = {
    "high",
    "low",
    "medium",
}


def check_domain_public_detail_effective_criticality_type_2_type_1(
    value: str,
) -> DomainPublicDetailEffectiveCriticalityType2Type1:
    if value in DOMAIN_PUBLIC_DETAIL_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DOMAIN_PUBLIC_DETAIL_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
