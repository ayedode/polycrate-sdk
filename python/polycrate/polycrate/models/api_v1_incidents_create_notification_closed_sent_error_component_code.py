from typing import Literal

ApiV1IncidentsCreateNotificationClosedSentErrorComponentCode = Literal["invalid", "null"]

API_V1_INCIDENTS_CREATE_NOTIFICATION_CLOSED_SENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IncidentsCreateNotificationClosedSentErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_incidents_create_notification_closed_sent_error_component_code(
    value: str,
) -> ApiV1IncidentsCreateNotificationClosedSentErrorComponentCode:
    if value in API_V1_INCIDENTS_CREATE_NOTIFICATION_CLOSED_SENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_CREATE_NOTIFICATION_CLOSED_SENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
