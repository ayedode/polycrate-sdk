from typing import Literal

ApiV1NotificationsSinksCreateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1_NOTIFICATIONS_SINKS_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksCreateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1_notifications_sinks_create_target_availability_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksCreateTargetAvailabilityErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
