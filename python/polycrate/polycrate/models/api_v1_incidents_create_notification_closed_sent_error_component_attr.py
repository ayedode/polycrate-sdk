from typing import Literal

ApiV1IncidentsCreateNotificationClosedSentErrorComponentAttr = Literal["notification_closed_sent"]

API_V1_INCIDENTS_CREATE_NOTIFICATION_CLOSED_SENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsCreateNotificationClosedSentErrorComponentAttr
] = {
    "notification_closed_sent",
}


def check_api_v1_incidents_create_notification_closed_sent_error_component_attr(
    value: str,
) -> ApiV1IncidentsCreateNotificationClosedSentErrorComponentAttr:
    if value in API_V1_INCIDENTS_CREATE_NOTIFICATION_CLOSED_SENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_CREATE_NOTIFICATION_CLOSED_SENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
