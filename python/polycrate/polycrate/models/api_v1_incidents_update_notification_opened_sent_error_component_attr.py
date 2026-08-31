from typing import Literal

ApiV1IncidentsUpdateNotificationOpenedSentErrorComponentAttr = Literal["notification_opened_sent"]

API_V1_INCIDENTS_UPDATE_NOTIFICATION_OPENED_SENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsUpdateNotificationOpenedSentErrorComponentAttr
] = {
    "notification_opened_sent",
}


def check_api_v1_incidents_update_notification_opened_sent_error_component_attr(
    value: str,
) -> ApiV1IncidentsUpdateNotificationOpenedSentErrorComponentAttr:
    if value in API_V1_INCIDENTS_UPDATE_NOTIFICATION_OPENED_SENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_UPDATE_NOTIFICATION_OPENED_SENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
