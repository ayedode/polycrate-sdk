from typing import Literal

ApiV1IncidentsArchiveCreateNotificationOpenedSentErrorComponentAttr = Literal["notification_opened_sent"]

API_V1_INCIDENTS_ARCHIVE_CREATE_NOTIFICATION_OPENED_SENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsArchiveCreateNotificationOpenedSentErrorComponentAttr
] = {
    "notification_opened_sent",
}


def check_api_v1_incidents_archive_create_notification_opened_sent_error_component_attr(
    value: str,
) -> ApiV1IncidentsArchiveCreateNotificationOpenedSentErrorComponentAttr:
    if value in API_V1_INCIDENTS_ARCHIVE_CREATE_NOTIFICATION_OPENED_SENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_ARCHIVE_CREATE_NOTIFICATION_OPENED_SENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
