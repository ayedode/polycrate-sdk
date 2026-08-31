from typing import Literal

ApiV1SecretmanagerManagersArchiveCreateIsSealedErrorComponentCode = Literal["invalid", "null"]

API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_IS_SEALED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1SecretmanagerManagersArchiveCreateIsSealedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_secretmanager_managers_archive_create_is_sealed_error_component_code(
    value: str,
) -> ApiV1SecretmanagerManagersArchiveCreateIsSealedErrorComponentCode:
    if value in API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_IS_SEALED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_IS_SEALED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
