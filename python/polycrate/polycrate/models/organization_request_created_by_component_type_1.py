from typing import Literal

OrganizationRequestCreatedByComponentType1 = Literal["", "api", "cli", "operator"]

ORGANIZATION_REQUEST_CREATED_BY_COMPONENT_TYPE_1_VALUES: set[OrganizationRequestCreatedByComponentType1] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_organization_request_created_by_component_type_1(value: str) -> OrganizationRequestCreatedByComponentType1:
    if value in ORGANIZATION_REQUEST_CREATED_BY_COMPONENT_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ORGANIZATION_REQUEST_CREATED_BY_COMPONENT_TYPE_1_VALUES!r}"
    )
