from typing import Literal

ApiV1IncidentsPartialUpdateNotificationClosedSentErrorComponentAttr = Literal["notification_closed_sent"]

API_V1_INCIDENTS_PARTIAL_UPDATE_NOTIFICATION_CLOSED_SENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsPartialUpdateNotificationClosedSentErrorComponentAttr
] = {
    "notification_closed_sent",
}


def check_api_v1_incidents_partial_update_notification_closed_sent_error_component_attr(
    value: str,
) -> ApiV1IncidentsPartialUpdateNotificationClosedSentErrorComponentAttr:
    if value in API_V1_INCIDENTS_PARTIAL_UPDATE_NOTIFICATION_CLOSED_SENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_PARTIAL_UPDATE_NOTIFICATION_CLOSED_SENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
