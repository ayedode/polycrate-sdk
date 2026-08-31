from typing import Literal

ApiV1WorkspacesArchiveCreateEncryptedErrorComponentAttr = Literal["encrypted"]

API_V1_WORKSPACES_ARCHIVE_CREATE_ENCRYPTED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesArchiveCreateEncryptedErrorComponentAttr
] = {
    "encrypted",
}


def check_api_v1_workspaces_archive_create_encrypted_error_component_attr(
    value: str,
) -> ApiV1WorkspacesArchiveCreateEncryptedErrorComponentAttr:
    if value in API_V1_WORKSPACES_ARCHIVE_CREATE_ENCRYPTED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_ARCHIVE_CREATE_ENCRYPTED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
