from typing import Literal

DomainRegistrarDetailCriticalityType1 = Literal["", "high", "low", "medium"]

DOMAIN_REGISTRAR_DETAIL_CRITICALITY_TYPE_1_VALUES: set[DomainRegistrarDetailCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_domain_registrar_detail_criticality_type_1(value: str) -> DomainRegistrarDetailCriticalityType1:
    if value in DOMAIN_REGISTRAR_DETAIL_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DOMAIN_REGISTRAR_DETAIL_CRITICALITY_TYPE_1_VALUES!r}"
    )
