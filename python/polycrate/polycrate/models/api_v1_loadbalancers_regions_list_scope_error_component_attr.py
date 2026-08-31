from typing import Literal

ApiV1LoadbalancersRegionsListScopeErrorComponentAttr = Literal["scope"]

API_V1_LOADBALANCERS_REGIONS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersRegionsListScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_loadbalancers_regions_list_scope_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersRegionsListScopeErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_REGIONS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
