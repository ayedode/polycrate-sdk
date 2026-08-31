from typing import Literal

ApiV1EndpointsListLoadbalancerInstanceErrorComponentCode = Literal["invalid", "null_characters_not_allowed"]

API_V1_ENDPOINTS_LIST_LOADBALANCER_INSTANCE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsListLoadbalancerInstanceErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
}


def check_api_v1_endpoints_list_loadbalancer_instance_error_component_code(
    value: str,
) -> ApiV1EndpointsListLoadbalancerInstanceErrorComponentCode:
    if value in API_V1_ENDPOINTS_LIST_LOADBALANCER_INSTANCE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_LIST_LOADBALANCER_INSTANCE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
