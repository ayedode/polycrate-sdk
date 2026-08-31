from typing import Literal

ApiV1NotificationsSinksArchiveCreateNameErrorComponentAttr = Literal["name"]

API_V1_NOTIFICATIONS_SINKS_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksArchiveCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_notifications_sinks_archive_create_name_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksArchiveCreateNameErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
