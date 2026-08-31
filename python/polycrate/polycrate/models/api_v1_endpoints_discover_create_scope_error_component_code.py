from typing import Literal

ApiV1EndpointsDiscoverCreateScopeErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_ENDPOINTS_DISCOVER_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsDiscoverCreateScopeErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_endpoints_discover_create_scope_error_component_code(
    value: str,
) -> ApiV1EndpointsDiscoverCreateScopeErrorComponentCode:
    if value in API_V1_ENDPOINTS_DISCOVER_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_DISCOVER_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
