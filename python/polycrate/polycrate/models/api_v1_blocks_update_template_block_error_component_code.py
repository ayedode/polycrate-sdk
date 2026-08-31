from typing import Literal

ApiV1BlocksUpdateTemplateBlockErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_BLOCKS_UPDATE_TEMPLATE_BLOCK_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksUpdateTemplateBlockErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_blocks_update_template_block_error_component_code(
    value: str,
) -> ApiV1BlocksUpdateTemplateBlockErrorComponentCode:
    if value in API_V1_BLOCKS_UPDATE_TEMPLATE_BLOCK_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_UPDATE_TEMPLATE_BLOCK_ERROR_COMPONENT_CODE_VALUES!r}"
    )
