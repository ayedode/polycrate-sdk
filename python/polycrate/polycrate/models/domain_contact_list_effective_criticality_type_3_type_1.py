from typing import Literal

DomainContactListEffectiveCriticalityType3Type1 = Literal["high", "low", "medium"]

DOMAIN_CONTACT_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[DomainContactListEffectiveCriticalityType3Type1] = {
    "high",
    "low",
    "medium",
}


def check_domain_contact_list_effective_criticality_type_3_type_1(
    value: str,
) -> DomainContactListEffectiveCriticalityType3Type1:
    if value in DOMAIN_CONTACT_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DOMAIN_CONTACT_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
