from typing import Literal

ApiV1BlockRolloutConfigsTriggerNowCreateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsTriggerNowCreateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_block_rollout_configs_trigger_now_create_provider_reference_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsTriggerNowCreateProviderReferenceErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
