from typing import Literal

ApiV1LoadbalancersRegionsCreateRegionConfigErrorComponentCode = Literal["invalid", "null"]

API_V1_LOADBALANCERS_REGIONS_CREATE_REGION_CONFIG_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1LoadbalancersRegionsCreateRegionConfigErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_loadbalancers_regions_create_region_config_error_component_code(
    value: str,
) -> ApiV1LoadbalancersRegionsCreateRegionConfigErrorComponentCode:
    if value in API_V1_LOADBALANCERS_REGIONS_CREATE_REGION_CONFIG_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_CREATE_REGION_CONFIG_ERROR_COMPONENT_CODE_VALUES!r}"
    )
