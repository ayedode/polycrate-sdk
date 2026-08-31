from typing import Literal

ApiV1BlockRolloutConfigsUpdateConfigToCredentialMappingsErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_CONFIG_TO_CREDENTIAL_MAPPINGS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutConfigsUpdateConfigToCredentialMappingsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_block_rollout_configs_update_config_to_credential_mappings_error_component_code(
    value: str,
) -> ApiV1BlockRolloutConfigsUpdateConfigToCredentialMappingsErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_CONFIG_TO_CREDENTIAL_MAPPINGS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_CONFIG_TO_CREDENTIAL_MAPPINGS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
