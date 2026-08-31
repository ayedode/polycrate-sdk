from typing import Literal

ApiV1SecretmanagerManagersUpdateVaultVersionErrorComponentAttr = Literal["vault_version"]

API_V1_SECRETMANAGER_MANAGERS_UPDATE_VAULT_VERSION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersUpdateVaultVersionErrorComponentAttr
] = {
    "vault_version",
}


def check_api_v1_secretmanager_managers_update_vault_version_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersUpdateVaultVersionErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_UPDATE_VAULT_VERSION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_UPDATE_VAULT_VERSION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
