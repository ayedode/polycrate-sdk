from typing import Literal

ApiV1LoadbalancersRegionsUpdateActiveErrorComponentCode = Literal["invalid", "null"]

API_V1_LOADBALANCERS_REGIONS_UPDATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1LoadbalancersRegionsUpdateActiveErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_loadbalancers_regions_update_active_error_component_code(
    value: str,
) -> ApiV1LoadbalancersRegionsUpdateActiveErrorComponentCode:
    if value in API_V1_LOADBALANCERS_REGIONS_UPDATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_UPDATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
