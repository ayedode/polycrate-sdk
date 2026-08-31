from typing import Literal

ApiV1MaintenancesPartialUpdateNotificationStartedSentErrorComponentCode = Literal["invalid", "null"]

API_V1_MAINTENANCES_PARTIAL_UPDATE_NOTIFICATION_STARTED_SENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesPartialUpdateNotificationStartedSentErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_maintenances_partial_update_notification_started_sent_error_component_code(
    value: str,
) -> ApiV1MaintenancesPartialUpdateNotificationStartedSentErrorComponentCode:
    if value in API_V1_MAINTENANCES_PARTIAL_UPDATE_NOTIFICATION_STARTED_SENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_PARTIAL_UPDATE_NOTIFICATION_STARTED_SENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
