from typing import Literal

ApiV1CredentialsPartialUpdateSshPublicKeyErrorComponentAttr = Literal["ssh_public_key"]

API_V1_CREDENTIALS_PARTIAL_UPDATE_SSH_PUBLIC_KEY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CredentialsPartialUpdateSshPublicKeyErrorComponentAttr
] = {
    "ssh_public_key",
}


def check_api_v1_credentials_partial_update_ssh_public_key_error_component_attr(
    value: str,
) -> ApiV1CredentialsPartialUpdateSshPublicKeyErrorComponentAttr:
    if value in API_V1_CREDENTIALS_PARTIAL_UPDATE_SSH_PUBLIC_KEY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_PARTIAL_UPDATE_SSH_PUBLIC_KEY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
