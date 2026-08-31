from typing import Literal

ApiV1EndpointsDiscoverCreateLoadbalancerInstanceErrorComponentAttr = Literal["loadbalancer_instance"]

API_V1_ENDPOINTS_DISCOVER_CREATE_LOADBALANCER_INSTANCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsDiscoverCreateLoadbalancerInstanceErrorComponentAttr
] = {
    "loadbalancer_instance",
}


def check_api_v1_endpoints_discover_create_loadbalancer_instance_error_component_attr(
    value: str,
) -> ApiV1EndpointsDiscoverCreateLoadbalancerInstanceErrorComponentAttr:
    if value in API_V1_ENDPOINTS_DISCOVER_CREATE_LOADBALANCER_INSTANCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_DISCOVER_CREATE_LOADBALANCER_INSTANCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
