from typing import Literal

ApiV1EndpointsArchiveCreateRegionErrorComponentAttr = Literal["region"]

API_V1_ENDPOINTS_ARCHIVE_CREATE_REGION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsArchiveCreateRegionErrorComponentAttr
] = {
    "region",
}


def check_api_v1_endpoints_archive_create_region_error_component_attr(
    value: str,
) -> ApiV1EndpointsArchiveCreateRegionErrorComponentAttr:
    if value in API_V1_ENDPOINTS_ARCHIVE_CREATE_REGION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_ARCHIVE_CREATE_REGION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
