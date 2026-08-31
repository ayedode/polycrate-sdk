from typing import Literal

ApiV1NotificationsSinksPartialUpdateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1_NOTIFICATIONS_SINKS_PARTIAL_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksPartialUpdateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1_notifications_sinks_partial_update_target_availability_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksPartialUpdateTargetAvailabilityErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_PARTIAL_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_PARTIAL_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
