from typing import Literal

ApiV1CredentialsUpdateSshPrivateKeyErrorComponentAttr = Literal["ssh_private_key"]

API_V1_CREDENTIALS_UPDATE_SSH_PRIVATE_KEY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CredentialsUpdateSshPrivateKeyErrorComponentAttr
] = {
    "ssh_private_key",
}


def check_api_v1_credentials_update_ssh_private_key_error_component_attr(
    value: str,
) -> ApiV1CredentialsUpdateSshPrivateKeyErrorComponentAttr:
    if value in API_V1_CREDENTIALS_UPDATE_SSH_PRIVATE_KEY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_UPDATE_SSH_PRIVATE_KEY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
