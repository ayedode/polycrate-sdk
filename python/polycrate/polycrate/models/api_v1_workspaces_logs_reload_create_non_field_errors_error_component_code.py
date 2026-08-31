from typing import Literal

ApiV1WorkspacesLogsReloadCreateNonFieldErrorsErrorComponentCode = Literal["invalid", "null", "unique"]

API_V1_WORKSPACES_LOGS_RELOAD_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesLogsReloadCreateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
    "unique",
}


def check_api_v1_workspaces_logs_reload_create_non_field_errors_error_component_code(
    value: str,
) -> ApiV1WorkspacesLogsReloadCreateNonFieldErrorsErrorComponentCode:
    if value in API_V1_WORKSPACES_LOGS_RELOAD_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_LOGS_RELOAD_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
