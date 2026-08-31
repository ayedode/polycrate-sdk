from typing import Literal

ApiV1LoadbalancersRegionsUpdateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_LOADBALANCERS_REGIONS_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1LoadbalancersRegionsUpdateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_loadbalancers_regions_update_kind_error_component_code(
    value: str,
) -> ApiV1LoadbalancersRegionsUpdateKindErrorComponentCode:
    if value in API_V1_LOADBALANCERS_REGIONS_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
