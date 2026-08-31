from typing import Literal

ApiV1CredentialsCreateSshPublicKeyErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_CREDENTIALS_CREATE_SSH_PUBLIC_KEY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CredentialsCreateSshPublicKeyErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_credentials_create_ssh_public_key_error_component_code(
    value: str,
) -> ApiV1CredentialsCreateSshPublicKeyErrorComponentCode:
    if value in API_V1_CREDENTIALS_CREATE_SSH_PUBLIC_KEY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_CREATE_SSH_PUBLIC_KEY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
