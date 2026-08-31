from typing import Literal

ApiV1SecretmanagerManagersArchiveCreateCredentialErrorComponentAttr = Literal["credential"]

API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersArchiveCreateCredentialErrorComponentAttr
] = {
    "credential",
}


def check_api_v1_secretmanager_managers_archive_create_credential_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersArchiveCreateCredentialErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
