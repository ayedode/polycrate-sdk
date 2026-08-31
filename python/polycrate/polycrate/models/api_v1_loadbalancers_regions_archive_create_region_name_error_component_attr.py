from typing import Literal

ApiV1LoadbalancersRegionsArchiveCreateRegionNameErrorComponentAttr = Literal["region_name"]

API_V1_LOADBALANCERS_REGIONS_ARCHIVE_CREATE_REGION_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersRegionsArchiveCreateRegionNameErrorComponentAttr
] = {
    "region_name",
}


def check_api_v1_loadbalancers_regions_archive_create_region_name_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersRegionsArchiveCreateRegionNameErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_REGIONS_ARCHIVE_CREATE_REGION_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_ARCHIVE_CREATE_REGION_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
