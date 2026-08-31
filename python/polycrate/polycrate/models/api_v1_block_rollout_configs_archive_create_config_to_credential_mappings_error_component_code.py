from typing import Literal

ApiV1BlockRolloutConfigsArchiveCreateConfigToCredentialMappingsErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_CONFIG_TO_CREDENTIAL_MAPPINGS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutConfigsArchiveCreateConfigToCredentialMappingsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_block_rollout_configs_archive_create_config_to_credential_mappings_error_component_code(
    value: str,
) -> ApiV1BlockRolloutConfigsArchiveCreateConfigToCredentialMappingsErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_CONFIG_TO_CREDENTIAL_MAPPINGS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_CONFIG_TO_CREDENTIAL_MAPPINGS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
