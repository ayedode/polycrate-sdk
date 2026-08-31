from typing import Literal

ApiV1EndpointsCreateScopeErrorComponentAttr = Literal["scope"]

API_V1_ENDPOINTS_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1EndpointsCreateScopeErrorComponentAttr] = {
    "scope",
}


def check_api_v1_endpoints_create_scope_error_component_attr(value: str) -> ApiV1EndpointsCreateScopeErrorComponentAttr:
    if value in API_V1_ENDPOINTS_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
