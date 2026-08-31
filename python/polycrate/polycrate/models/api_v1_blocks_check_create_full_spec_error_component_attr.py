from typing import Literal

ApiV1BlocksCheckCreateFullSpecErrorComponentAttr = Literal["full_spec"]

API_V1_BLOCKS_CHECK_CREATE_FULL_SPEC_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksCheckCreateFullSpecErrorComponentAttr
] = {
    "full_spec",
}


def check_api_v1_blocks_check_create_full_spec_error_component_attr(
    value: str,
) -> ApiV1BlocksCheckCreateFullSpecErrorComponentAttr:
    if value in API_V1_BLOCKS_CHECK_CREATE_FULL_SPEC_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CHECK_CREATE_FULL_SPEC_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
