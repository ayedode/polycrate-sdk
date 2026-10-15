from typing import Literal

OrganizationCriticalityType2Type1 = Literal["", "high", "low", "medium"]

ORGANIZATION_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[OrganizationCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_organization_criticality_type_2_type_1(value: str) -> OrganizationCriticalityType2Type1:
    if value in ORGANIZATION_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ORGANIZATION_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}")
