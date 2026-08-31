from typing import Literal

ApiV1WorkspacesUpdateNotificationsEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_WORKSPACES_UPDATE_NOTIFICATIONS_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesUpdateNotificationsEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_workspaces_update_notifications_enabled_error_component_code(
    value: str,
) -> ApiV1WorkspacesUpdateNotificationsEnabledErrorComponentCode:
    if value in API_V1_WORKSPACES_UPDATE_NOTIFICATIONS_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_UPDATE_NOTIFICATIONS_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
