from typing import Literal

ApiV1BlocksCreateTemplateBlockErrorComponentAttr = Literal["template_block"]

API_V1_BLOCKS_CREATE_TEMPLATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksCreateTemplateBlockErrorComponentAttr
] = {
    "template_block",
}


def check_api_v1_blocks_create_template_block_error_component_attr(
    value: str,
) -> ApiV1BlocksCreateTemplateBlockErrorComponentAttr:
    if value in API_V1_BLOCKS_CREATE_TEMPLATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CREATE_TEMPLATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
