from typing import Literal

ApiV1BlockRolloutConfigsCreateNotifyOnWaveBlockedErrorComponentAttr = Literal["notify_on_wave_blocked"]

API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_NOTIFY_ON_WAVE_BLOCKED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsCreateNotifyOnWaveBlockedErrorComponentAttr
] = {
    "notify_on_wave_blocked",
}


def check_api_v1_block_rollout_configs_create_notify_on_wave_blocked_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsCreateNotifyOnWaveBlockedErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_NOTIFY_ON_WAVE_BLOCKED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_NOTIFY_ON_WAVE_BLOCKED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
