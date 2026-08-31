from typing import Literal

ApiV1CredentialsDiscoverCreateSshPublicKeyErrorComponentAttr = Literal["ssh_public_key"]

API_V1_CREDENTIALS_DISCOVER_CREATE_SSH_PUBLIC_KEY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CredentialsDiscoverCreateSshPublicKeyErrorComponentAttr
] = {
    "ssh_public_key",
}


def check_api_v1_credentials_discover_create_ssh_public_key_error_component_attr(
    value: str,
) -> ApiV1CredentialsDiscoverCreateSshPublicKeyErrorComponentAttr:
    if value in API_V1_CREDENTIALS_DISCOVER_CREATE_SSH_PUBLIC_KEY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_DISCOVER_CREATE_SSH_PUBLIC_KEY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
