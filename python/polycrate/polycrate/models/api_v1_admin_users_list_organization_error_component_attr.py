from typing import Literal

ApiV1AdminUsersListOrganizationErrorComponentAttr = Literal["organization"]

API_V1_ADMIN_USERS_LIST_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AdminUsersListOrganizationErrorComponentAttr
] = {
    "organization",
}


def check_api_v1_admin_users_list_organization_error_component_attr(
    value: str,
) -> ApiV1AdminUsersListOrganizationErrorComponentAttr:
    if value in API_V1_ADMIN_USERS_LIST_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ADMIN_USERS_LIST_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
