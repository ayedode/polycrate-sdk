from typing import Literal

ApiV1CredentialsCreateSshPrivateKeyErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_CREDENTIALS_CREATE_SSH_PRIVATE_KEY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CredentialsCreateSshPrivateKeyErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_credentials_create_ssh_private_key_error_component_code(
    value: str,
) -> ApiV1CredentialsCreateSshPrivateKeyErrorComponentCode:
    if value in API_V1_CREDENTIALS_CREATE_SSH_PRIVATE_KEY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_CREATE_SSH_PRIVATE_KEY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
