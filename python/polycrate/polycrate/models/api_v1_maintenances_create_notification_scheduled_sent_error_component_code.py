from typing import Literal

ApiV1MaintenancesCreateNotificationScheduledSentErrorComponentCode = Literal["invalid", "null"]

API_V1_MAINTENANCES_CREATE_NOTIFICATION_SCHEDULED_SENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesCreateNotificationScheduledSentErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_maintenances_create_notification_scheduled_sent_error_component_code(
    value: str,
) -> ApiV1MaintenancesCreateNotificationScheduledSentErrorComponentCode:
    if value in API_V1_MAINTENANCES_CREATE_NOTIFICATION_SCHEDULED_SENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_CREATE_NOTIFICATION_SCHEDULED_SENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
