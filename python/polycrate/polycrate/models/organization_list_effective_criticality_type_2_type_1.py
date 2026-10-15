from typing import Literal

OrganizationListEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

ORGANIZATION_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[OrganizationListEffectiveCriticalityType2Type1] = {
    "high",
    "low",
    "medium",
}


def check_organization_list_effective_criticality_type_2_type_1(
    value: str,
) -> OrganizationListEffectiveCriticalityType2Type1:
    if value in ORGANIZATION_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ORGANIZATION_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
