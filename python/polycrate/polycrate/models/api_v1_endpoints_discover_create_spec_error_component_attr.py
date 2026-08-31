from typing import Literal

ApiV1EndpointsDiscoverCreateSpecErrorComponentAttr = Literal["spec"]

API_V1_ENDPOINTS_DISCOVER_CREATE_SPEC_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsDiscoverCreateSpecErrorComponentAttr
] = {
    "spec",
}


def check_api_v1_endpoints_discover_create_spec_error_component_attr(
    value: str,
) -> ApiV1EndpointsDiscoverCreateSpecErrorComponentAttr:
    if value in API_V1_ENDPOINTS_DISCOVER_CREATE_SPEC_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_DISCOVER_CREATE_SPEC_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
