from typing import Literal

ApiV1NotificationsSinksArchiveCreateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_NOTIFICATIONS_SINKS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotificationsSinksArchiveCreateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_notifications_sinks_archive_create_archived_error_component_code(
    value: str,
) -> ApiV1NotificationsSinksArchiveCreateArchivedErrorComponentCode:
    if value in API_V1_NOTIFICATIONS_SINKS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
