from typing import Literal

ApiV1WorkspacesLogsReloadCreateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_WORKSPACES_LOGS_RELOAD_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesLogsReloadCreateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_workspaces_logs_reload_create_archived_error_component_code(
    value: str,
) -> ApiV1WorkspacesLogsReloadCreateArchivedErrorComponentCode:
    if value in API_V1_WORKSPACES_LOGS_RELOAD_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_LOGS_RELOAD_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
