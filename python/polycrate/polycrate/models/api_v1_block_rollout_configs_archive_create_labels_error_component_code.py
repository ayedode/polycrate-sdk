from typing import Literal

ApiV1BlockRolloutConfigsArchiveCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutConfigsArchiveCreateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_block_rollout_configs_archive_create_labels_error_component_code(
    value: str,
) -> ApiV1BlockRolloutConfigsArchiveCreateLabelsErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
