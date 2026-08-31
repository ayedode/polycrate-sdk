from typing import Literal

ApiV1CredentialsReconcileCreateApiUserErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_CREDENTIALS_RECONCILE_CREATE_API_USER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CredentialsReconcileCreateApiUserErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_credentials_reconcile_create_api_user_error_component_code(
    value: str,
) -> ApiV1CredentialsReconcileCreateApiUserErrorComponentCode:
    if value in API_V1_CREDENTIALS_RECONCILE_CREATE_API_USER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_RECONCILE_CREATE_API_USER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
