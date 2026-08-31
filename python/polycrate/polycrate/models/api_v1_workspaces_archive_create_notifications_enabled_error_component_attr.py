from typing import Literal

ApiV1WorkspacesArchiveCreateNotificationsEnabledErrorComponentAttr = Literal["notifications_enabled"]

API_V1_WORKSPACES_ARCHIVE_CREATE_NOTIFICATIONS_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesArchiveCreateNotificationsEnabledErrorComponentAttr
] = {
    "notifications_enabled",
}


def check_api_v1_workspaces_archive_create_notifications_enabled_error_component_attr(
    value: str,
) -> ApiV1WorkspacesArchiveCreateNotificationsEnabledErrorComponentAttr:
    if value in API_V1_WORKSPACES_ARCHIVE_CREATE_NOTIFICATIONS_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_ARCHIVE_CREATE_NOTIFICATIONS_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
