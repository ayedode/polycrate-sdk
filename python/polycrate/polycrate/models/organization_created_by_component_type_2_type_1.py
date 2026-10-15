from typing import Literal

OrganizationCreatedByComponentType2Type1 = Literal["", "api", "cli", "operator"]

ORGANIZATION_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES: set[OrganizationCreatedByComponentType2Type1] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_organization_created_by_component_type_2_type_1(value: str) -> OrganizationCreatedByComponentType2Type1:
    if value in ORGANIZATION_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ORGANIZATION_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES!r}"
    )
