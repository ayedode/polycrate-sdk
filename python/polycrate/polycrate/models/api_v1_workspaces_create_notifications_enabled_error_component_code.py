from typing import Literal

ApiV1WorkspacesCreateNotificationsEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_WORKSPACES_CREATE_NOTIFICATIONS_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesCreateNotificationsEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_workspaces_create_notifications_enabled_error_component_code(
    value: str,
) -> ApiV1WorkspacesCreateNotificationsEnabledErrorComponentCode:
    if value in API_V1_WORKSPACES_CREATE_NOTIFICATIONS_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CREATE_NOTIFICATIONS_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
