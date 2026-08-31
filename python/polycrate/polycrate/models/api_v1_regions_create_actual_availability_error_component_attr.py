from typing import Literal

ApiV1RegionsCreateActualAvailabilityErrorComponentAttr = Literal["actual_availability"]

API_V1_REGIONS_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegionsCreateActualAvailabilityErrorComponentAttr
] = {
    "actual_availability",
}


def check_api_v1_regions_create_actual_availability_error_component_attr(
    value: str,
) -> ApiV1RegionsCreateActualAvailabilityErrorComponentAttr:
    if value in API_V1_REGIONS_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
