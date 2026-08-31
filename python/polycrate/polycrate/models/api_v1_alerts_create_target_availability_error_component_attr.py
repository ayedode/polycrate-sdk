from typing import Literal

ApiV1AlertsCreateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1_ALERTS_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsCreateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1_alerts_create_target_availability_error_component_attr(
    value: str,
) -> ApiV1AlertsCreateTargetAvailabilityErrorComponentAttr:
    if value in API_V1_ALERTS_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
