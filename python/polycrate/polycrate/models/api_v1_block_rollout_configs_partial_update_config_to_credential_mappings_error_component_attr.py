from typing import Literal

ApiV1BlockRolloutConfigsPartialUpdateConfigToCredentialMappingsErrorComponentAttr = Literal[
    "config_to_credential_mappings"
]

API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_CONFIG_TO_CREDENTIAL_MAPPINGS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsPartialUpdateConfigToCredentialMappingsErrorComponentAttr
] = {
    "config_to_credential_mappings",
}


def check_api_v1_block_rollout_configs_partial_update_config_to_credential_mappings_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsPartialUpdateConfigToCredentialMappingsErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_CONFIG_TO_CREDENTIAL_MAPPINGS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_CONFIG_TO_CREDENTIAL_MAPPINGS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
