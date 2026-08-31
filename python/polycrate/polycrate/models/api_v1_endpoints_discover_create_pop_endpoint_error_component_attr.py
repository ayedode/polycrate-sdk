from typing import Literal

ApiV1EndpointsDiscoverCreatePopEndpointErrorComponentAttr = Literal["pop_endpoint"]

API_V1_ENDPOINTS_DISCOVER_CREATE_POP_ENDPOINT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsDiscoverCreatePopEndpointErrorComponentAttr
] = {
    "pop_endpoint",
}


def check_api_v1_endpoints_discover_create_pop_endpoint_error_component_attr(
    value: str,
) -> ApiV1EndpointsDiscoverCreatePopEndpointErrorComponentAttr:
    if value in API_V1_ENDPOINTS_DISCOVER_CREATE_POP_ENDPOINT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_DISCOVER_CREATE_POP_ENDPOINT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
