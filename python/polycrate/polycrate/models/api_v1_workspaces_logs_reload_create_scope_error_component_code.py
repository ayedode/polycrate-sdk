from typing import Literal

ApiV1WorkspacesLogsReloadCreateScopeErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_WORKSPACES_LOGS_RELOAD_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesLogsReloadCreateScopeErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_workspaces_logs_reload_create_scope_error_component_code(
    value: str,
) -> ApiV1WorkspacesLogsReloadCreateScopeErrorComponentCode:
    if value in API_V1_WORKSPACES_LOGS_RELOAD_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_LOGS_RELOAD_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
