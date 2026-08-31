from typing import Literal

ApiV1EndpointsPartialUpdatePopEndpointErrorComponentAttr = Literal["pop_endpoint"]

API_V1_ENDPOINTS_PARTIAL_UPDATE_POP_ENDPOINT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsPartialUpdatePopEndpointErrorComponentAttr
] = {
    "pop_endpoint",
}


def check_api_v1_endpoints_partial_update_pop_endpoint_error_component_attr(
    value: str,
) -> ApiV1EndpointsPartialUpdatePopEndpointErrorComponentAttr:
    if value in API_V1_ENDPOINTS_PARTIAL_UPDATE_POP_ENDPOINT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_PARTIAL_UPDATE_POP_ENDPOINT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
