from typing import Literal

ApiV1BlocksPartialUpdateFromBlockErrorComponentAttr = Literal["from_block"]

API_V1_BLOCKS_PARTIAL_UPDATE_FROM_BLOCK_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksPartialUpdateFromBlockErrorComponentAttr
] = {
    "from_block",
}


def check_api_v1_blocks_partial_update_from_block_error_component_attr(
    value: str,
) -> ApiV1BlocksPartialUpdateFromBlockErrorComponentAttr:
    if value in API_V1_BLOCKS_PARTIAL_UPDATE_FROM_BLOCK_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_PARTIAL_UPDATE_FROM_BLOCK_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
