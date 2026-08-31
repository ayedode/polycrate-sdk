from typing import Literal

ApiV1BlocksPartialUpdateUserSpecErrorComponentCode = Literal["invalid"]

API_V1_BLOCKS_PARTIAL_UPDATE_USER_SPEC_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksPartialUpdateUserSpecErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_blocks_partial_update_user_spec_error_component_code(
    value: str,
) -> ApiV1BlocksPartialUpdateUserSpecErrorComponentCode:
    if value in API_V1_BLOCKS_PARTIAL_UPDATE_USER_SPEC_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_PARTIAL_UPDATE_USER_SPEC_ERROR_COMPONENT_CODE_VALUES!r}"
    )
