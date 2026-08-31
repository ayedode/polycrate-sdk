from typing import Literal

ApiV1BlocksUpdateLatestStableErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_BLOCKS_UPDATE_LATEST_STABLE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1BlocksUpdateLatestStableErrorComponentCode] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_blocks_update_latest_stable_error_component_code(
    value: str,
) -> ApiV1BlocksUpdateLatestStableErrorComponentCode:
    if value in API_V1_BLOCKS_UPDATE_LATEST_STABLE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_UPDATE_LATEST_STABLE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
