from typing import Literal

ApiV1BlockRolloutConfigsArchiveCreateLastStateErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_LAST_STATE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutConfigsArchiveCreateLastStateErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_block_rollout_configs_archive_create_last_state_error_component_code(
    value: str,
) -> ApiV1BlockRolloutConfigsArchiveCreateLastStateErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_LAST_STATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_LAST_STATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
