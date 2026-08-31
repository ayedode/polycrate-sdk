from typing import Literal

ApiV1PopsArchiveCreateLatitudeErrorComponentAttr = Literal["latitude"]

API_V1_POPS_ARCHIVE_CREATE_LATITUDE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PopsArchiveCreateLatitudeErrorComponentAttr
] = {
    "latitude",
}


def check_api_v1_pops_archive_create_latitude_error_component_attr(
    value: str,
) -> ApiV1PopsArchiveCreateLatitudeErrorComponentAttr:
    if value in API_V1_POPS_ARCHIVE_CREATE_LATITUDE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_ARCHIVE_CREATE_LATITUDE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
