from typing import Literal

ApiV1KubernetesControlplanesPartialUpdateSecretsEncryptionEnabledErrorComponentAttr = Literal[
    "secrets_encryption_enabled"
]

API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_SECRETS_ENCRYPTION_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesPartialUpdateSecretsEncryptionEnabledErrorComponentAttr
] = {
    "secrets_encryption_enabled",
}


def check_api_v1_kubernetes_controlplanes_partial_update_secrets_encryption_enabled_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesPartialUpdateSecretsEncryptionEnabledErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_SECRETS_ENCRYPTION_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_SECRETS_ENCRYPTION_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
