from typing import Literal

ApiV1LoadbalancersRegionsPartialUpdateRegionConfigErrorComponentCode = Literal["invalid", "null"]

API_V1_LOADBALANCERS_REGIONS_PARTIAL_UPDATE_REGION_CONFIG_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1LoadbalancersRegionsPartialUpdateRegionConfigErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_loadbalancers_regions_partial_update_region_config_error_component_code(
    value: str,
) -> ApiV1LoadbalancersRegionsPartialUpdateRegionConfigErrorComponentCode:
    if value in API_V1_LOADBALANCERS_REGIONS_PARTIAL_UPDATE_REGION_CONFIG_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_PARTIAL_UPDATE_REGION_CONFIG_ERROR_COMPONENT_CODE_VALUES!r}"
    )
