from typing import Literal

DomainContactDetailEffectiveCriticalityType1 = Literal["high", "low", "medium"]

DOMAIN_CONTACT_DETAIL_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[DomainContactDetailEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_domain_contact_detail_effective_criticality_type_1(
    value: str,
) -> DomainContactDetailEffectiveCriticalityType1:
    if value in DOMAIN_CONTACT_DETAIL_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DOMAIN_CONTACT_DETAIL_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
