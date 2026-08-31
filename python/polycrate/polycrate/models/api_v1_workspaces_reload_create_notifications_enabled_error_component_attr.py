from typing import Literal

ApiV1WorkspacesReloadCreateNotificationsEnabledErrorComponentAttr = Literal["notifications_enabled"]

API_V1_WORKSPACES_RELOAD_CREATE_NOTIFICATIONS_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesReloadCreateNotificationsEnabledErrorComponentAttr
] = {
    "notifications_enabled",
}


def check_api_v1_workspaces_reload_create_notifications_enabled_error_component_attr(
    value: str,
) -> ApiV1WorkspacesReloadCreateNotificationsEnabledErrorComponentAttr:
    if value in API_V1_WORKSPACES_RELOAD_CREATE_NOTIFICATIONS_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RELOAD_CREATE_NOTIFICATIONS_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
