from typing import Literal

ApiV1WorkspacesCreateNonFieldErrorsErrorComponentCode = Literal["invalid", "null", "unique"]

API_V1_WORKSPACES_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesCreateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
    "unique",
}


def check_api_v1_workspaces_create_non_field_errors_error_component_code(
    value: str,
) -> ApiV1WorkspacesCreateNonFieldErrorsErrorComponentCode:
    if value in API_V1_WORKSPACES_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
