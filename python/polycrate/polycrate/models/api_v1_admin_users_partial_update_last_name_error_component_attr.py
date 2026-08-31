from typing import Literal

ApiV1AdminUsersPartialUpdateLastNameErrorComponentAttr = Literal["last_name"]

API_V1_ADMIN_USERS_PARTIAL_UPDATE_LAST_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AdminUsersPartialUpdateLastNameErrorComponentAttr
] = {
    "last_name",
}


def check_api_v1_admin_users_partial_update_last_name_error_component_attr(
    value: str,
) -> ApiV1AdminUsersPartialUpdateLastNameErrorComponentAttr:
    if value in API_V1_ADMIN_USERS_PARTIAL_UPDATE_LAST_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ADMIN_USERS_PARTIAL_UPDATE_LAST_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
