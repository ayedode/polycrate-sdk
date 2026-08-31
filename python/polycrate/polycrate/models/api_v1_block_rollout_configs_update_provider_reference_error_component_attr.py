from typing import Literal

ApiV1BlockRolloutConfigsUpdateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsUpdateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_block_rollout_configs_update_provider_reference_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsUpdateProviderReferenceErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
