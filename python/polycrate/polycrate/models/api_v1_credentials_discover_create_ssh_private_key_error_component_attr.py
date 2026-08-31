from typing import Literal

ApiV1CredentialsDiscoverCreateSshPrivateKeyErrorComponentAttr = Literal["ssh_private_key"]

API_V1_CREDENTIALS_DISCOVER_CREATE_SSH_PRIVATE_KEY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CredentialsDiscoverCreateSshPrivateKeyErrorComponentAttr
] = {
    "ssh_private_key",
}


def check_api_v1_credentials_discover_create_ssh_private_key_error_component_attr(
    value: str,
) -> ApiV1CredentialsDiscoverCreateSshPrivateKeyErrorComponentAttr:
    if value in API_V1_CREDENTIALS_DISCOVER_CREATE_SSH_PRIVATE_KEY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_DISCOVER_CREATE_SSH_PRIVATE_KEY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
