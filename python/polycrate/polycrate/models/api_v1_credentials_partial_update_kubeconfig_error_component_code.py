from typing import Literal

ApiV1CredentialsPartialUpdateKubeconfigErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_CREDENTIALS_PARTIAL_UPDATE_KUBECONFIG_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CredentialsPartialUpdateKubeconfigErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_credentials_partial_update_kubeconfig_error_component_code(
    value: str,
) -> ApiV1CredentialsPartialUpdateKubeconfigErrorComponentCode:
    if value in API_V1_CREDENTIALS_PARTIAL_UPDATE_KUBECONFIG_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_PARTIAL_UPDATE_KUBECONFIG_ERROR_COMPONENT_CODE_VALUES!r}"
    )
