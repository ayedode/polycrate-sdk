from typing import Literal

ApiV1WorkspacesDiscoverCreateNotificationsEnabledErrorComponentAttr = Literal["notifications_enabled"]

API_V1_WORKSPACES_DISCOVER_CREATE_NOTIFICATIONS_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesDiscoverCreateNotificationsEnabledErrorComponentAttr
] = {
    "notifications_enabled",
}


def check_api_v1_workspaces_discover_create_notifications_enabled_error_component_attr(
    value: str,
) -> ApiV1WorkspacesDiscoverCreateNotificationsEnabledErrorComponentAttr:
    if value in API_V1_WORKSPACES_DISCOVER_CREATE_NOTIFICATIONS_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_DISCOVER_CREATE_NOTIFICATIONS_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
