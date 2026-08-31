from typing import Literal

ApiV1EndpointsArchiveCreateActualAvailabilityErrorComponentAttr = Literal["actual_availability"]

API_V1_ENDPOINTS_ARCHIVE_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsArchiveCreateActualAvailabilityErrorComponentAttr
] = {
    "actual_availability",
}


def check_api_v1_endpoints_archive_create_actual_availability_error_component_attr(
    value: str,
) -> ApiV1EndpointsArchiveCreateActualAvailabilityErrorComponentAttr:
    if value in API_V1_ENDPOINTS_ARCHIVE_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_ARCHIVE_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
