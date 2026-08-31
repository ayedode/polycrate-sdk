from typing import Literal

ApiV1UsersMembershipsCreateNonFieldErrorsErrorComponentCode = Literal["invalid", "null"]

API_V1_USERS_MEMBERSHIPS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1UsersMembershipsCreateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_users_memberships_create_non_field_errors_error_component_code(
    value: str,
) -> ApiV1UsersMembershipsCreateNonFieldErrorsErrorComponentCode:
    if value in API_V1_USERS_MEMBERSHIPS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_USERS_MEMBERSHIPS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
