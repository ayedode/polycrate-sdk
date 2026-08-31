from typing import Literal

ApiV1BlocksListTemplateBlockErrorComponentAttr = Literal["template_block"]

API_V1_BLOCKS_LIST_TEMPLATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksListTemplateBlockErrorComponentAttr] = {
    "template_block",
}


def check_api_v1_blocks_list_template_block_error_component_attr(
    value: str,
) -> ApiV1BlocksListTemplateBlockErrorComponentAttr:
    if value in API_V1_BLOCKS_LIST_TEMPLATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_LIST_TEMPLATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
