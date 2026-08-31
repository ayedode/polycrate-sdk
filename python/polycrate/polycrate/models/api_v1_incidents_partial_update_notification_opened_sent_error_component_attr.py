from typing import Literal

ApiV1IncidentsPartialUpdateNotificationOpenedSentErrorComponentAttr = Literal["notification_opened_sent"]

API_V1_INCIDENTS_PARTIAL_UPDATE_NOTIFICATION_OPENED_SENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsPartialUpdateNotificationOpenedSentErrorComponentAttr
] = {
    "notification_opened_sent",
}


def check_api_v1_incidents_partial_update_notification_opened_sent_error_component_attr(
    value: str,
) -> ApiV1IncidentsPartialUpdateNotificationOpenedSentErrorComponentAttr:
    if value in API_V1_INCIDENTS_PARTIAL_UPDATE_NOTIFICATION_OPENED_SENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_PARTIAL_UPDATE_NOTIFICATION_OPENED_SENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
