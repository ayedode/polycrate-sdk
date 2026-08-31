from typing import Literal

ApiV1EndpointsUpdateLoadbalancerInstanceErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_ENDPOINTS_UPDATE_LOADBALANCER_INSTANCE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsUpdateLoadbalancerInstanceErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_endpoints_update_loadbalancer_instance_error_component_code(
    value: str,
) -> ApiV1EndpointsUpdateLoadbalancerInstanceErrorComponentCode:
    if value in API_V1_ENDPOINTS_UPDATE_LOADBALANCER_INSTANCE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_UPDATE_LOADBALANCER_INSTANCE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
