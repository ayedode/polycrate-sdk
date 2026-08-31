from typing import Literal

ApiV1MaintenancesPartialUpdateNotificationScheduledSentErrorComponentAttr = Literal["notification_scheduled_sent"]

API_V1_MAINTENANCES_PARTIAL_UPDATE_NOTIFICATION_SCHEDULED_SENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesPartialUpdateNotificationScheduledSentErrorComponentAttr
] = {
    "notification_scheduled_sent",
}


def check_api_v1_maintenances_partial_update_notification_scheduled_sent_error_component_attr(
    value: str,
) -> ApiV1MaintenancesPartialUpdateNotificationScheduledSentErrorComponentAttr:
    if value in API_V1_MAINTENANCES_PARTIAL_UPDATE_NOTIFICATION_SCHEDULED_SENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_PARTIAL_UPDATE_NOTIFICATION_SCHEDULED_SENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
