from typing import Literal

ApiV1WorkspacesArchiveCreateEncryptedErrorComponentCode = Literal["invalid", "null"]

API_V1_WORKSPACES_ARCHIVE_CREATE_ENCRYPTED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesArchiveCreateEncryptedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_workspaces_archive_create_encrypted_error_component_code(
    value: str,
) -> ApiV1WorkspacesArchiveCreateEncryptedErrorComponentCode:
    if value in API_V1_WORKSPACES_ARCHIVE_CREATE_ENCRYPTED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_ARCHIVE_CREATE_ENCRYPTED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
