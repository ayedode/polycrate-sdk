from typing import Literal

ApiV1MaintenancesCreateNotificationStartedSentErrorComponentAttr = Literal["notification_started_sent"]

API_V1_MAINTENANCES_CREATE_NOTIFICATION_STARTED_SENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesCreateNotificationStartedSentErrorComponentAttr
] = {
    "notification_started_sent",
}


def check_api_v1_maintenances_create_notification_started_sent_error_component_attr(
    value: str,
) -> ApiV1MaintenancesCreateNotificationStartedSentErrorComponentAttr:
    if value in API_V1_MAINTENANCES_CREATE_NOTIFICATION_STARTED_SENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_CREATE_NOTIFICATION_STARTED_SENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
