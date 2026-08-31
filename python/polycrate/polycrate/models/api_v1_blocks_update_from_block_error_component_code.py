from typing import Literal

ApiV1BlocksUpdateFromBlockErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_BLOCKS_UPDATE_FROM_BLOCK_ERROR_COMPONENT_CODE_VALUES: set[ApiV1BlocksUpdateFromBlockErrorComponentCode] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_blocks_update_from_block_error_component_code(
    value: str,
) -> ApiV1BlocksUpdateFromBlockErrorComponentCode:
    if value in API_V1_BLOCKS_UPDATE_FROM_BLOCK_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_UPDATE_FROM_BLOCK_ERROR_COMPONENT_CODE_VALUES!r}"
    )
