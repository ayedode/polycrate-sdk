from typing import Literal

ApiV1BlocksCheckCreateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_BLOCKS_CHECK_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksCheckCreateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_blocks_check_create_display_name_error_component_attr(
    value: str,
) -> ApiV1BlocksCheckCreateDisplayNameErrorComponentAttr:
    if value in API_V1_BLOCKS_CHECK_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CHECK_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
