from typing import Literal

ApiV1BlockRolloutConfigsTriggerNowCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsTriggerNowCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_block_rollout_configs_trigger_now_create_provider_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsTriggerNowCreateProviderErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
