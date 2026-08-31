from typing import Literal

ApiV1BlocksCheckCreateNameErrorComponentAttr = Literal["name"]

API_V1_BLOCKS_CHECK_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksCheckCreateNameErrorComponentAttr] = {
    "name",
}


def check_api_v1_blocks_check_create_name_error_component_attr(
    value: str,
) -> ApiV1BlocksCheckCreateNameErrorComponentAttr:
    if value in API_V1_BLOCKS_CHECK_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CHECK_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
