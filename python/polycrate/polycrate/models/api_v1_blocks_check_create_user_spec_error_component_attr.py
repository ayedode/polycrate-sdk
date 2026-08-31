from typing import Literal

ApiV1BlocksCheckCreateUserSpecErrorComponentAttr = Literal["user_spec"]

API_V1_BLOCKS_CHECK_CREATE_USER_SPEC_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksCheckCreateUserSpecErrorComponentAttr
] = {
    "user_spec",
}


def check_api_v1_blocks_check_create_user_spec_error_component_attr(
    value: str,
) -> ApiV1BlocksCheckCreateUserSpecErrorComponentAttr:
    if value in API_V1_BLOCKS_CHECK_CREATE_USER_SPEC_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CHECK_CREATE_USER_SPEC_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
