from typing import Literal

ApiV1CredentialsUpdateSshPublicKeyErrorComponentAttr = Literal["ssh_public_key"]

API_V1_CREDENTIALS_UPDATE_SSH_PUBLIC_KEY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CredentialsUpdateSshPublicKeyErrorComponentAttr
] = {
    "ssh_public_key",
}


def check_api_v1_credentials_update_ssh_public_key_error_component_attr(
    value: str,
) -> ApiV1CredentialsUpdateSshPublicKeyErrorComponentAttr:
    if value in API_V1_CREDENTIALS_UPDATE_SSH_PUBLIC_KEY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_UPDATE_SSH_PUBLIC_KEY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
