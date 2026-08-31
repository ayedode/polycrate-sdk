from typing import Literal

ApiV1BlockRolloutConfigsTriggerNowCreateNotifyOnWaveBlockedErrorComponentAttr = Literal["notify_on_wave_blocked"]

API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_NOTIFY_ON_WAVE_BLOCKED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsTriggerNowCreateNotifyOnWaveBlockedErrorComponentAttr
] = {
    "notify_on_wave_blocked",
}


def check_api_v1_block_rollout_configs_trigger_now_create_notify_on_wave_blocked_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsTriggerNowCreateNotifyOnWaveBlockedErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_NOTIFY_ON_WAVE_BLOCKED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_NOTIFY_ON_WAVE_BLOCKED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
