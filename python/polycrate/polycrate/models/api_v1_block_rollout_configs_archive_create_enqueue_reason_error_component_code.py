from typing import Literal

ApiV1BlockRolloutConfigsArchiveCreateEnqueueReasonErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_ENQUEUE_REASON_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutConfigsArchiveCreateEnqueueReasonErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_block_rollout_configs_archive_create_enqueue_reason_error_component_code(
    value: str,
) -> ApiV1BlockRolloutConfigsArchiveCreateEnqueueReasonErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_ENQUEUE_REASON_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_ENQUEUE_REASON_ERROR_COMPONENT_CODE_VALUES!r}"
    )
