from typing import Literal

OrganizationListEffectiveCriticalityType1 = Literal["high", "low", "medium"]

ORGANIZATION_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[OrganizationListEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_organization_list_effective_criticality_type_1(value: str) -> OrganizationListEffectiveCriticalityType1:
    if value in ORGANIZATION_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ORGANIZATION_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
