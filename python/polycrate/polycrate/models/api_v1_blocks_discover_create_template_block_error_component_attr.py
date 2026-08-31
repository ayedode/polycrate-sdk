from typing import Literal

ApiV1BlocksDiscoverCreateTemplateBlockErrorComponentAttr = Literal["template_block"]

API_V1_BLOCKS_DISCOVER_CREATE_TEMPLATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksDiscoverCreateTemplateBlockErrorComponentAttr
] = {
    "template_block",
}


def check_api_v1_blocks_discover_create_template_block_error_component_attr(
    value: str,
) -> ApiV1BlocksDiscoverCreateTemplateBlockErrorComponentAttr:
    if value in API_V1_BLOCKS_DISCOVER_CREATE_TEMPLATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_DISCOVER_CREATE_TEMPLATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
