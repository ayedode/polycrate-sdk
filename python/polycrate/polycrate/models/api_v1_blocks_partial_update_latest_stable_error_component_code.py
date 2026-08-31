from typing import Literal

ApiV1BlocksPartialUpdateLatestStableErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_BLOCKS_PARTIAL_UPDATE_LATEST_STABLE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksPartialUpdateLatestStableErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_blocks_partial_update_latest_stable_error_component_code(
    value: str,
) -> ApiV1BlocksPartialUpdateLatestStableErrorComponentCode:
    if value in API_V1_BLOCKS_PARTIAL_UPDATE_LATEST_STABLE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_PARTIAL_UPDATE_LATEST_STABLE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
