from typing import Literal

ApiV1SecretmanagerManagersArchiveCreateVaultVersionErrorComponentAttr = Literal["vault_version"]

API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_VAULT_VERSION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersArchiveCreateVaultVersionErrorComponentAttr
] = {
    "vault_version",
}


def check_api_v1_secretmanager_managers_archive_create_vault_version_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersArchiveCreateVaultVersionErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_VAULT_VERSION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_VAULT_VERSION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
