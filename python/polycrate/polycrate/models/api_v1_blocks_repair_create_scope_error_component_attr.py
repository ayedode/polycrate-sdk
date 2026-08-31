from typing import Literal

ApiV1BlocksRepairCreateScopeErrorComponentAttr = Literal["scope"]

API_V1_BLOCKS_REPAIR_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksRepairCreateScopeErrorComponentAttr] = {
    "scope",
}


def check_api_v1_blocks_repair_create_scope_error_component_attr(
    value: str,
) -> ApiV1BlocksRepairCreateScopeErrorComponentAttr:
    if value in API_V1_BLOCKS_REPAIR_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_REPAIR_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
