from typing import Literal

ApiV1BlockRolloutConfigsArchiveCreateKindErrorComponentCode = Literal["invalid_choice", "null", "required"]

API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutConfigsArchiveCreateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
    "required",
}


def check_api_v1_block_rollout_configs_archive_create_kind_error_component_code(
    value: str,
) -> ApiV1BlockRolloutConfigsArchiveCreateKindErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
