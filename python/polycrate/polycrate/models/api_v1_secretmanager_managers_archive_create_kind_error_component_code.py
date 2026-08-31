from typing import Literal

ApiV1SecretmanagerManagersArchiveCreateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1SecretmanagerManagersArchiveCreateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_secretmanager_managers_archive_create_kind_error_component_code(
    value: str,
) -> ApiV1SecretmanagerManagersArchiveCreateKindErrorComponentCode:
    if value in API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
