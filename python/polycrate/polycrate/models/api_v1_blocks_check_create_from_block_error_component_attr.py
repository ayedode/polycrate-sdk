from typing import Literal

ApiV1BlocksCheckCreateFromBlockErrorComponentAttr = Literal["from_block"]

API_V1_BLOCKS_CHECK_CREATE_FROM_BLOCK_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksCheckCreateFromBlockErrorComponentAttr
] = {
    "from_block",
}


def check_api_v1_blocks_check_create_from_block_error_component_attr(
    value: str,
) -> ApiV1BlocksCheckCreateFromBlockErrorComponentAttr:
    if value in API_V1_BLOCKS_CHECK_CREATE_FROM_BLOCK_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CHECK_CREATE_FROM_BLOCK_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
