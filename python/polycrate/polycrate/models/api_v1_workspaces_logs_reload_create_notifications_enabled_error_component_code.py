from typing import Literal

ApiV1WorkspacesLogsReloadCreateNotificationsEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_WORKSPACES_LOGS_RELOAD_CREATE_NOTIFICATIONS_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesLogsReloadCreateNotificationsEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_workspaces_logs_reload_create_notifications_enabled_error_component_code(
    value: str,
) -> ApiV1WorkspacesLogsReloadCreateNotificationsEnabledErrorComponentCode:
    if value in API_V1_WORKSPACES_LOGS_RELOAD_CREATE_NOTIFICATIONS_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_LOGS_RELOAD_CREATE_NOTIFICATIONS_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
