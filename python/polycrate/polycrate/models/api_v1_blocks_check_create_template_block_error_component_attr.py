from typing import Literal

ApiV1BlocksCheckCreateTemplateBlockErrorComponentAttr = Literal["template_block"]

API_V1_BLOCKS_CHECK_CREATE_TEMPLATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksCheckCreateTemplateBlockErrorComponentAttr
] = {
    "template_block",
}


def check_api_v1_blocks_check_create_template_block_error_component_attr(
    value: str,
) -> ApiV1BlocksCheckCreateTemplateBlockErrorComponentAttr:
    if value in API_V1_BLOCKS_CHECK_CREATE_TEMPLATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CHECK_CREATE_TEMPLATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
