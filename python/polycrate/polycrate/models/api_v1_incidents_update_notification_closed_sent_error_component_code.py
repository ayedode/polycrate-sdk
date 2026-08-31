from typing import Literal

ApiV1IncidentsUpdateNotificationClosedSentErrorComponentCode = Literal["invalid", "null"]

API_V1_INCIDENTS_UPDATE_NOTIFICATION_CLOSED_SENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IncidentsUpdateNotificationClosedSentErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_incidents_update_notification_closed_sent_error_component_code(
    value: str,
) -> ApiV1IncidentsUpdateNotificationClosedSentErrorComponentCode:
    if value in API_V1_INCIDENTS_UPDATE_NOTIFICATION_CLOSED_SENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_UPDATE_NOTIFICATION_CLOSED_SENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
