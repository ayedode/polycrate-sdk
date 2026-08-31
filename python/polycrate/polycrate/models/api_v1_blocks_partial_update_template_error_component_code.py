from typing import Literal

ApiV1BlocksPartialUpdateTemplateErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCKS_PARTIAL_UPDATE_TEMPLATE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksPartialUpdateTemplateErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_blocks_partial_update_template_error_component_code(
    value: str,
) -> ApiV1BlocksPartialUpdateTemplateErrorComponentCode:
    if value in API_V1_BLOCKS_PARTIAL_UPDATE_TEMPLATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_PARTIAL_UPDATE_TEMPLATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
