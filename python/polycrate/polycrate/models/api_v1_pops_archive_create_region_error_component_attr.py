from typing import Literal

ApiV1PopsArchiveCreateRegionErrorComponentAttr = Literal["region"]

API_V1_POPS_ARCHIVE_CREATE_REGION_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PopsArchiveCreateRegionErrorComponentAttr] = {
    "region",
}


def check_api_v1_pops_archive_create_region_error_component_attr(
    value: str,
) -> ApiV1PopsArchiveCreateRegionErrorComponentAttr:
    if value in API_V1_POPS_ARCHIVE_CREATE_REGION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_ARCHIVE_CREATE_REGION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
