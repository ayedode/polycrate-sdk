from typing import Literal

ApiV1IncidentsCreateNotificationOpenedSentErrorComponentCode = Literal["invalid", "null"]

API_V1_INCIDENTS_CREATE_NOTIFICATION_OPENED_SENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IncidentsCreateNotificationOpenedSentErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_incidents_create_notification_opened_sent_error_component_code(
    value: str,
) -> ApiV1IncidentsCreateNotificationOpenedSentErrorComponentCode:
    if value in API_V1_INCIDENTS_CREATE_NOTIFICATION_OPENED_SENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_CREATE_NOTIFICATION_OPENED_SENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
