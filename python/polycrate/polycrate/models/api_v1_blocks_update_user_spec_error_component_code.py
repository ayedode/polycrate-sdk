from typing import Literal

ApiV1BlocksUpdateUserSpecErrorComponentCode = Literal["invalid"]

API_V1_BLOCKS_UPDATE_USER_SPEC_ERROR_COMPONENT_CODE_VALUES: set[ApiV1BlocksUpdateUserSpecErrorComponentCode] = {
    "invalid",
}


def check_api_v1_blocks_update_user_spec_error_component_code(
    value: str,
) -> ApiV1BlocksUpdateUserSpecErrorComponentCode:
    if value in API_V1_BLOCKS_UPDATE_USER_SPEC_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_UPDATE_USER_SPEC_ERROR_COMPONENT_CODE_VALUES!r}"
    )
