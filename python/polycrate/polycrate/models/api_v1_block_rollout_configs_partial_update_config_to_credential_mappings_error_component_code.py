from typing import Literal

ApiV1BlockRolloutConfigsPartialUpdateConfigToCredentialMappingsErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_CONFIG_TO_CREDENTIAL_MAPPINGS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutConfigsPartialUpdateConfigToCredentialMappingsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_block_rollout_configs_partial_update_config_to_credential_mappings_error_component_code(
    value: str,
) -> ApiV1BlockRolloutConfigsPartialUpdateConfigToCredentialMappingsErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_CONFIG_TO_CREDENTIAL_MAPPINGS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_CONFIG_TO_CREDENTIAL_MAPPINGS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
