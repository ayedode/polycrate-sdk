from typing import Literal

ApiV1MaintenancesUpdateNotificationScheduledSentErrorComponentAttr = Literal["notification_scheduled_sent"]

API_V1_MAINTENANCES_UPDATE_NOTIFICATION_SCHEDULED_SENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesUpdateNotificationScheduledSentErrorComponentAttr
] = {
    "notification_scheduled_sent",
}


def check_api_v1_maintenances_update_notification_scheduled_sent_error_component_attr(
    value: str,
) -> ApiV1MaintenancesUpdateNotificationScheduledSentErrorComponentAttr:
    if value in API_V1_MAINTENANCES_UPDATE_NOTIFICATION_SCHEDULED_SENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_UPDATE_NOTIFICATION_SCHEDULED_SENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
