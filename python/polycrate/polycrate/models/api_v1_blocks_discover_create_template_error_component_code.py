from typing import Literal

ApiV1BlocksDiscoverCreateTemplateErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCKS_DISCOVER_CREATE_TEMPLATE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksDiscoverCreateTemplateErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_blocks_discover_create_template_error_component_code(
    value: str,
) -> ApiV1BlocksDiscoverCreateTemplateErrorComponentCode:
    if value in API_V1_BLOCKS_DISCOVER_CREATE_TEMPLATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_DISCOVER_CREATE_TEMPLATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
