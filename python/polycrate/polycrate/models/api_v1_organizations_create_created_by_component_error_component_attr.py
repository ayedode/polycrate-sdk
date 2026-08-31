from typing import Literal

ApiV1OrganizationsCreateCreatedByComponentErrorComponentAttr = Literal["created_by_component"]

API_V1_ORGANIZATIONS_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsCreateCreatedByComponentErrorComponentAttr
] = {
    "created_by_component",
}


def check_api_v1_organizations_create_created_by_component_error_component_attr(
    value: str,
) -> ApiV1OrganizationsCreateCreatedByComponentErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
