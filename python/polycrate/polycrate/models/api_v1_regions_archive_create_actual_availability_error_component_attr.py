from typing import Literal

ApiV1RegionsArchiveCreateActualAvailabilityErrorComponentAttr = Literal["actual_availability"]

API_V1_REGIONS_ARCHIVE_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegionsArchiveCreateActualAvailabilityErrorComponentAttr
] = {
    "actual_availability",
}


def check_api_v1_regions_archive_create_actual_availability_error_component_attr(
    value: str,
) -> ApiV1RegionsArchiveCreateActualAvailabilityErrorComponentAttr:
    if value in API_V1_REGIONS_ARCHIVE_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_ARCHIVE_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
