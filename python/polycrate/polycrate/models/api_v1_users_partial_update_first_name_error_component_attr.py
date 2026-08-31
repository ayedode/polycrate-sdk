from typing import Literal

ApiV1UsersPartialUpdateFirstNameErrorComponentAttr = Literal["first_name"]

API_V1_USERS_PARTIAL_UPDATE_FIRST_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1UsersPartialUpdateFirstNameErrorComponentAttr
] = {
    "first_name",
}


def check_api_v1_users_partial_update_first_name_error_component_attr(
    value: str,
) -> ApiV1UsersPartialUpdateFirstNameErrorComponentAttr:
    if value in API_V1_USERS_PARTIAL_UPDATE_FIRST_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_USERS_PARTIAL_UPDATE_FIRST_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
