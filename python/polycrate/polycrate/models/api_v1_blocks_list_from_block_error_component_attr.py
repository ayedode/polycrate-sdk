from typing import Literal

ApiV1BlocksListFromBlockErrorComponentAttr = Literal["from_block"]

API_V1_BLOCKS_LIST_FROM_BLOCK_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksListFromBlockErrorComponentAttr] = {
    "from_block",
}


def check_api_v1_blocks_list_from_block_error_component_attr(value: str) -> ApiV1BlocksListFromBlockErrorComponentAttr:
    if value in API_V1_BLOCKS_LIST_FROM_BLOCK_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_LIST_FROM_BLOCK_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
