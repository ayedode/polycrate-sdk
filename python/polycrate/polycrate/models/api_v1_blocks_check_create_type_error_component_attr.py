from typing import Literal

ApiV1BlocksCheckCreateTypeErrorComponentAttr = Literal["type"]

API_V1_BLOCKS_CHECK_CREATE_TYPE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksCheckCreateTypeErrorComponentAttr] = {
    "type",
}


def check_api_v1_blocks_check_create_type_error_component_attr(
    value: str,
) -> ApiV1BlocksCheckCreateTypeErrorComponentAttr:
    if value in API_V1_BLOCKS_CHECK_CREATE_TYPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CHECK_CREATE_TYPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
