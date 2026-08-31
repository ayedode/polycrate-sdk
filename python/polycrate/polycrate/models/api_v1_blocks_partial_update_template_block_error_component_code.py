from typing import Literal

ApiV1BlocksPartialUpdateTemplateBlockErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_BLOCKS_PARTIAL_UPDATE_TEMPLATE_BLOCK_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksPartialUpdateTemplateBlockErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_blocks_partial_update_template_block_error_component_code(
    value: str,
) -> ApiV1BlocksPartialUpdateTemplateBlockErrorComponentCode:
    if value in API_V1_BLOCKS_PARTIAL_UPDATE_TEMPLATE_BLOCK_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_PARTIAL_UPDATE_TEMPLATE_BLOCK_ERROR_COMPONENT_CODE_VALUES!r}"
    )
