from typing import Literal

OrganizationCriticalityType3Type1 = Literal["", "high", "low", "medium"]

ORGANIZATION_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[OrganizationCriticalityType3Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_organization_criticality_type_3_type_1(value: str) -> OrganizationCriticalityType3Type1:
    if value in ORGANIZATION_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ORGANIZATION_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}")
