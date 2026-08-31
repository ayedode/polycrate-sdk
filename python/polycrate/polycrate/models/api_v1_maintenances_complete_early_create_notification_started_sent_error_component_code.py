from typing import Literal

ApiV1MaintenancesCompleteEarlyCreateNotificationStartedSentErrorComponentCode = Literal["invalid", "null"]

API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_NOTIFICATION_STARTED_SENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesCompleteEarlyCreateNotificationStartedSentErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_maintenances_complete_early_create_notification_started_sent_error_component_code(
    value: str,
) -> ApiV1MaintenancesCompleteEarlyCreateNotificationStartedSentErrorComponentCode:
    if value in API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_NOTIFICATION_STARTED_SENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_NOTIFICATION_STARTED_SENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
