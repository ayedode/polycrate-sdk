from typing import Literal

ApiV1AlertroutersListCreatedByUsersErrorComponentCode = Literal["invalid_choice", "invalid_list", "invalid_pk_value"]

API_V1_ALERTROUTERS_LIST_CREATED_BY_USERS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertroutersListCreatedByUsersErrorComponentCode
] = {
    "invalid_choice",
    "invalid_list",
    "invalid_pk_value",
}


def check_api_v1_alertrouters_list_created_by_users_error_component_code(
    value: str,
) -> ApiV1AlertroutersListCreatedByUsersErrorComponentCode:
    if value in API_V1_ALERTROUTERS_LIST_CREATED_BY_USERS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_LIST_CREATED_BY_USERS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
