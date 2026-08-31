from typing import Literal

ApiV1WorkspacesLogsReloadCreateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_WORKSPACES_LOGS_RELOAD_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesLogsReloadCreateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_workspaces_logs_reload_create_kind_error_component_code(
    value: str,
) -> ApiV1WorkspacesLogsReloadCreateKindErrorComponentCode:
    if value in API_V1_WORKSPACES_LOGS_RELOAD_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_LOGS_RELOAD_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
