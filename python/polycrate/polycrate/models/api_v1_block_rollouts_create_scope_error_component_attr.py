from typing import Literal

ApiV1BlockRolloutsCreateScopeErrorComponentAttr = Literal["scope"]

API_V1_BLOCK_ROLLOUTS_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlockRolloutsCreateScopeErrorComponentAttr] = {
    "scope",
}


def check_api_v1_block_rollouts_create_scope_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsCreateScopeErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
