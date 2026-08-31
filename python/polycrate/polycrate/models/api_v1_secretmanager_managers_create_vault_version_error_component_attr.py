from typing import Literal

ApiV1SecretmanagerManagersCreateVaultVersionErrorComponentAttr = Literal["vault_version"]

API_V1_SECRETMANAGER_MANAGERS_CREATE_VAULT_VERSION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersCreateVaultVersionErrorComponentAttr
] = {
    "vault_version",
}


def check_api_v1_secretmanager_managers_create_vault_version_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersCreateVaultVersionErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_CREATE_VAULT_VERSION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_CREATE_VAULT_VERSION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
