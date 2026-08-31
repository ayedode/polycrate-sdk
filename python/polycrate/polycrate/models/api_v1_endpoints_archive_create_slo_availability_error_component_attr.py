from typing import Literal

ApiV1EndpointsArchiveCreateSloAvailabilityErrorComponentAttr = Literal["slo_availability"]

API_V1_ENDPOINTS_ARCHIVE_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsArchiveCreateSloAvailabilityErrorComponentAttr
] = {
    "slo_availability",
}


def check_api_v1_endpoints_archive_create_slo_availability_error_component_attr(
    value: str,
) -> ApiV1EndpointsArchiveCreateSloAvailabilityErrorComponentAttr:
    if value in API_V1_ENDPOINTS_ARCHIVE_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_ARCHIVE_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
