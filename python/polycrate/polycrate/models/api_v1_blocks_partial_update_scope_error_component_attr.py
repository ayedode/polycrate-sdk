from typing import Literal

ApiV1BlocksPartialUpdateScopeErrorComponentAttr = Literal["scope"]

API_V1_BLOCKS_PARTIAL_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksPartialUpdateScopeErrorComponentAttr] = {
    "scope",
}


def check_api_v1_blocks_partial_update_scope_error_component_attr(
    value: str,
) -> ApiV1BlocksPartialUpdateScopeErrorComponentAttr:
    if value in API_V1_BLOCKS_PARTIAL_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_PARTIAL_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
