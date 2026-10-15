from typing import Literal

DomainRegistrarListEffectiveCriticalityType1 = Literal["high", "low", "medium"]

DOMAIN_REGISTRAR_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[DomainRegistrarListEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_domain_registrar_list_effective_criticality_type_1(
    value: str,
) -> DomainRegistrarListEffectiveCriticalityType1:
    if value in DOMAIN_REGISTRAR_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DOMAIN_REGISTRAR_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
