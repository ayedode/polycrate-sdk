from typing import Literal

ApiV1EndpointsUpdateScopeErrorComponentAttr = Literal["scope"]

API_V1_ENDPOINTS_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1EndpointsUpdateScopeErrorComponentAttr] = {
    "scope",
}


def check_api_v1_endpoints_update_scope_error_component_attr(value: str) -> ApiV1EndpointsUpdateScopeErrorComponentAttr:
    if value in API_V1_ENDPOINTS_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
