from typing import Literal

ApiV1NotificationsSinksCreateSloAvailabilityErrorComponentAttr = Literal["slo_availability"]

API_V1_NOTIFICATIONS_SINKS_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksCreateSloAvailabilityErrorComponentAttr
] = {
    "slo_availability",
}


def check_api_v1_notifications_sinks_create_slo_availability_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksCreateSloAvailabilityErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
