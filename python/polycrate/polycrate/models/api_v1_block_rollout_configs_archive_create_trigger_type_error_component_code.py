from typing import Literal

ApiV1BlockRolloutConfigsArchiveCreateTriggerTypeErrorComponentCode = Literal["invalid_choice"]

API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_TRIGGER_TYPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutConfigsArchiveCreateTriggerTypeErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_block_rollout_configs_archive_create_trigger_type_error_component_code(
    value: str,
) -> ApiV1BlockRolloutConfigsArchiveCreateTriggerTypeErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_TRIGGER_TYPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_TRIGGER_TYPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
