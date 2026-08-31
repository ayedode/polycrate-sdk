from typing import Literal

ApiV1OrganizationsUpdatePriorityErrorComponentCode = Literal["invalid", "null"]

API_V1_ORGANIZATIONS_UPDATE_PRIORITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsUpdatePriorityErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_organizations_update_priority_error_component_code(
    value: str,
) -> ApiV1OrganizationsUpdatePriorityErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_UPDATE_PRIORITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_PRIORITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
