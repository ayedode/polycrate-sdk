from typing import Literal

ApiV1BlockRolloutConfigsCreateConfigToCredentialMappingsErrorComponentAttr = Literal["config_to_credential_mappings"]

API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_CONFIG_TO_CREDENTIAL_MAPPINGS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsCreateConfigToCredentialMappingsErrorComponentAttr
] = {
    "config_to_credential_mappings",
}


def check_api_v1_block_rollout_configs_create_config_to_credential_mappings_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsCreateConfigToCredentialMappingsErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_CONFIG_TO_CREDENTIAL_MAPPINGS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_CONFIG_TO_CREDENTIAL_MAPPINGS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
