from typing import Literal

ApiV1BlocksDiscoverCreateScopeErrorComponentAttr = Literal["scope"]

API_V1_BLOCKS_DISCOVER_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksDiscoverCreateScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_blocks_discover_create_scope_error_component_attr(
    value: str,
) -> ApiV1BlocksDiscoverCreateScopeErrorComponentAttr:
    if value in API_V1_BLOCKS_DISCOVER_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_DISCOVER_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
