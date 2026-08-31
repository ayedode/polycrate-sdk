from typing import Literal

ApiV1BlocksUpdateScopeErrorComponentAttr = Literal["scope"]

API_V1_BLOCKS_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksUpdateScopeErrorComponentAttr] = {
    "scope",
}


def check_api_v1_blocks_update_scope_error_component_attr(value: str) -> ApiV1BlocksUpdateScopeErrorComponentAttr:
    if value in API_V1_BLOCKS_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
