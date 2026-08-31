from typing import Literal

ApiV1MaintenancesArchiveCreateNotificationEndedSentErrorComponentAttr = Literal["notification_ended_sent"]

API_V1_MAINTENANCES_ARCHIVE_CREATE_NOTIFICATION_ENDED_SENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesArchiveCreateNotificationEndedSentErrorComponentAttr
] = {
    "notification_ended_sent",
}


def check_api_v1_maintenances_archive_create_notification_ended_sent_error_component_attr(
    value: str,
) -> ApiV1MaintenancesArchiveCreateNotificationEndedSentErrorComponentAttr:
    if value in API_V1_MAINTENANCES_ARCHIVE_CREATE_NOTIFICATION_ENDED_SENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_ARCHIVE_CREATE_NOTIFICATION_ENDED_SENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
