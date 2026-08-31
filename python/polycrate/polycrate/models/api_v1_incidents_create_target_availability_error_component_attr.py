from typing import Literal

ApiV1IncidentsCreateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1_INCIDENTS_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsCreateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1_incidents_create_target_availability_error_component_attr(
    value: str,
) -> ApiV1IncidentsCreateTargetAvailabilityErrorComponentAttr:
    if value in API_V1_INCIDENTS_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
