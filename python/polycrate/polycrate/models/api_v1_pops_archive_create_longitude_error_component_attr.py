from typing import Literal

ApiV1PopsArchiveCreateLongitudeErrorComponentAttr = Literal["longitude"]

API_V1_POPS_ARCHIVE_CREATE_LONGITUDE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PopsArchiveCreateLongitudeErrorComponentAttr
] = {
    "longitude",
}


def check_api_v1_pops_archive_create_longitude_error_component_attr(
    value: str,
) -> ApiV1PopsArchiveCreateLongitudeErrorComponentAttr:
    if value in API_V1_POPS_ARCHIVE_CREATE_LONGITUDE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_ARCHIVE_CREATE_LONGITUDE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
