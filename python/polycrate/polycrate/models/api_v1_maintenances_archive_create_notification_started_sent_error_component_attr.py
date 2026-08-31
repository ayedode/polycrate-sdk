from typing import Literal

ApiV1MaintenancesArchiveCreateNotificationStartedSentErrorComponentAttr = Literal["notification_started_sent"]

API_V1_MAINTENANCES_ARCHIVE_CREATE_NOTIFICATION_STARTED_SENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesArchiveCreateNotificationStartedSentErrorComponentAttr
] = {
    "notification_started_sent",
}


def check_api_v1_maintenances_archive_create_notification_started_sent_error_component_attr(
    value: str,
) -> ApiV1MaintenancesArchiveCreateNotificationStartedSentErrorComponentAttr:
    if value in API_V1_MAINTENANCES_ARCHIVE_CREATE_NOTIFICATION_STARTED_SENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_ARCHIVE_CREATE_NOTIFICATION_STARTED_SENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
