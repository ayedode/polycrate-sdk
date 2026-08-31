from typing import Literal

ApiV1BlocksPartialUpdateUserSpecErrorComponentAttr = Literal["user_spec"]

API_V1_BLOCKS_PARTIAL_UPDATE_USER_SPEC_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksPartialUpdateUserSpecErrorComponentAttr
] = {
    "user_spec",
}


def check_api_v1_blocks_partial_update_user_spec_error_component_attr(
    value: str,
) -> ApiV1BlocksPartialUpdateUserSpecErrorComponentAttr:
    if value in API_V1_BLOCKS_PARTIAL_UPDATE_USER_SPEC_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_PARTIAL_UPDATE_USER_SPEC_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
