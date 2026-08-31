from typing import Literal

ApiV1BlocksPartialUpdateVersionErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "required", "surrogate_characters_not_allowed"
]

API_V1_BLOCKS_PARTIAL_UPDATE_VERSION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksPartialUpdateVersionErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_blocks_partial_update_version_error_component_code(
    value: str,
) -> ApiV1BlocksPartialUpdateVersionErrorComponentCode:
    if value in API_V1_BLOCKS_PARTIAL_UPDATE_VERSION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_PARTIAL_UPDATE_VERSION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
