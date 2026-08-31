from typing import Literal

ApiV1EndpointsPartialUpdateScopeErrorComponentAttr = Literal["scope"]

API_V1_ENDPOINTS_PARTIAL_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsPartialUpdateScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_endpoints_partial_update_scope_error_component_attr(
    value: str,
) -> ApiV1EndpointsPartialUpdateScopeErrorComponentAttr:
    if value in API_V1_ENDPOINTS_PARTIAL_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_PARTIAL_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
