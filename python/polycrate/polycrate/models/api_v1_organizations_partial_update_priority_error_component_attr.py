from typing import Literal

ApiV1OrganizationsPartialUpdatePriorityErrorComponentAttr = Literal["priority"]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_PRIORITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsPartialUpdatePriorityErrorComponentAttr
] = {
    "priority",
}


def check_api_v1_organizations_partial_update_priority_error_component_attr(
    value: str,
) -> ApiV1OrganizationsPartialUpdatePriorityErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_PRIORITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_PRIORITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
