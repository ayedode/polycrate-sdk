from typing import Literal

OrganizationCreatedByComponentType3Type1 = Literal["", "api", "cli", "operator"]

ORGANIZATION_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES: set[OrganizationCreatedByComponentType3Type1] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_organization_created_by_component_type_3_type_1(value: str) -> OrganizationCreatedByComponentType3Type1:
    if value in ORGANIZATION_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ORGANIZATION_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES!r}"
    )
