from typing import Literal

ApiV1OrganizationsCreatePriorityErrorComponentAttr = Literal["priority"]

API_V1_ORGANIZATIONS_CREATE_PRIORITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsCreatePriorityErrorComponentAttr
] = {
    "priority",
}


def check_api_v1_organizations_create_priority_error_component_attr(
    value: str,
) -> ApiV1OrganizationsCreatePriorityErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_CREATE_PRIORITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_CREATE_PRIORITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
