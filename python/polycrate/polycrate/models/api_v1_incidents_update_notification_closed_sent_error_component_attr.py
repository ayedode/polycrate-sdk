from typing import Literal

ApiV1IncidentsUpdateNotificationClosedSentErrorComponentAttr = Literal["notification_closed_sent"]

API_V1_INCIDENTS_UPDATE_NOTIFICATION_CLOSED_SENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsUpdateNotificationClosedSentErrorComponentAttr
] = {
    "notification_closed_sent",
}


def check_api_v1_incidents_update_notification_closed_sent_error_component_attr(
    value: str,
) -> ApiV1IncidentsUpdateNotificationClosedSentErrorComponentAttr:
    if value in API_V1_INCIDENTS_UPDATE_NOTIFICATION_CLOSED_SENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_UPDATE_NOTIFICATION_CLOSED_SENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
