from typing import Literal

ApiV1BlockRolloutConfigsCreateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsCreateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_block_rollout_configs_create_provider_id_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsCreateProviderIdErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
