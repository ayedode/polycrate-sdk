from typing import Literal

ApiV1EndpointsCreateLoadbalancerInstanceErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_ENDPOINTS_CREATE_LOADBALANCER_INSTANCE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsCreateLoadbalancerInstanceErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_endpoints_create_loadbalancer_instance_error_component_code(
    value: str,
) -> ApiV1EndpointsCreateLoadbalancerInstanceErrorComponentCode:
    if value in API_V1_ENDPOINTS_CREATE_LOADBALANCER_INSTANCE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_CREATE_LOADBALANCER_INSTANCE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
