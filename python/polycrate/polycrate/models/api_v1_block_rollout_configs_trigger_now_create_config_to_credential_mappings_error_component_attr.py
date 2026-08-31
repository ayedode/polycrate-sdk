from typing import Literal

ApiV1BlockRolloutConfigsTriggerNowCreateConfigToCredentialMappingsErrorComponentAttr = Literal[
    "config_to_credential_mappings"
]

API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_CONFIG_TO_CREDENTIAL_MAPPINGS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsTriggerNowCreateConfigToCredentialMappingsErrorComponentAttr
] = {
    "config_to_credential_mappings",
}


def check_api_v1_block_rollout_configs_trigger_now_create_config_to_credential_mappings_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsTriggerNowCreateConfigToCredentialMappingsErrorComponentAttr:
    if (
        value
        in API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_CONFIG_TO_CREDENTIAL_MAPPINGS_ERROR_COMPONENT_ATTR_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_CONFIG_TO_CREDENTIAL_MAPPINGS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
