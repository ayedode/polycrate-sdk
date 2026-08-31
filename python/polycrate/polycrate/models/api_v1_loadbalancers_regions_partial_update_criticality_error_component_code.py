from typing import Literal

ApiV1LoadbalancersRegionsPartialUpdateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_LOADBALANCERS_REGIONS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1LoadbalancersRegionsPartialUpdateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_loadbalancers_regions_partial_update_criticality_error_component_code(
    value: str,
) -> ApiV1LoadbalancersRegionsPartialUpdateCriticalityErrorComponentCode:
    if value in API_V1_LOADBALANCERS_REGIONS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
