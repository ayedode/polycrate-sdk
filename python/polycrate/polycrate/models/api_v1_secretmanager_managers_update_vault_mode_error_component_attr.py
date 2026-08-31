from typing import Literal

ApiV1SecretmanagerManagersUpdateVaultModeErrorComponentAttr = Literal["vault_mode"]

API_V1_SECRETMANAGER_MANAGERS_UPDATE_VAULT_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersUpdateVaultModeErrorComponentAttr
] = {
    "vault_mode",
}


def check_api_v1_secretmanager_managers_update_vault_mode_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersUpdateVaultModeErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_UPDATE_VAULT_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_UPDATE_VAULT_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
