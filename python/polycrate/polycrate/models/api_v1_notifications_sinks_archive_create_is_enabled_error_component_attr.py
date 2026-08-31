from typing import Literal

ApiV1NotificationsSinksArchiveCreateIsEnabledErrorComponentAttr = Literal["is_enabled"]

API_V1_NOTIFICATIONS_SINKS_ARCHIVE_CREATE_IS_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksArchiveCreateIsEnabledErrorComponentAttr
] = {
    "is_enabled",
}


def check_api_v1_notifications_sinks_archive_create_is_enabled_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksArchiveCreateIsEnabledErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_ARCHIVE_CREATE_IS_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_ARCHIVE_CREATE_IS_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
