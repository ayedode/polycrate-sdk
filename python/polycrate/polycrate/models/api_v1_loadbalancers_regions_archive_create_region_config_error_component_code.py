from typing import Literal

ApiV1LoadbalancersRegionsArchiveCreateRegionConfigErrorComponentCode = Literal["invalid", "null"]

API_V1_LOADBALANCERS_REGIONS_ARCHIVE_CREATE_REGION_CONFIG_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1LoadbalancersRegionsArchiveCreateRegionConfigErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_loadbalancers_regions_archive_create_region_config_error_component_code(
    value: str,
) -> ApiV1LoadbalancersRegionsArchiveCreateRegionConfigErrorComponentCode:
    if value in API_V1_LOADBALANCERS_REGIONS_ARCHIVE_CREATE_REGION_CONFIG_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_ARCHIVE_CREATE_REGION_CONFIG_ERROR_COMPONENT_CODE_VALUES!r}"
    )
