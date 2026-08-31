from typing import Literal

ApiV1BlocksArchiveCreateTemplateBlockErrorComponentAttr = Literal["template_block"]

API_V1_BLOCKS_ARCHIVE_CREATE_TEMPLATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksArchiveCreateTemplateBlockErrorComponentAttr
] = {
    "template_block",
}


def check_api_v1_blocks_archive_create_template_block_error_component_attr(
    value: str,
) -> ApiV1BlocksArchiveCreateTemplateBlockErrorComponentAttr:
    if value in API_V1_BLOCKS_ARCHIVE_CREATE_TEMPLATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_ARCHIVE_CREATE_TEMPLATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
