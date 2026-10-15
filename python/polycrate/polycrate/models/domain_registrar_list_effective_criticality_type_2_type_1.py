from typing import Literal

DomainRegistrarListEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

DOMAIN_REGISTRAR_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[
    DomainRegistrarListEffectiveCriticalityType2Type1
] = {
    "high",
    "low",
    "medium",
}


def check_domain_registrar_list_effective_criticality_type_2_type_1(
    value: str,
) -> DomainRegistrarListEffectiveCriticalityType2Type1:
    if value in DOMAIN_REGISTRAR_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DOMAIN_REGISTRAR_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
