from typing import Literal

ApiV1BlocksCreateScopeErrorComponentAttr = Literal["scope"]

API_V1_BLOCKS_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksCreateScopeErrorComponentAttr] = {
    "scope",
}


def check_api_v1_blocks_create_scope_error_component_attr(value: str) -> ApiV1BlocksCreateScopeErrorComponentAttr:
    if value in API_V1_BLOCKS_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
