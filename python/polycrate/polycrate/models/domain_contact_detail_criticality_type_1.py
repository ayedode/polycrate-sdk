from typing import Literal

DomainContactDetailCriticalityType1 = Literal["", "high", "low", "medium"]

DOMAIN_CONTACT_DETAIL_CRITICALITY_TYPE_1_VALUES: set[DomainContactDetailCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_domain_contact_detail_criticality_type_1(value: str) -> DomainContactDetailCriticalityType1:
    if value in DOMAIN_CONTACT_DETAIL_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOMAIN_CONTACT_DETAIL_CRITICALITY_TYPE_1_VALUES!r}")
