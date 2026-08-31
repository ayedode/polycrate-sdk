from typing import Literal

ApiV1NotificationsSinksUpdateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_NOTIFICATIONS_SINKS_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksUpdateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_notifications_sinks_update_sla_availability_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksUpdateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
