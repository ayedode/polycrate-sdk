from typing import Literal

ApiV1IncidentsCreateNotificationOpenedSentErrorComponentAttr = Literal["notification_opened_sent"]

API_V1_INCIDENTS_CREATE_NOTIFICATION_OPENED_SENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsCreateNotificationOpenedSentErrorComponentAttr
] = {
    "notification_opened_sent",
}


def check_api_v1_incidents_create_notification_opened_sent_error_component_attr(
    value: str,
) -> ApiV1IncidentsCreateNotificationOpenedSentErrorComponentAttr:
    if value in API_V1_INCIDENTS_CREATE_NOTIFICATION_OPENED_SENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_CREATE_NOTIFICATION_OPENED_SENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
