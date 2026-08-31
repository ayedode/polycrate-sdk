from typing import Literal

ApiV1AdminUsersCreateNonFieldErrorsErrorComponentCode = Literal["invalid", "null"]

API_V1_ADMIN_USERS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AdminUsersCreateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_admin_users_create_non_field_errors_error_component_code(
    value: str,
) -> ApiV1AdminUsersCreateNonFieldErrorsErrorComponentCode:
    if value in API_V1_ADMIN_USERS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ADMIN_USERS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
