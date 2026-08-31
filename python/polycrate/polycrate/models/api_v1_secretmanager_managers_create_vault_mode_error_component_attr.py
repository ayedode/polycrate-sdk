from typing import Literal

ApiV1SecretmanagerManagersCreateVaultModeErrorComponentAttr = Literal["vault_mode"]

API_V1_SECRETMANAGER_MANAGERS_CREATE_VAULT_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersCreateVaultModeErrorComponentAttr
] = {
    "vault_mode",
}


def check_api_v1_secretmanager_managers_create_vault_mode_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersCreateVaultModeErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_CREATE_VAULT_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_CREATE_VAULT_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
