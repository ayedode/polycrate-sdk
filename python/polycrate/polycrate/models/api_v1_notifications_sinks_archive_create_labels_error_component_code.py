from typing import Literal

ApiV1NotificationsSinksArchiveCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_NOTIFICATIONS_SINKS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotificationsSinksArchiveCreateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_notifications_sinks_archive_create_labels_error_component_code(
    value: str,
) -> ApiV1NotificationsSinksArchiveCreateLabelsErrorComponentCode:
    if value in API_V1_NOTIFICATIONS_SINKS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
