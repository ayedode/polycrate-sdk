from typing import Literal

ApiV1KubernetesControlplanesUpdateSecretsEncryptionEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_CONTROLPLANES_UPDATE_SECRETS_ENCRYPTION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesControlplanesUpdateSecretsEncryptionEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_controlplanes_update_secrets_encryption_enabled_error_component_code(
    value: str,
) -> ApiV1KubernetesControlplanesUpdateSecretsEncryptionEnabledErrorComponentCode:
    if value in API_V1_KUBERNETES_CONTROLPLANES_UPDATE_SECRETS_ENCRYPTION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_UPDATE_SECRETS_ENCRYPTION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
