from typing import Literal

ApiV1IncidentsArchiveCreateNotificationClosedSentErrorComponentCode = Literal["invalid", "null"]

API_V1_INCIDENTS_ARCHIVE_CREATE_NOTIFICATION_CLOSED_SENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IncidentsArchiveCreateNotificationClosedSentErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_incidents_archive_create_notification_closed_sent_error_component_code(
    value: str,
) -> ApiV1IncidentsArchiveCreateNotificationClosedSentErrorComponentCode:
    if value in API_V1_INCIDENTS_ARCHIVE_CREATE_NOTIFICATION_CLOSED_SENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_ARCHIVE_CREATE_NOTIFICATION_CLOSED_SENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
