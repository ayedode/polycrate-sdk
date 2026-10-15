from typing import Literal

DomainRegistrarDetailEffectiveCriticalityType1 = Literal["high", "low", "medium"]

DOMAIN_REGISTRAR_DETAIL_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[DomainRegistrarDetailEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_domain_registrar_detail_effective_criticality_type_1(
    value: str,
) -> DomainRegistrarDetailEffectiveCriticalityType1:
    if value in DOMAIN_REGISTRAR_DETAIL_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DOMAIN_REGISTRAR_DETAIL_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
