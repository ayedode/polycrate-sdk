from typing import Literal

ApiV1WorkspacesLogsReloadCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_WORKSPACES_LOGS_RELOAD_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesLogsReloadCreateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_workspaces_logs_reload_create_labels_error_component_code(
    value: str,
) -> ApiV1WorkspacesLogsReloadCreateLabelsErrorComponentCode:
    if value in API_V1_WORKSPACES_LOGS_RELOAD_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_LOGS_RELOAD_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
