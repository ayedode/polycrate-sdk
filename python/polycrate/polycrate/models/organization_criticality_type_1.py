from typing import Literal

OrganizationCriticalityType1 = Literal["", "high", "low", "medium"]

ORGANIZATION_CRITICALITY_TYPE_1_VALUES: set[OrganizationCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_organization_criticality_type_1(value: str) -> OrganizationCriticalityType1:
    if value in ORGANIZATION_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ORGANIZATION_CRITICALITY_TYPE_1_VALUES!r}")
