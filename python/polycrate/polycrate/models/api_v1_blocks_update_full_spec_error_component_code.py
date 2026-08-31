from typing import Literal

ApiV1BlocksUpdateFullSpecErrorComponentCode = Literal["invalid"]

API_V1_BLOCKS_UPDATE_FULL_SPEC_ERROR_COMPONENT_CODE_VALUES: set[ApiV1BlocksUpdateFullSpecErrorComponentCode] = {
    "invalid",
}


def check_api_v1_blocks_update_full_spec_error_component_code(
    value: str,
) -> ApiV1BlocksUpdateFullSpecErrorComponentCode:
    if value in API_V1_BLOCKS_UPDATE_FULL_SPEC_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_UPDATE_FULL_SPEC_ERROR_COMPONENT_CODE_VALUES!r}"
    )
