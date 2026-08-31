from typing import Literal

ApiV1MaintenancesCompleteEarlyCreateNotificationEndedSentErrorComponentCode = Literal["invalid", "null"]

API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_NOTIFICATION_ENDED_SENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesCompleteEarlyCreateNotificationEndedSentErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_maintenances_complete_early_create_notification_ended_sent_error_component_code(
    value: str,
) -> ApiV1MaintenancesCompleteEarlyCreateNotificationEndedSentErrorComponentCode:
    if value in API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_NOTIFICATION_ENDED_SENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_COMPLETE_EARLY_CREATE_NOTIFICATION_ENDED_SENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
