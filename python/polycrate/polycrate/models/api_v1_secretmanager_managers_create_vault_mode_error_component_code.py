from typing import Literal

ApiV1SecretmanagerManagersCreateVaultModeErrorComponentCode = Literal["invalid_choice"]

API_V1_SECRETMANAGER_MANAGERS_CREATE_VAULT_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1SecretmanagerManagersCreateVaultModeErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_secretmanager_managers_create_vault_mode_error_component_code(
    value: str,
) -> ApiV1SecretmanagerManagersCreateVaultModeErrorComponentCode:
    if value in API_V1_SECRETMANAGER_MANAGERS_CREATE_VAULT_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_CREATE_VAULT_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
