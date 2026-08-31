from typing import Literal

ApiV1BlocksCheckCreateTemplateErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCKS_CHECK_CREATE_TEMPLATE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksCheckCreateTemplateErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_blocks_check_create_template_error_component_code(
    value: str,
) -> ApiV1BlocksCheckCreateTemplateErrorComponentCode:
    if value in API_V1_BLOCKS_CHECK_CREATE_TEMPLATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CHECK_CREATE_TEMPLATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
