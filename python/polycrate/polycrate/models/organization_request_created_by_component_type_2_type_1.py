from typing import Literal

OrganizationRequestCreatedByComponentType2Type1 = Literal["", "api", "cli", "operator"]

ORGANIZATION_REQUEST_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES: set[OrganizationRequestCreatedByComponentType2Type1] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_organization_request_created_by_component_type_2_type_1(
    value: str,
) -> OrganizationRequestCreatedByComponentType2Type1:
    if value in ORGANIZATION_REQUEST_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ORGANIZATION_REQUEST_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES!r}"
    )
