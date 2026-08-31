from typing import Literal

ApiV1BlockRolloutConfigsArchiveCreateNotifyOnWaveBlockedErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_NOTIFY_ON_WAVE_BLOCKED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutConfigsArchiveCreateNotifyOnWaveBlockedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_block_rollout_configs_archive_create_notify_on_wave_blocked_error_component_code(
    value: str,
) -> ApiV1BlockRolloutConfigsArchiveCreateNotifyOnWaveBlockedErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_NOTIFY_ON_WAVE_BLOCKED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_NOTIFY_ON_WAVE_BLOCKED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
