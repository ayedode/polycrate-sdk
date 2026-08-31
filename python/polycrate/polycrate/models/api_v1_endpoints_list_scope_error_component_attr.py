from typing import Literal

ApiV1EndpointsListScopeErrorComponentAttr = Literal["scope"]

API_V1_ENDPOINTS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1EndpointsListScopeErrorComponentAttr] = {
    "scope",
}


def check_api_v1_endpoints_list_scope_error_component_attr(value: str) -> ApiV1EndpointsListScopeErrorComponentAttr:
    if value in API_V1_ENDPOINTS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
