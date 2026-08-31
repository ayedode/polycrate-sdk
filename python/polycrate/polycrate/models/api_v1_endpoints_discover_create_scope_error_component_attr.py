from typing import Literal

ApiV1EndpointsDiscoverCreateScopeErrorComponentAttr = Literal["scope"]

API_V1_ENDPOINTS_DISCOVER_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsDiscoverCreateScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_endpoints_discover_create_scope_error_component_attr(
    value: str,
) -> ApiV1EndpointsDiscoverCreateScopeErrorComponentAttr:
    if value in API_V1_ENDPOINTS_DISCOVER_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_DISCOVER_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
