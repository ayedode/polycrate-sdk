from typing import Literal

ApiV1SecretmanagerManagersCreateVaultVersionErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_SECRETMANAGER_MANAGERS_CREATE_VAULT_VERSION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1SecretmanagerManagersCreateVaultVersionErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_secretmanager_managers_create_vault_version_error_component_code(
    value: str,
) -> ApiV1SecretmanagerManagersCreateVaultVersionErrorComponentCode:
    if value in API_V1_SECRETMANAGER_MANAGERS_CREATE_VAULT_VERSION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_CREATE_VAULT_VERSION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
