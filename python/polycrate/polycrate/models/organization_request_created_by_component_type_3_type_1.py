from typing import Literal

OrganizationRequestCreatedByComponentType3Type1 = Literal["", "api", "cli", "operator"]

ORGANIZATION_REQUEST_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES: set[OrganizationRequestCreatedByComponentType3Type1] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_organization_request_created_by_component_type_3_type_1(
    value: str,
) -> OrganizationRequestCreatedByComponentType3Type1:
    if value in ORGANIZATION_REQUEST_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ORGANIZATION_REQUEST_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES!r}"
    )
