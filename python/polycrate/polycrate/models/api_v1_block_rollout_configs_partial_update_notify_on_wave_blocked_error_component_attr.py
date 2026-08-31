from typing import Literal

ApiV1BlockRolloutConfigsPartialUpdateNotifyOnWaveBlockedErrorComponentAttr = Literal["notify_on_wave_blocked"]

API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_NOTIFY_ON_WAVE_BLOCKED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsPartialUpdateNotifyOnWaveBlockedErrorComponentAttr
] = {
    "notify_on_wave_blocked",
}


def check_api_v1_block_rollout_configs_partial_update_notify_on_wave_blocked_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsPartialUpdateNotifyOnWaveBlockedErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_NOTIFY_ON_WAVE_BLOCKED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_NOTIFY_ON_WAVE_BLOCKED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
