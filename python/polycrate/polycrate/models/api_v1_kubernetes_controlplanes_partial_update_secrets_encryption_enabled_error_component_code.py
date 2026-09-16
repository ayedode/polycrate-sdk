from typing import Literal

ApiV1KubernetesControlplanesPartialUpdateSecretsEncryptionEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_SECRETS_ENCRYPTION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesControlplanesPartialUpdateSecretsEncryptionEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_controlplanes_partial_update_secrets_encryption_enabled_error_component_code(
    value: str,
) -> ApiV1KubernetesControlplanesPartialUpdateSecretsEncryptionEnabledErrorComponentCode:
    if value in API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_SECRETS_ENCRYPTION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_SECRETS_ENCRYPTION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
