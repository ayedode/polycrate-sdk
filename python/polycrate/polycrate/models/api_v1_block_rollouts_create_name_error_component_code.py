from typing import Literal

ApiV1BlockRolloutsCreateNameErrorComponentCode = Literal[
    "invalid", "max_length", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_BLOCK_ROLLOUTS_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES: set[ApiV1BlockRolloutsCreateNameErrorComponentCode] = {
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_block_rollouts_create_name_error_component_code(
    value: str,
) -> ApiV1BlockRolloutsCreateNameErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUTS_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
