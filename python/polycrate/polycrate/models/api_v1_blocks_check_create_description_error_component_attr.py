from typing import Literal

ApiV1BlocksCheckCreateDescriptionErrorComponentAttr = Literal["description"]

API_V1_BLOCKS_CHECK_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksCheckCreateDescriptionErrorComponentAttr
] = {
    "description",
}


def check_api_v1_blocks_check_create_description_error_component_attr(
    value: str,
) -> ApiV1BlocksCheckCreateDescriptionErrorComponentAttr:
    if value in API_V1_BLOCKS_CHECK_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CHECK_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
