from typing import Literal

ApiV1NotificationsSinksArchiveCreateConfigErrorComponentAttr = Literal["config"]

API_V1_NOTIFICATIONS_SINKS_ARCHIVE_CREATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksArchiveCreateConfigErrorComponentAttr
] = {
    "config",
}


def check_api_v1_notifications_sinks_archive_create_config_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksArchiveCreateConfigErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_ARCHIVE_CREATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_ARCHIVE_CREATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
