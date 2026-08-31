from typing import Literal

ApiV1CredentialsReconcileCreateSshPublicKeyErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_CREDENTIALS_RECONCILE_CREATE_SSH_PUBLIC_KEY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CredentialsReconcileCreateSshPublicKeyErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_credentials_reconcile_create_ssh_public_key_error_component_code(
    value: str,
) -> ApiV1CredentialsReconcileCreateSshPublicKeyErrorComponentCode:
    if value in API_V1_CREDENTIALS_RECONCILE_CREATE_SSH_PUBLIC_KEY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_RECONCILE_CREATE_SSH_PUBLIC_KEY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
