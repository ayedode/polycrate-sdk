from typing import Literal

ApiV1CredentialsArchiveCreateSshPublicKeyErrorComponentAttr = Literal["ssh_public_key"]

API_V1_CREDENTIALS_ARCHIVE_CREATE_SSH_PUBLIC_KEY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CredentialsArchiveCreateSshPublicKeyErrorComponentAttr
] = {
    "ssh_public_key",
}


def check_api_v1_credentials_archive_create_ssh_public_key_error_component_attr(
    value: str,
) -> ApiV1CredentialsArchiveCreateSshPublicKeyErrorComponentAttr:
    if value in API_V1_CREDENTIALS_ARCHIVE_CREATE_SSH_PUBLIC_KEY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_ARCHIVE_CREATE_SSH_PUBLIC_KEY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
