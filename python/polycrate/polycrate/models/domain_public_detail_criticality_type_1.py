from typing import Literal

DomainPublicDetailCriticalityType1 = Literal["", "high", "low", "medium"]

DOMAIN_PUBLIC_DETAIL_CRITICALITY_TYPE_1_VALUES: set[DomainPublicDetailCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_domain_public_detail_criticality_type_1(value: str) -> DomainPublicDetailCriticalityType1:
    if value in DOMAIN_PUBLIC_DETAIL_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOMAIN_PUBLIC_DETAIL_CRITICALITY_TYPE_1_VALUES!r}")
