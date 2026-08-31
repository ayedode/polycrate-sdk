from typing import Literal

ApiV1MaintenancesUpdateNotificationStartedSentErrorComponentAttr = Literal["notification_started_sent"]

API_V1_MAINTENANCES_UPDATE_NOTIFICATION_STARTED_SENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesUpdateNotificationStartedSentErrorComponentAttr
] = {
    "notification_started_sent",
}


def check_api_v1_maintenances_update_notification_started_sent_error_component_attr(
    value: str,
) -> ApiV1MaintenancesUpdateNotificationStartedSentErrorComponentAttr:
    if value in API_V1_MAINTENANCES_UPDATE_NOTIFICATION_STARTED_SENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_UPDATE_NOTIFICATION_STARTED_SENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
