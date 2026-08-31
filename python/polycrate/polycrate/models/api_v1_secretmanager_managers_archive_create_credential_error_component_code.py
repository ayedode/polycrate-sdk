from typing import Literal

ApiV1SecretmanagerManagersArchiveCreateCredentialErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_CREDENTIAL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1SecretmanagerManagersArchiveCreateCredentialErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_secretmanager_managers_archive_create_credential_error_component_code(
    value: str,
) -> ApiV1SecretmanagerManagersArchiveCreateCredentialErrorComponentCode:
    if value in API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_CREDENTIAL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_CREDENTIAL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
