from typing import Literal

ApiV1EndpointsPartialUpdateLoadbalancerInstanceErrorComponentAttr = Literal["loadbalancer_instance"]

API_V1_ENDPOINTS_PARTIAL_UPDATE_LOADBALANCER_INSTANCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsPartialUpdateLoadbalancerInstanceErrorComponentAttr
] = {
    "loadbalancer_instance",
}


def check_api_v1_endpoints_partial_update_loadbalancer_instance_error_component_attr(
    value: str,
) -> ApiV1EndpointsPartialUpdateLoadbalancerInstanceErrorComponentAttr:
    if value in API_V1_ENDPOINTS_PARTIAL_UPDATE_LOADBALANCER_INSTANCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_PARTIAL_UPDATE_LOADBALANCER_INSTANCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
