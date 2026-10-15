from typing import Literal

DomainListEffectiveCriticalityType1 = Literal["high", "low", "medium"]

DOMAIN_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[DomainListEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_domain_list_effective_criticality_type_1(value: str) -> DomainListEffectiveCriticalityType1:
    if value in DOMAIN_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOMAIN_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}")
