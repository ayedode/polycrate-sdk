from typing import Literal

ApiV1SecretmanagerManagersArchiveCreateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1SecretmanagerManagersArchiveCreateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_secretmanager_managers_archive_create_provider_error_component_code(
    value: str,
) -> ApiV1SecretmanagerManagersArchiveCreateProviderErrorComponentCode:
    if value in API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
