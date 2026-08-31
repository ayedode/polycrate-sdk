from typing import Literal

ApiV1BlockRolloutConfigsTriggerNowCreatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsTriggerNowCreatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_block_rollout_configs_trigger_now_create_platform_service_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsTriggerNowCreatePlatformServiceErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
